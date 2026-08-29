# Code Notes: Text Classification Pipeline

## 🔑 Core Patterns

### Pattern 1: Chuẩn bị Dataset cho HuggingFace

Trong PyTorch, ta phải bọc output của Tokenizer vào một class `Dataset`.

```python
import torch
from torch.utils.data import Dataset

class TextDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_length=128):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = str(self.texts[idx])
        label = self.labels[idx]

        # Tokenizer trả về dictionary chứa input_ids và attention_mask
        encoding = self.tokenizer(
            text,
            truncation=True,
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt'
        )

        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'labels': torch.tensor(label, dtype=torch.long)
        }
```

### Pattern 2: Fine-Tuning Loop cho HuggingFace Model

```python
# Gọi model(input_ids, attention_mask, labels) của HF sẽ TỰ ĐỘNG TÍNH LOSS
for batch in train_loader:
    optimizer.zero_grad()

    input_ids = batch['input_ids'].to(device)
    attention_mask = batch['attention_mask'].to(device)
    labels = batch['labels'].to(device)

    # HF Model trả về một object chứa loss và logits
    outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)

    loss = outputs.loss
    loss.backward()

    # Clip gradient để tránh nổ gradient (rất phổ biến trong Transformer)
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

    optimizer.step()
    scheduler.step() # Nhớ step cả scheduler!
```

## 📋 API Cheat Sheet

| Việc cần làm        | Code (HuggingFace)                                                              | Link Docs                                                                                                                     |
| ------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Tải Tokenizer       | `AutoTokenizer.from_pretrained('tên_model')`                                    | [AutoTokenizer](https://huggingface.co/docs/transformers/model_doc/auto#transformers.AutoTokenizer)                           |
| Tải Model Phân loại | `AutoModelForSequenceClassification.from_pretrained('tên_model', num_labels=2)` | [AutoModelForSeqCls](https://huggingface.co/docs/transformers/model_doc/auto#transformers.AutoModelForSequenceClassification) |

### 🧠 Flashcards

| Hỏi                                                         | Trả lời                                   |
| ----------------------------------------------------------- | ----------------------------------------- |
| Loss function nào dùng cho Multi-class Text Classification? | CrossEntropyLoss.                         |
| Loss function nào dùng cho Multi-label Text Classification? | BCEWithLogitsLoss (Binary Cross Entropy). |
