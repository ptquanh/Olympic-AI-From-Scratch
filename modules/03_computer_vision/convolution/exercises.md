# Bài tập: Convolution

## Tầng 1: Understand

**1. Tại sao cần nhiều Out Channels?**
Nếu ảnh đầu vào chỉ có 3 kênh (RGB), tại sao tầng Conv2D tiếp theo người ta thường thiết kế tới 16, 32, hoặc 64 `out_channels`?

## Tầng 2: Implement

**1. Tính tay kích thước Output**
Cho một ảnh đầu vào có kích thước (128, 128). Tầng Conv2D có:

- Kernel size = 5x5
- Stride = 3
- Padding = 2
  Hỏi kích thước (Width, Height) của output là bao nhiêu?

## Tầng 3: Experiment

**1. Phát hiện cạnh (Edge Detection)**
Viết một hàm Python sử dụng thư viện `cv2` đọc một bức ảnh bất kỳ.
Định nghĩa một kernel (matrix 3x3) dùng để phát hiện cạnh dọc (Sobel dọc):
`[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]`
Thực hiện phép chập (có thể dùng `cv2.filter2D`) để xem ảnh sẽ biến đổi như thế nào.

## Tầng 4: Transfer

**1. Flattening**
Trong mạng CNN, sau khi đi qua các tầng Conv, dữ liệu thường có dạng `(Batch, Channels, H, W)`. Để đưa vào mạng Linear cuối cùng nhằm phân loại, ta phải duỗi phẳng (Flatten) dữ liệu.
Hãy dùng `nn.Flatten()` hoặc `.view()` để duỗi một tensor `torch.randn(32, 16, 8, 8)` thành `(32, 1024)`.

## Tầng 5: Olympiad

Trong thi đấu, bạn KHÔNG BAO GIỜ tự viết Conv2D bằng Numpy (vì cực chậm). Tuy nhiên, bạn phải nắm cực chắc công thức tính Shape để thiết kế mạng không bị lỗi "Shape mismatch" khi nối Conv Layer sang Linear Layer.
