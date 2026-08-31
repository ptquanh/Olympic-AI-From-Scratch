# Code Notes: Language Modeling

> ⚠️ **Online/optional appendix:** một số snippet bên dưới cần package hoặc model cache bổ sung và có thể tải dữ liệu ở lần chạy đầu. Chúng không competition-safe nếu profile chính thức không cho phép rõ ràng. Notebook chính của chương luôn có đường chạy fast/offline và không tự cài/tải.

## 🔑 Core Patterns

### Pattern 1: HuggingFace Pipeline (Text Generation)

```python
# Mô tả: Sinh văn bản tự động bằng mô hình Causal LM
# Khi nào dùng: Khi cần sinh text nhanh không cần cấu hình phức tạp
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
out = generator("Artificial Intelligence is", max_length=30, num_return_sequences=1)
print(out[0]['generated_text'])

```

**Ghi nhớ:** Dùng `pipeline("text-generation")` cho Causal LM.

### Pattern 2: Tính Perplexity từ CrossEntropyLoss

```python
# Mô tả: Tính Perplexity từ kết quả hàm loss
import torch
import torch.nn as nn
import math

loss_fn = nn.CrossEntropyLoss()
# Giả sử logits có shape (batch_size, num_classes) và target có shape (batch_size)
logits = torch.tensor([[2.0, 1.0, 0.1], [0.5, 2.5, 0.3]])
targets = torch.tensor([0, 1])

loss = loss_fn(logits, targets)
perplexity = math.exp(loss.item())
print(f"Loss: {loss.item():.4f}, Perplexity: {perplexity:.4f}")

```

**Ghi nhớ:** `PPL = exp(CrossEntropyLoss)`.

## 📋 API Cheat Sheet

| Việc cần làm        | Code                                       | Link Docs                                                                            |
| ------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------ |
| Load LM pipeline    | `pipeline("text-generation", model="...")` | [HF Pipeline](https://huggingface.co/docs/transformers/main_classes/pipelines)       |
| Sampling (Nhiệt độ) | `generator("...", temperature=0.7)`        | [HF Text Generation](https://huggingface.co/docs/transformers/generation_strategies) |

## 🏋️ Bài Luyện Code Tay

**Quy tắc:** Đóng tài liệu. Mở notebook trống. Hẹn giờ.

| #   | Bài                                                                | Thời gian | Hint (ẩn)                                   |
| --- | ------------------------------------------------------------------ | --------- | ------------------------------------------- |
| 1   | Load GPT-2 pipeline và sinh văn bản dài 50 tokens                  | 5 phút    | `pipeline("text-generation", model="gpt2")` |
| 2   | Code hàm tính PPL từ mảng các giá trị Cross Entropy Loss (PyTorch) | 10 phút   | `torch.exp(loss.mean())`                    |

## 🧠 Flashcards

| Hỏi                                      | Trả lời                                                          |
| ---------------------------------------- | ---------------------------------------------------------------- |
| Autoregressive LM là gì?                 | Mô hình dự đoán token kế tiếp dựa trên các token trước đó.       |
| Masked LM là gì?                         | Mô hình dự đoán token bị che ở giữa câu dựa trên văn cảnh 2 bên. |
| Công thức tính Perplexity (PPL) từ Loss? | PPL = exp(Cross Entropy Loss)                                    |
| Tại sao PPL lại quan trọng?              | Nó đánh giá mức độ chắc chắn của mô hình khi sinh chuỗi từ.      |
