# Lời giải: Loss Functions

<details><summary><b>Tầng 1: Understand</b></summary>
Trong các phiên bản PyTorch cũ, `CrossEntropyLoss` KHÔNG nhận `y_true` là One-hot. Nó bắt buộc `y_true` phải là một mảng 1D chứa Class Index (kiểu `torch.long`). Bạn phải dùng lệnh `y_true = torch.argmax(y_true, dim=1)` để chuyển nó về dạng index trước khi tính loss. (Bản mới có hỗ trợ One-hot nhưng dạng Index vẫn là chuẩn mực an toàn nhất).
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
import torch
def manual_mse(y_pred, y_true):
    return torch.mean((y_pred - y_true)**2)
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

torch.manual_seed(42)
y_pred = torch.randn(5, 3)
y_true = torch.tensor([0, 1, 2, 0, 1])

# Cách 1
loss_ce = nn.CrossEntropyLoss()(y_pred, y_true)

# Cách 2
log_probs = F.log_softmax(y_pred, dim=1)
loss_nll = nn.NLLLoss()(log_probs, y_true)

print(loss_ce)
print(loss_nll)
```

Kết quả hoàn toàn khớp nhau (đều ra cùng một con số). Điều này chứng minh CrossEntropyLoss chính xác bằng LogSoftmax + NLLLoss.

</details>
