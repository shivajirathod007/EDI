import json
from torch.utils.data import Dataset
from sentence_transformers import InputExample

LABEL_MAP = {
    "highly_relevant": 1.0,
    "relevant": 1.0,
    "not_relevant": 0.0
}

class Model1Dataset(Dataset):
    def __init__(self, jsonl_path, debug=False):
        self.samples = []
        self.debug = debug

        with open(jsonl_path, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f):
                try:
                    row = json.loads(line)

                    prompt = row["prompt"].strip()
                    memory = row["memory_item"].strip()
                    label = LABEL_MAP[row["relevance_label"]]

                    if not prompt or not memory:
                        continue

                    self.samples.append(
                        InputExample(
                            texts=[prompt, memory],
                            label=label
                        )
                    )

                except Exception as e:
                    if self.debug:
                        print(f"[SKIP] Line {idx}: {e}")

        if self.debug:
            print(f"[INFO] Loaded {len(self.samples)} samples from {jsonl_path}")

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        return self.samples[idx]
