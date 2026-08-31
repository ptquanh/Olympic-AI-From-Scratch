# Bài tập: Loss Functions

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Lỗi phổ biến với CrossEntropyLoss**
Bạn có `y_pred` kích thước (Batch, 10) và `y_true` là dạng One-hot vector kích thước (Batch, 10). Bạn đưa vào `nn.CrossEntropyLoss(y_pred, y_true)` và PyTorch báo lỗi. Tại sao?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Tự code MSE**
Viết hàm tính MSE bằng PyTorch Tensor thuần mà không dùng `nn.MSELoss`.

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Cross Entropy vs NLLLoss**
Tính Cross Entropy Loss của mảng logits ngẫu nhiên `y_pred = torch.randn(5, 3)` và nhãn `y_true = torch.tensor([0, 1, 2, 0, 1])` bằng 2 cách: dùng `nn.CrossEntropyLoss` và dùng `nn.LogSoftmax()` kết hợp `nn.NLLLoss`. So sánh hai kết quả xem có khớp hoàn toàn không.

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
