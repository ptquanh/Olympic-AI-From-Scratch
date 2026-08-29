# Lời giải: Optimization

<details><summary><b>Tầng 1: Understand</b></summary>
Nếu LR quá lớn, mô hình sẽ không bao giờ chạm được đến đáy của Loss (hội tụ) mà cứ bật qua bật lại hai bên vách đá. Nếu LR quá nhỏ, mô hình sẽ chạy cực kỳ chậm và mất hàng tháng trời để hội tụ, hoặc mắc kẹt ở một vách đá nông nào đó.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
import torch
import torch.optim as optim
import matplotlib.pyplot as plt

model = torch.nn.Linear(10, 2)
optimizer = optim.Adam(model.parameters(), lr=0.1)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=100)

lrs = []
for epoch in range(100):
    lrs.append(scheduler.get_last_lr()[0])
    optimizer.step()
    scheduler.step()

plt.plot(lrs)
plt.title("Cosine Annealing Learning Rate")
plt.xlabel("Epoch")
plt.ylabel("LR")
plt.show()
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>
Adam hội tụ nhanh và ổn định hơn rất nhiều. Hàm Rosenbrock có một thung lũng rất hẹp hình mặt trăng khuyết. SGD sẽ đi zigzag và mất hàng chục ngàn vòng lặp mới tới được đích $(1, 1)$. Adam có xung lượng (Momentum) và cập nhật LR riêng cho từng chiều (RMSProp) nên nó luồn lách qua thung lũng rất mượt.
</details>
