# Lời giải: Loss Functions

<details><summary><b>Tầng 1: Understand</b></summary>
Trong các phiên bản PyTorch cũ, `CrossEntropyLoss` KHÔNG nhận `y_true` là One-hot. Nó bắt buộc `y_true` phải là một mảng 1D chứa Class Index (kiểu `torch.long`). Bạn phải dùng lệnh `y_true = torch.argmax(y_true, dim=1)` để chuyển nó về dạng index trước khi tính loss. (Bản mới có hỗ trợ One-hot nhưng dạng Index vẫn là chuẩn mực an toàn nhất).
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
def manual_mse(y_pred, y_true):
    return torch.mean((y_pred - y_true)**2)
```

</details>
