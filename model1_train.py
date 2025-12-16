import os
import torch
from torch.utils.data import DataLoader
from sentence_transformers import SentenceTransformer, losses
from model1_dataset import Model1Dataset

# ================= PATHS =================
TRAIN_PATH = r"C:\Users\shiva\Desktop\EDI\DATASET\model1_training_70k.jsonl"
VAL_PATH   = r"C:\Users\shiva\Desktop\EDI\DATASET\model1_validation_1k.jsonl"
OUTPUT_DIR = "model1_mpnet_relevance"

# ================= CONFIG =================
MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
BATCH_SIZE = 32
EPOCHS = 3
LR = 2e-5
WARMUP_STEPS = 500

def main():
    print("🚀 Loading datasets...")
    train_dataset = Model1Dataset(TRAIN_PATH, debug=True)
    val_dataset   = Model1Dataset(VAL_PATH, debug=True)

    train_loader = DataLoader(train_dataset, shuffle=True, batch_size=BATCH_SIZE)
    val_loader   = DataLoader(val_dataset, shuffle=False, batch_size=BATCH_SIZE)

    print("🧠 Loading model...")
    model = SentenceTransformer(MODEL_NAME)

    loss_fn = losses.CosineSimilarityLoss(model)

    print("🔥 Training started...")
    model.fit(
        train_objectives=[(train_loader, loss_fn)],
        epochs=EPOCHS,
        optimizer_params={"lr": LR},
        warmup_steps=WARMUP_STEPS,
        show_progress_bar=True,
        evaluator=None
    )

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    model.save(OUTPUT_DIR)

    print(f"\n✅ Model saved at: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
