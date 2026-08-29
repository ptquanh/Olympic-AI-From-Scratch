# Lời giải: Optimization

<details><summary><b>Tầng 1: Understand</b></summary>
Nếu LR quá lớn, mô hình sẽ không bao giờ chạm được đến đáy của Loss (hội tụ) mà cứ bật qua bật lại hai bên vách đá. Nếu LR quá nhỏ, mô hình sẽ chạy cực kỳ chậm và mất hàng tháng trời để hội tụ, hoặc mắc kẹt ở một vách đá nông nào đó. Tìm được LR chuẩn bằng thuật toán Adam/AdamW là bí quyết thành bại.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# Tạo mô hình ảo
model = nn.Linear(10, 2)

# Khởi tạo AdamW và CosineAnnealingLR
optimizer = optim.AdamW(model.parameters(), lr=0.01)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=100)

lrs = []
for epoch in range(100):
    # Lấy LR hiện tại
    current_lr = scheduler.get_last_lr()[0]
    lrs.append(current_lr)

    # Bước nhảy ảo
    optimizer.step()
    scheduler.step()

# Vẽ đồ thị
plt.plot(lrs)
plt.title("Cosine Annealing Learning Rate")
plt.xlabel("Epoch")
plt.ylabel("Learning Rate")
plt.show()
```

Đồ thị sẽ vẽ ra một nửa hình chuông úp ngược (đường cong Cosine), giảm dần mượt mà từ 0.01 về 0.

</details>
