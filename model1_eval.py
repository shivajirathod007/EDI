import json
import numpy as np
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer, util
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix

VAL_PATH = r"C:\Users\shiva\Desktop\EDI\DATASET\model1_validation_1k.jsonl"
MODEL_PATH = "model1_mpnet_relevance"

THRESHOLD = 0.65   # adjustable

def load_validation():
    prompts, memories, labels = [], [], []

    with open(VAL_PATH, "r", encoding="utf-8") as f:
        for line in f:
            row = json.loads(line)
            prompts.append(row["prompt"])
            memories.append(row["memory_item"])
            labels.append(1 if row["relevance_label"] != "not_relevant" else 0)

    return prompts, memories, np.array(labels)

def main():
    print("🧠 Loading model...")
    model = SentenceTransformer(MODEL_PATH)

    prompts, memories, y_true = load_validation()

    print("⚙️ Encoding...")
    emb_p = model.encode(prompts, convert_to_tensor=True, batch_size=32)
    emb_m = model.encode(memories, convert_to_tensor=True, batch_size=32)

    scores = util.cos_sim(emb_p, emb_m).diagonal().cpu().numpy()
    y_pred = (scores >= THRESHOLD).astype(int)

    acc = accuracy_score(y_true, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, average="binary"
    )

    print("\n📊 METRICS")
    print(f"Accuracy : {acc:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    # ================= VISUALIZATION =================
    cm = confusion_matrix(y_true, y_pred)

    plt.figure(figsize=(5,4))
    plt.imshow(cm, cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.colorbar()

    for i in range(2):
        for j in range(2):
            plt.text(j, i, cm[i, j], ha="center", va="center")

    plt.tight_layout()
    plt.show()

    # Score distribution
    plt.figure(figsize=(6,4))
    plt.hist(scores[y_true==1], bins=30, alpha=0.6, label="Relevant")
    plt.hist(scores[y_true==0], bins=30, alpha=0.6, label="Not Relevant")
    plt.axvline(THRESHOLD, color="red", linestyle="--", label="Threshold")
    plt.legend()
    plt.title("Similarity Score Distribution")
    plt.show()

if __name__ == "__main__":
    main()
