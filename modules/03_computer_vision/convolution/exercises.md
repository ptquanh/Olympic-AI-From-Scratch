# Bài tập: Convolution

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Tại sao cần nhiều Out Channels?**
Nếu ảnh đầu vào chỉ có 3 kênh (RGB), tại sao tầng Conv2D tiếp theo người ta thường thiết kế tới 16, 32, hoặc 64 `out_channels`?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Tính tay kích thước Output**
Cho một ảnh đầu vào có kích thước (128, 128). Tầng Conv2D có:

- Kernel size = 5x5
- Stride = 3
- Padding = 2
  Hỏi kích thước (Width, Height) của output là bao nhiêu?

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Phát hiện cạnh (Edge Detection)**
Viết một hàm Python sử dụng thư viện `cv2` đọc một bức ảnh bất kỳ.
Định nghĩa một kernel (matrix 3x3) dùng để phát hiện cạnh dọc (Sobel dọc):

`[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]`
Thực hiện phép chập (có thể dùng `cv2.filter2D`) để xem ảnh sẽ biến đổi như thế nào.

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.

## T-1 — Transfer

**Learning outcome:** Chuyển kỹ thuật sang dữ liệu mới mà không leakage, dùng metric và failure mode phù hợp.

**1. Flattening**
Trong mạng CNN, sau khi đi qua các tầng Conv, dữ liệu thường có dạng `(Batch, Channels, H, W)`. Để đưa vào mạng Linear cuối cùng nhằm phân loại, ta phải duỗi phẳng (Flatten) dữ liệu.
Hãy dùng `nn.Flatten()` hoặc `.view()` để duỗi một tensor `torch.randn(32, 16, 8, 8)` thành `(32, 1024)`.

**Kết quả mong đợi:** Pipeline chạy trên dữ liệu/bối cảnh mới, metric phù hợp và phân tích ít nhất một failure mode.

## O-1 — Olympiad

**Learning outcome:** Dựng baseline theo đúng competition profile, timebox và artifact nộp có thể chạy lại.

Trong thi đấu, bạn KHÔNG BAO GIỜ tự viết Conv2D bằng Numpy (vì cực chậm). Tuy nhiên, bạn phải nắm cực chắc công thức tính Shape để thiết kế mạng không bị lỗi "Shape mismatch" khi nối Conv Layer sang Linear Layer.

**Kết quả mong đợi:** Baseline tái lập được trong timebox, validation đúng, metric và checklist file cần nộp.
