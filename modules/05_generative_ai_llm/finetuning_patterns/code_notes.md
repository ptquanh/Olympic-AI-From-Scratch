# Code Notes: Fine-tuning Patterns

## 🔑 Core Patterns

### Pattern 1: LoRA Layer From Scratch

```python
# Mô tả: Thay thế Linear layer bằng LoRA Linear layer
# Khi nào dùng: Khi muốn hiểu bản chất toán học của LoRA
import torch
import torch.nn as nn
import math

class LoRALinear(nn.Module):
    def __init__(self, in_features, out_features, r=8, alpha=16):
        super().__init__()
        # Freeze pretrained weight
        self.pretrained = nn.Linear(in_features, out_features, bias=False)
        self.pretrained.weight.requires_grad = False

        # LoRA matrices
        self.lora_A = nn.Parameter(torch.randn(r, in_features) / math.sqrt(in_features))
        self.lora_B = nn.Parameter(torch.zeros(out_features, r))
        self.scaling = alpha / r

    def forward(self, x):
        # W0 * x + (B * A) * x * scaling
        orig_out = self.pretrained(x)
        lora_out = (x @ self.lora_A.T @ self.lora_B.T) * self.scaling
        return orig_out + lora_out
```

**Ghi nhớ:** `lora_B` khởi tạo = 0, `lora_A` khởi tạo ngẫu nhiên. Output cộng thêm scaling.

### Pattern 2: Dùng thư viện PEFT

```python
# Mô tả: Áp dụng LoRA vào model có sẵn bằng HuggingFace peft
# Khi nào dùng: Trong thi đấu hoặc làm dự án thực tế
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")
config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["query", "value"], # Các layer muốn áp dụng LoRA
    lora_dropout=0.1,
    bias="none"
)
peft_model = get_peft_model(model, config)
peft_model.print_trainable_parameters()
```

**Ghi nhớ:** `LoraConfig` định nghĩa r, alpha, và target modules. `get_peft_model` bọc mô hình gốc lại.

## 📋 API Cheat Sheet

| Việc cần làm        | Code                                 | Link Docs                                                                                                |
| ------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Load PEFT model     | `get_peft_model(model, config)`      | [PEFT Docs](https://huggingface.co/docs/peft/index)                                                      |
| In số lượng tham số | `model.print_trainable_parameters()` | [PEFT Model](https://huggingface.co/docs/peft/main/en/package_reference/peft_model)                      |
| Merge LoRA vào gốc  | `model.merge_and_unload()`           | [Merging](https://huggingface.co/docs/peft/developer_guides/lora#merge-lora-weights-into-the-base-model) |

## 🏋️ Bài Luyện Code Tay

**Quy tắc:** Đóng tài liệu. Mở notebook trống. Hẹn giờ.

| #   | Bài                                        | Thời gian | Hint (ẩn)                                  |
| --- | ------------------------------------------ | --------- | ------------------------------------------ |
| 1   | Viết class `LoRALinear` thay thế nn.Linear | 10 phút   | Cần nn.Parameter cho A và B. $B \times A$. |
| 2   | Config HuggingFace PEFT cho model GPT-2    | 5 phút    | `target_modules=["c_attn"]`                |

## 🧠 Flashcards

| Hỏi                               | Trả lời                                                                             |
| --------------------------------- | ----------------------------------------------------------------------------------- |
| Ý tưởng chính của LoRA?           | Phân rã ma trận cập nhật trọng số $\Delta W$ thành tích 2 ma trận nhỏ $B \times A$. |
| Tại sao $B$ phải khởi tạo bằng 0? | Để bước đầu tiên $\Delta W = 0$, mô hình hoạt động hệt như lúc chưa fine-tune.      |
| Có bị trễ khi inference không?    | Không, ta có thể cộng gộp $W_{new} = W_0 + B \times A$ vào trọng số gốc.            |
