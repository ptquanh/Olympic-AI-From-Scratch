# Code Notes: Loss Functions

## 🔑 Core Patterns

```python
import torch.nn as nn

# 1. Bài toán Hồi quy (Regression - Dự đoán số thực)
criterion = nn.MSELoss()
loss = criterion(y_pred, y_true)

# 2. Bài toán Phân loại Đa lớp (Multi-class Classification)
# LƯU Ý: Không dùng Softmax ở lớp mạng cuối cùng, vì CrossEntropyLoss ĐÃ BAO GỒM Softmax bên trong nó!
criterion = nn.CrossEntropyLoss()
loss = criterion(y_pred_logits, y_class_indices)
```

## 🧠 Flashcards

| Hỏi                                                              | Trả lời                                                                                                                                                                    |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sự khác biệt giữa `NLLLoss` và `CrossEntropyLoss` trong PyTorch? | `NLLLoss` yêu cầu bạn phải áp dụng LogSoftmax ở layer cuối mạng. Còn `CrossEntropyLoss` kết hợp cả LogSoftmax và NLLLoss thành một lệnh duy nhất (nhanh hơn, ổn định hơn). |
| Khi nào nên dùng Focal Loss?                                     | Khi dataset bị mất cân bằng trầm trọng (Class Imbalance). Hàm này ép mô hình tập trung học những mẫu "khó" và bỏ qua những mẫu "dễ".                                       |

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                                                                     | Thời gian | Hint (ẩn)                                                        |
| --- | ------------------------------------------------------------------------------------------------------- | --------- | ---------------------------------------------------------------- |
| 1   | Khởi tạo MSELoss, tính loss cho `y_pred = torch.tensor([0.5, 1.5])` và `y = torch.tensor([1.0, 1.0])`.  | 2 phút    | `criterion = nn.MSELoss(); loss = criterion(y_pred, y)`          |
| 2   | Tính `CrossEntropyLoss` cho `logits = torch.tensor([[2.0, 0.5, 0.1]])` và nhãn `y = torch.tensor([0])`. | 2 phút    | `criterion = nn.CrossEntropyLoss(); loss = criterion(logits, y)` |
