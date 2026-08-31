# Lời giải: Fine-tuning Patterns

<details><summary><b>U-1 — Understand</b></summary>

1. Số lượng tham số Linear gốc: $1024 \times 1024 = 1,048,576$.
   Số lượng tham số LoRA ($r=8$): $A(8 \times 1024) + B(1024 \times 8) = 8192 + 8192 = 16,384$.
2. Nếu cả A và B đều bằng 0, gradient truyền ngược qua phép nhân $B \times A$ sẽ bằng 0 cho cả 2 ma trận (do đạo hàm của u\*v là u'v + uv'). Cả A và B sẽ không bao giờ được cập nhật. Do đó, A được khởi tạo random (phá vỡ tính đối xứng) và B bằng 0.
3. `scaling` giúp làm mượt quá trình học. Khi ta đổi rank $r$, tổng các giá trị trong phép nhân $B \times A$ sẽ thay đổi. Chia cho $r$ giúp output luôn ổn định dù cấu hình rank khác nhau.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

```python
# Xem code trong phần Code Notes Pattern 1.
class LoRALinear(nn.Module):
    # ...

```

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

1. Rank cao hơn tăng số bậc tự do nhưng không bảo đảm train loss giảm nhanh hay validation tốt hơn. So sánh rank trên cùng split, budget và seed; không có `r=8/16` tối ưu chung.
2. `query`/`value` là lựa chọn thường gặp, không phải luôn tốt nhất. Tên target module phụ thuộc kiến trúc; kiểm trainable parameter count và ablation thay vì copy cấu hình.

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>

<details><summary><b>T-1 — Transfer</b></summary>

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

**Lỗi thường gặp:** fit preprocessing/chọn threshold trên test, dùng metric sai hoặc bỏ qua failure mode.

</details>

<details><summary><b>O-1 — Olympiad</b></summary>

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

**Lỗi thường gặp:** áp luật của kỳ thi khác, không lưu config/artifact hoặc hết timebox mà chưa chạy infer cuối.

</details>
