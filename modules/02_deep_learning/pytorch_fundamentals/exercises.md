# Bài tập: PyTorch Fundamentals

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Tại sao PyTorch Tensor cần hàm `.item()`?**
Nếu bạn in ra biến `loss` (là 1 tensor chứa duy nhất 1 con số), bạn sẽ thấy nó in ra kiểu `tensor(2.541, requires_grad=True)`. Để in ra con số thuần túy `2.541` cho gọn gàng, ta dùng lệnh `loss.item()`. Tại sao không lấy thẳng mà phải cần hàm `.item()`?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Thao tác Shape (Rất quan trọng trong Computer Vision)**
Cho một tensor đóng giả là tập dữ liệu gồm 100 ảnh màu cỡ 32x32: `X = torch.randn(100, 32, 32, 3)`.
Yêu cầu:

1. Chuyển nó về đúng chuẩn PyTorch (N, C, H, W) là `(100, 3, 32, 32)`.
2. Giả sử ta muốn làm phẳng ảnh để đưa vào mạng MLP, hãy reshape nó về dạng `(100, 3072)`. (Gợi ý: Dùng `view()` hoặc `reshape()`).

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Tốc độ CPU vs GPU**
Sử dụng hàm `time.time()`.
Tạo 2 ma trận cực lớn: `A = torch.randn(10000, 10000)` và `B = torch.randn(10000, 10000)`.
Lần 1: Thực hiện nhân ma trận `C = A @ B` trên CPU và đo thời gian.
Lần 2: Chuyển A và B sang GPU (`.to('cuda')`), thực hiện phép nhân trên GPU và đo thời gian. So sánh!

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.

## Tầng 4: Transfer

**1. Custom Dataset với phép biến đổi (Transforms)**
Trong thi đấu thực tế, dataset thường là một list các đường dẫn file ảnh. Khi gọi `__getitem__(self, idx)`, ta mới đọc file ảnh đó lên. Hãy giả lập viết một `ImageDataset` nhận vào 1 mảng các đường dẫn string `image_paths`. Trong hàm `__getitem__`, hãy trả về string path đó và một nhãn giả (0 hoặc 1).

## Tầng 5: Olympiad

**1. Viết Training Loop chuẩn**
Trong phòng thi, bạn phải thuộc lòng cấu trúc của một vòng lặp huấn luyện chuẩn.
Yêu cầu: Không nhìn tài liệu, hãy gõ lại 5 bước cơ bản của training loop trong 1 mini-batch (Zero grad, Forward, Loss, Backward, Step). Viết đoạn code giả (pseudo-code) bằng Python minh họa 5 bước này. (Bạn có đúng 3 phút).
