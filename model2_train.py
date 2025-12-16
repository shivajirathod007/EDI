import json
import torch
from torch.utils.data import Dataset
from transformers import (
    T5Tokenizer,
    T5ForConditionalGeneration,
    Trainer,
    TrainingArguments,
    DataCollatorForSeq2Seq
)
import nltk
nltk.download("punkt")

import evaluate

# =========================================================
# CONFIG
# =========================================================

MODEL_NAME = "google/flan-t5-base"

TRAIN_PATH = "edi_model2_train.jsonl"
VAL_PATH   = "edi_model2_val.jsonl"

OUTPUT_DIR = "./model2_slm"

MAX_LEN = 512
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

print(f"🧠 Device detected: {DEVICE}")

# =========================================================
# DATASET
# =========================================================

class Model2Dataset(Dataset):
    def __init__(self, path, tokenizer, max_len=512):
        self.tokenizer = tokenizer
        self.max_len = max_len
        self.samples = []

        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                self.samples.append(json.loads(line))

        print(f"📥 Loaded {len(self.samples)} samples from {path}")

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        item = self.samples[idx]

        # -------- Build memory block --------
        memories = ""
        for m in item.get("retrieved_memories", []):
            memories += f"- {m['memory_text']} ({m['memory_type']}, {m['relevance']})\n"

        if not memories:
            memories = "None"

        # -------- INPUT --------
        input_text = (
            f"Instruction:\n{item['instruction']}\n\n"
            f"Raw Prompt:\n{item['raw_prompt']}\n\n"
            f"Memories:\n{memories}\n\n"
            f"Task Type:\n{item['task_type']}"
        )

        # -------- TARGET --------
        target_text = item["expected_output"]["final_prompt"]

        # -------- TOKENIZE INPUT --------
        model_inputs = self.tokenizer(
            input_text,
            max_length=self.max_len,
            truncation=True,
            padding="max_length",
            return_tensors="pt"
        )

        # -------- TOKENIZE TARGET --------
        labels = self.tokenizer(
            target_text,
            max_length=self.max_len,
            truncation=True,
            padding="max_length",
            return_tensors="pt"
        )

        label_ids = labels["input_ids"][0]
        label_ids[label_ids == self.tokenizer.pad_token_id] = -100

        return {
            "input_ids": model_inputs["input_ids"][0],
            "attention_mask": model_inputs["attention_mask"][0],
            "labels": label_ids
        }

# =========================================================
# METRICS (ROUGE-L — CORRECT WAY)
# =========================================================

rouge = evaluate.load("rouge")

def compute_metrics(eval_preds):
    preds, labels = eval_preds

    # Decode predictions
    decoded_preds = tokenizer.batch_decode(
        preds, skip_special_tokens=True
    )

    # Decode labels
    labels = torch.tensor(labels)
    labels[labels == -100] = tokenizer.pad_token_id

    decoded_labels = tokenizer.batch_decode(
        labels, skip_special_tokens=True
    )

    scores = rouge.compute(
        predictions=decoded_preds,
        references=decoded_labels
    )

    return {
        "rougeL": scores["rougeL"]
    }

# =========================================================
# LOAD MODEL & TOKENIZER
# =========================================================

tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
model.to(DEVICE)

# =========================================================
# DATASETS
# =========================================================

train_dataset = Model2Dataset(TRAIN_PATH, tokenizer, MAX_LEN)
val_dataset   = Model2Dataset(VAL_PATH, tokenizer, MAX_LEN)

# =========================================================
# TRAINING ARGS (PRODUCTION-GRADE)
# =========================================================

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,

    evaluation_strategy="steps",
    save_strategy="steps",

    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    gradient_accumulation_steps=4,

    learning_rate=2e-5,
    num_train_epochs=3,

    logging_steps=100,
    eval_steps=500,
    save_steps=500,

    save_total_limit=2,
    load_best_model_at_end=True,
    metric_for_best_model="rougeL",

    fp16=torch.cuda.is_available(),
    predict_with_generate=True,

    report_to="none"
)

# =========================================================
# TRAINER
# =========================================================

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer,
    data_collator=DataCollatorForSeq2Seq(tokenizer, model),
    compute_metrics=compute_metrics
)

# =========================================================
# TRAIN
# =========================================================

print("🔥 Training Model-2 started...")
trainer.train()

# =========================================================
# SAVE
# =========================================================

trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print(f"\n✅ Model-2 training complete.")
print(f"📦 Saved at: {OUTPUT_DIR}")
