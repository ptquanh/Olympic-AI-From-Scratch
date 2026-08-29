# Lời giải: Segmentation

<details><summary><b>Tầng 1: Understand</b></summary>
Kỹ thuật Skip-connection ngang trong U-Net giúp nhánh Decoder lấy lại được các chi tiết không gian (spatial details) cực kỳ sắc nét đã bị mất đi do các phép Max Pooling ở nhánh Encoder, từ đó tạo ra mask dự đoán có biên mượt mà và chính xác hơn.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
def dice_coeff(a, b):
    inter = (a * b).sum()
    return 2. * inter / (a.sum() + b.sum() + 1e-6)
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

```python
import torch

def dice_coeff(a, b):
    inter = (a * b).sum()
    return 2. * inter / (a.sum() + b.sum() + 1e-6)

pred_prob = torch.rand(1, 100, 100)
mask_true = torch.randint(0, 2, (1, 100, 100)).float()

mask_pred_03 = (pred_prob > 0.3).float()
mask_pred_07 = (pred_prob > 0.7).float()

print("Dice (Th=0.3):", dice_coeff(mask_pred_03, mask_true).item())
print("Dice (Th=0.7):", dice_coeff(mask_pred_07, mask_true).item())
```

Việc chọn Threshold đóng vai trò lớn trong độ nhạy (Recall) và độ đặc hiệu (Precision) của mô hình phân đoạn.

</details>
