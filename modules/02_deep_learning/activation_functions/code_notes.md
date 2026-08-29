# Code Notes: Activation Functions

## 🔑 Core Patterns

```python
import torch
import torch.nn as nn

# Sử dụng Kích hoạt như một Layer (Thường dùng trong nn.Sequential)
model = nn.Sequential(
    nn.Linear(10, 5),
    nn.ReLU(),
    nn.Linear(5, 1)
)

# Sử dụng Kích hoạt như một Hàm (Thường dùng trong class kế thừa nn.Module)
import torch.nn.functional as F

class MyModel(nn.Module):
    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)  # Hoặc torch.relu(x)
        return self.fc2(x)
```

## 📋 API Cheat Sheet

| Việc cần làm     | Code                                   | Link Docs                                                                  |
| ---------------- | -------------------------------------- | -------------------------------------------------------------------------- |
| ReLU             | `nn.ReLU()` hoặc `F.relu()`            | [ReLU](https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html)       |
| Sigmoid          | `nn.Sigmoid()` hoặc `torch.sigmoid()`  | [Sigmoid](https://pytorch.org/docs/stable/generated/torch.nn.Sigmoid.html) |
| Tanh             | `nn.Tanh()` hoặc `torch.tanh()`        | [Tanh](https://pytorch.org/docs/stable/generated/torch.nn.Tanh.html)       |
| GELU             | `nn.GELU()` hoặc `F.gelu()`            | [GELU](https://pytorch.org/docs/stable/generated/torch.nn.GELU.html)       |
| Softmax (Đầu ra) | `nn.Softmax(dim=1)` hoặc `F.softmax()` | [Softmax](https://pytorch.org/docs/stable/generated/torch.nn.Softmax.html) |

## 🧠 Flashcards

| Hỏi                                                   | Trả lời                                                                                                                                       |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Điểm yếu lớn nhất của Sigmoid là gì?                  | Vấn đề Vanishing Gradient (Triệt tiêu đạo hàm). Đạo hàm tối đa chỉ là 0.25, đi qua nhiều tầng mạng thì gradient sẽ về 0 khiến mạng ngừng học. |
| Tại sao Transformer (LLM) lại dùng GELU thay vì ReLU? | GELU mượt mà hơn ở điểm 0 (không bị gập khúc sắc nét như ReLU), giúp luồng gradient truyền đi ổn định hơn và tránh được hiện tượng Dead ReLU. |

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                                             | Thời gian | Hint (ẩn)                                                     |
| --- | ------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------- |
| 1   | Khai báo một chuỗi `nn.Sequential` gồm 3 layer: Linear(10,5), ReLU, Linear(5,1) | 1 phút    | `nn.Sequential(nn.Linear(10, 5), nn.ReLU(), nn.Linear(5, 1))` |
| 2   | Chạy biến `x = torch.tensor([-2.0, 3.0])` qua hàm `F.gelu()`.                   | 1 phút    | `import torch.nn.functional as F; F.gelu(x)`                  |
