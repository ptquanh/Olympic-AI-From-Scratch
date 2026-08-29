# Lời giải: Fine-tuning Patterns

<details><summary><b>Tầng 1: Understand</b></summary>

1. Số lượng tham số Linear gốc: $1024 \times 1024 = 1,048,576$.
   Số lượng tham số LoRA ($r=8$): $A(8 \times 1024) + B(1024 \times 8) = 8192 + 8192 = 16,384$.
2. Nếu cả A và B đều bằng 0, gradient truyền ngược qua phép nhân $B \times A$ sẽ bằng 0 cho cả 2 ma trận (do đạo hàm của u\*v là u'v + uv'). Cả A và B sẽ không bao giờ được cập nhật. Do đó, A được khởi tạo random (phá vỡ tính đối xứng) và B bằng 0.
3. `scaling` giúp làm mượt quá trình học. Khi ta đổi rank $r$, tổng các giá trị trong phép nhân $B \times A$ sẽ thay đổi. Chia cho $r$ giúp output luôn ổn định dù cấu hình rank khác nhau.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
# Xem code trong phần Code Notes Pattern 1.
class LoRALinear(nn.Module):
    # ...
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

1. Đúng, khi rank cao hơn, năng lực biểu diễn của mô hình cũng lớn hơn, vì vậy trên tập huấn luyện loss có thể giảm nhanh hơn. Tuy nhiên, r quá lớn làm mất lợi thế về tốc độ và dễ bị overfit trên tập dữ liệu nhỏ. Thông thường, r=8 hoặc r=16 là điểm cân bằng tốt nhất.
2. Áp dụng LoRA vào cả `query` và `value` thường mang lại chất lượng tốt nhất trong khi số lượng tham số vẫn giữ ở mức cực nhỏ so với full fine-tuning.

</details>

<details><summary><b>Tầng 4: Transfer</b></summary>

Trong PyTorch, `peft` đã hỗ trợ sẵn LoRA cho Conv2d, nhưng nếu viết tay:

```python
class LoRAConv2d(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, r=8):
        super().__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size, bias=False)
        self.conv.weight.requires_grad = False

        # A: (r, in_channels * k * k)
        # B: (out_channels, r)
        self.lora_A = nn.Parameter(torch.randn(r, in_channels * kernel_size * kernel_size))
        self.lora_B = nn.Parameter(torch.zeros(out_channels, r))
        self.kernel_size = kernel_size

    def forward(self, x):
        orig = self.conv(x)
        # Flatten input: x_unfold shape (batch, in_c*k*k, L)
        # Compute LoRA updates manually or by combining 1x1 convs
        # Cách dễ hơn: Dùng 2 lớp conv1x1
        # self.lora_A = nn.Conv2d(in_c, r, kernel_size, bias=False)
        # self.lora_B = nn.Conv2d(r, out_c, 1, bias=False)
```

_Cách chuẩn: Dùng 2 hàm nn.Conv2d liên tiếp, 1 cái giảm chiều xuống $r$ (với kernel gốc), 1 cái tăng lên $out\_channels$ (kernel 1x1)._

</details>

<details><summary><b>Tầng 5: Olympiad</b></summary>

```python
# Cấu hình LoRA cho phân loại văn bản với PhoBERT
from peft import LoraConfig, get_peft_model, TaskType
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("vinai/phobert-base", num_labels=2)
peft_config = LoraConfig(
    task_type=TaskType.SEQ_CLS,
    r=8,
    lora_alpha=32,
    lora_dropout=0.1,
    target_modules=["query", "value"]
)
peft_model = get_peft_model(model, peft_config)
peft_model.print_trainable_parameters()
```

</details>
