# Lời giải: Backprop & Training Loop

<details><summary><b>U-1 — Understand</b></summary>

Không có activation phi tuyến, hợp thành các affine layer vẫn là một affine map duy nhất: `W_eff x + b_eff`. Vì vậy độ sâu không tăng lớp hàm biểu diễn. Với output/loss phù hợp nó vẫn giải được bài toán tuyến tính, nhưng không biểu diễn được ranh giới phi tuyến như XOR. Activation tạo khả năng biểu diễn phi tuyến; không nên mô tả nó như tự tạo ra “trí tuệ”.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

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

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

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

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>

<details><summary><b>T-1 — Transfer</b></summary>

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

**Lỗi thường gặp:** fit preprocessing/chọn threshold trên test, dùng metric sai hoặc bỏ qua failure mode.

</details>

<details><summary><b>O-1 — Olympiad</b></summary>

Đáp án là một quy trình: baseline sớm, validation chống leakage, lưu seed/config, theo dõi metric và dành thời gian tái chạy artifact cuối. Chi tiết phụ thuộc profile kỳ thi; xem `olympiad_transfer.md`.

**Lỗi thường gặp:** áp luật của kỳ thi khác, không lưu config/artifact hoặc hết timebox mà chưa chạy infer cuối.

</details>
