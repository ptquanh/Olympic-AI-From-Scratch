# Olympiad Transfer: Backprop & Training Loop

> **Profile áp dụng:** General, trừ các mục ghi rõ PTIT 2026. Các mốc 4h/6h trong tài liệu này chỉ là timebox của PTIT 2026, không phải luật chung. Đã kiểm chứng 2026-08-31; xem [competition profiles](../../../COMPETITION_PROFILES.md) và ưu tiên thông báo chính thức mới hơn.

## 1. Tầm quan trọng trong thi đấu

Việc hiểu và viết được Training Loop chuẩn xác 100% là KỸ NĂNG BẮT BUỘC. Bạn phải gõ được vòng lặp huấn luyện cơ bản mà không cần nhìn Google. Trong thi đấu, bạn không tự viết `nn.Linear` từ số không (đó là việc của module này), nhưng bạn PHẢI TỰ VIẾT được kiến trúc Custom Network.

## 2. Viết Custom Network Bằng PyTorch

Trong PyTorch, không ai dùng `nn.Sequential` để thi giải, vì nó thiếu tính tùy biến. Tất cả đều phải kế thừa `nn.Module`.

```python
import torch.nn as nn

class MyOlympiadModel(nn.Module):
    def __init__(self):
        super().__init__()
        # Khởi tạo các lớp học tập (có weights) ở đây
        self.fc1 = nn.Linear(300, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 2)

    def forward(self, x):
        # Thiết kế luồng đi của dữ liệu ở đây
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

```

Hàm `forward` chính là trái tim của mô hình, nó thay thế hàm `__call__` mà ta viết bên Micrograd.

## 3. Failure modes

Lỗi hay gặp nhất của người mới học là **Đưa dữ liệu qua hàm mà không lưu kết quả**.
Ví dụ Sai:

```python
def forward(self, x):
    self.fc1(x)
    self.relu(x)
    return self.fc2(x)

```

Mô hình sẽ không thể chạy được, vì dữ liệu đi qua `fc1` bị vứt bỏ, `fc2` vẫn nhận dữ liệu `x` nguyên thủy (chưa xử lý). Phải gán lại: `x = self.fc1(x)`.
