# Bài tập: Loss Functions

## Tầng 1: Understand

**1. Lỗi phổ biến với CrossEntropyLoss**
Bạn có `y_pred` kích thước (Batch, 10) và `y_true` là dạng One-hot vector kích thước (Batch, 10). Bạn đưa vào `nn.CrossEntropyLoss(y_pred, y_true)` và PyTorch báo lỗi. Tại sao?

## Tầng 2: Implement

**1. Tự code MSE**
Viết hàm tính MSE bằng PyTorch Tensor thuần mà không dùng `nn.MSELoss`.

## Tầng 3: Experiment

**1. Cross Entropy vs NLLLoss**
Tính Cross Entropy Loss của mảng logits ngẫu nhiên `y_pred = torch.randn(5, 3)` và nhãn `y_true = torch.tensor([0, 1, 2, 0, 1])` bằng 2 cách: dùng `nn.CrossEntropyLoss` và dùng `nn.LogSoftmax()` kết hợp `nn.NLLLoss`. So sánh hai kết quả xem có khớp hoàn toàn không.
