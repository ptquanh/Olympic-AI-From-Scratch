# Bài tập: Loss Functions

## Tầng 1: Understand

**1. Lỗi phổ biến với CrossEntropyLoss**
Bạn có `y_pred` kích thước (Batch, 10) và `y_true` là dạng One-hot vector kích thước (Batch, 10). Bạn đưa vào `nn.CrossEntropyLoss(y_pred, y_true)` và PyTorch báo lỗi. Tại sao?

## Tầng 2: Implement

**1. Tự code MSE**
Viết hàm tính MSE bằng PyTorch Tensor thuần mà không dùng `nn.MSELoss`.
