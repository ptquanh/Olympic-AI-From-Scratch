# Lời giải: Backprop & Training Loop

<details><summary><b>Tầng 1: Understand</b></summary>

Nếu không có hàm kích hoạt phi tuyến tính (non-linear activation function), thì việc bạn xếp chồng 100 tầng tuyến tính cũng chỉ tương đương về mặt toán học với việc dùng ĐÚNG 1 TẦNG tuyến tính duy nhất. Mạng khổng lồ của bạn sẽ thoái hóa thành một mô hình Hồi quy Tuyến tính (Linear Regression) thông thường và vĩnh viễn không bao giờ giải được các bài toán phức tạp (như phân loại ảnh, dịch máy). Hàm phi tuyến tính bẻ cong không gian dữ liệu, tạo ra "trí tuệ" cho mạng nơ-ron.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
initial_lr = 0.1
for epoch in range(150):
    # Cập nhật Learning rate giảm dần
    lr = initial_lr - 0.09 * (epoch / 150)

    # ... (Các bước Forward, Loss, Zero Grad, Backward) ...

    # Gradient Descent với lr động
    for p in model.parameters():
        p.data -= lr * p.grad
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

(Mã nguồn tham khảo - có thể chạy hơi chậm vì đây là code Python thuần, không tối ưu C/C++)

```python
# Giả sử X, y là list các cặp (x1, x2) và nhãn (-1 hoặc 1)
model = MLP(2, [16, 16, 1])

for k in range(100):
    # Forward
    scores = list(map(model, X))

    # Hinge Loss (dành cho SVM/Phân loại nhị phân -1, 1)
    losses = [(1 + -yi*scorei).relu() for yi, scorei in zip(y, scores)]
    data_loss = sum(losses) * (1.0 / len(losses))

    # Zero grad
    for p in model.parameters():
        p.grad = 0.0

    # Backward
    data_loss.backward()

    # Update
    learning_rate = 0.1 - 0.09 * (k/100)
    for p in model.parameters():
        p.data -= learning_rate * p.grad

    if k % 10 == 0:
        print(f"step {k} loss {data_loss.data}")
```

</details>

<details><summary><b>Tầng 4: Transfer</b></summary>

```python
import torch
import torch.nn as nn

# Định nghĩa mạng
model = nn.Sequential(
    nn.Linear(2, 16),
    nn.ReLU(),
    nn.Linear(16, 16),
    nn.ReLU(),
    nn.Linear(16, 1)
)

criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# X, y giả định
X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.float32).view(-1, 1)

for epoch in range(100):
    optimizer.zero_grad()

    preds = model(X_tensor)
    loss = criterion(preds, y_tensor)

    loss.backward()
    optimizer.step()
```

Đoạn code cực kỳ súc tích nhưng làm được mọi việc của 100 dòng code Python phức tạp ban nãy!

</details>
