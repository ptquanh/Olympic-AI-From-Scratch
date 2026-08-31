# Code Notes: PyTorch Fundamentals

## 🔑 Core Patterns

### Pattern 1: Tensor Basics & Device

```python
import torch
import numpy as np

# Tạo tensor
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.randn(3, 4) # Ma trận 3x4 giá trị chuẩn tắc

# Kiểm tra GPU
device = "cuda" if torch.cuda.is_available() else "cpu"

# Chuyển tensor sang GPU
x = x.to(device)

# Chuyển từ PyTorch về NumPy (phải kéo về CPU trước)
x_numpy = x.cpu().numpy()

```

### Pattern 2: DataLoader Pattern

```python
from torch.utils.data import Dataset, DataLoader

# 1. Định nghĩa Dataset custom
class MyDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# 2. Khởi tạo Dataset
dataset = MyDataset(X_data, y_data)

# 3. Đưa vào DataLoader (chia batch, xáo trộn)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

```

## 📋 API Cheat Sheet

| Việc cần làm                | Code                                                  | Link Docs                                                                             |
| --------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Kiểm tra shape              | `tensor.shape` hoặc `tensor.size()`                   | [torch.Tensor.size](https://pytorch.org/docs/stable/generated/torch.Tensor.size.html) |
| Thêm 1 chiều (Unsqueeze)    | `x.unsqueeze(dim=0)` (biến shape (3,) thành (1,3))    | [torch.unsqueeze](https://pytorch.org/docs/stable/generated/torch.unsqueeze.html)     |
| Xóa chiều bằng 1 (Squeeze)  | `x.squeeze()` (biến shape (1, 3, 1) thành (3,))       | [torch.squeeze](https://pytorch.org/docs/stable/generated/torch.squeeze.html)         |
| Đổi thứ tự chiều (Permute)  | `x.permute(2, 0, 1)` (biến ảnh (H,W,C) thành (C,H,W)) | [torch.permute](https://pytorch.org/docs/stable/generated/torch.permute.html)         |
| Đưa list/numpy thành Tensor | `torch.tensor(data)` hoặc `torch.from_numpy(arr)`     | [torch.tensor](https://pytorch.org/docs/stable/generated/torch.tensor.html)           |

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                                                         | Thời gian | Hint (ẩn)                             |
| --- | ------------------------------------------------------------------------------------------- | --------- | ------------------------------------- |
| 1   | Tạo tensor ngẫu nhiên shape (10, 5), in ra shape, và chuyển nó sang GPU nếu có.             | 2 phút    | `torch.randn(10, 5).to(device)`       |
| 2   | Viết class CustomDataset nhận vào mảng X và list nhãn Y. Ghi đè `__len__` và `__getitem__`. | 5 phút    | Nhớ return `self.X[idx], self.y[idx]` |
| 3   | Có 1 tensor shape `(28, 28, 3)`. Dùng lệnh gì để biến nó thành `(3, 28, 28)`?               | 2 phút    | `tensor.permute(2, 0, 1)`             |

## 🧠 Flashcards

| Hỏi                                                                     | Trả lời                                                                                                                    |
| ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Điểm khác biệt lớn nhất giữa `torch.Tensor` và `numpy.ndarray` là gì?   | Tensor có thể được lưu trữ và tính toán trên GPU. Hơn nữa, nó hỗ trợ tự động tính đạo hàm (autograd).                      |
| Tham số `shuffle=True` trong DataLoader có tác dụng gì và khi nào dùng? | Trộn đều dữ liệu mỗi epoch. Rất CẦN THIẾT cho tập Train để tránh mô hình học vẹt theo thứ tự. KHÔNG DÙNG cho tập Test/Val. |
