# Code Notes: Convolution

## 🔑 Core Patterns

```python
import torch
import torch.nn as nn

# Định nghĩa 1 lớp Conv2D
# in_channels: Số kênh ảnh đầu vào (Ví dụ: 3 cho RGB)
# out_channels: Số lượng Filter/Kernel muốn tạo ra
# kernel_size: Kích thước kính lúp (vd 3x3)
conv = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)

# Ảnh mô phỏng: Batch=1, Channels=3, H=32, W=32
dummy_image = torch.randn(1, 3, 32, 32)
output = conv(dummy_image)
print(output.shape) # Output: (1, 16, 32, 32) (Do padding=1 nên H,W không đổi)

```

## 📋 API Cheat Sheet

| Việc cần làm | Code                                | Link Docs                                                                      |
| ------------ | ----------------------------------- | ------------------------------------------------------------------------------ |
| Conv2D       | `nn.Conv2d(in, out, kernel_size)`   | [Conv2d](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html)       |
| Max Pooling  | `nn.MaxPool2d(kernel_size, stride)` | [MaxPool2d](https://pytorch.org/docs/stable/generated/torch.nn.MaxPool2d.html) |

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                                   | Thời gian | Hint (ẩn)                                   |
| --- | --------------------------------------------------------------------- | --------- | ------------------------------------------- |
| 1   | Tính số lượng tham số của Conv2D(in=3, out=16, kernel=3x3, bias=True) | 2 phút    | $(3 \times 3 \times 3 + 1) \times 16 = 448$ |
| 2   | Viết code khởi tạo mạng `Conv2d` giảm 1 nửa kích thước ảnh `(H,W)`.   | 2 phút    | `nn.Conv2d(..., stride=2, padding=1)`       |

## 🧠 Flashcards

| Hỏi                    | Trả lời                                                                                                                                                                         |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stride là gì?          | Là "bước nhảy" của Kernel khi trượt trên ảnh. Stride = 2 nghĩa là kernel nhảy cách 2 pixel, khiến ảnh đầu ra bị thu nhỏ đi 1 nửa.                                               |
| Receptive Field là gì? | Là vùng không gian trên ảnh GỐC mà một nơ-ron ở các tầng SÂU có thể "nhìn thấy". Qua nhiều tầng Conv và Pool, 1 nơ-ron bé xíu có thể mang thông tin của cả một mảng ảnh rất to. |
