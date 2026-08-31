# Code Notes: Optimization

## 🔑 Core Patterns

```python
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR, CosineAnnealingLR

# 1. AdamW (baseline phổ biến; không mặc định tốt nhất cho mọi bài toán)
optimizer = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-2)

# 2. Đưa Scheduler vào vòng lặp huấn luyện
scheduler = CosineAnnealingLR(optimizer, T_max=100)

for epoch in range(100):
    for X, y in dataloader:
        optimizer.zero_grad()
        loss = criterion(model(X), y)
        loss.backward()
        optimizer.step()

    # Ở cuối mỗi Epoch, gọi Scheduler để giảm dần Learning Rate
    scheduler.step()

```

## 📋 API Cheat Sheet

| API                   | Dùng khi                    |
| --------------------- | --------------------------- |
| `torch.optim.SGD`     | SGD/momentum                |
| `torch.optim.AdamW`   | decoupled weight decay      |
| `optimizer.zero_grad` | clear accumulated gradients |

## 🧠 Flashcards

| Hỏi                                | Trả lời                                                                                                                                                                                                |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Momentum hoạt động như thế nào?    | Giống như một quả cầu lăn xuống dốc, nó tích lũy "đà" từ các bước trước đó. Giúp mô hình vượt qua được các hố nhỏ (local minima) và hội tụ nhanh hơn.                                                  |
| Tại sao gọi là AdamW thay vì Adam? | Chữ W là Weight Decay (Regularization). Ở Adam cũ, Weight Decay bị lỗi cài đặt khiến nó không hoạt động đúng chức năng. AdamW đã sửa lỗi này và giúp mô hình khái quát hóa (generalize) tốt hơn nhiều. |

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                                                           | Thời gian | Hint (ẩn)                                                           |
| --- | --------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------- |
| 1   | Khởi tạo optimizer AdamW với learning rate 0.001, weight decay 0.01 cho `model.parameters()`. | 1 phút    | `torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-2)` |
| 2   | Khởi tạo CosineAnnealingLR scheduler với T_max=100.                                           | 1 phút    | `torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=100)`  |
