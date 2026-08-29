# Code Notes: Regularization

## 🔑 Core Patterns

```python
import torch.nn as nn

class MyRobustModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(100, 50)
        # 1. BatchNorm đặt NGAY SAU Linear, TRƯỚC Kích hoạt
        self.bn1 = nn.BatchNorm1d(50)
        self.relu = nn.ReLU()
        # 2. Dropout với tỷ lệ loại bỏ 50%
        self.dropout = nn.Dropout(p=0.5)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.dropout(x)
        return self.fc2(x)
```

## 🧠 Flashcards

| Hỏi                                                 | Trả lời                                                                                                                                                                                                                               |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tại sao phải gọi `model.train()` và `model.eval()`? | Lệnh này báo hiệu cho Dropout và BatchNorm biết mô hình đang ở trạng thái nào. Khi `eval()` (Predict/Test), Dropout sẽ ngừng loại bỏ nơ-ron và BatchNorm sử dụng thống kê trung bình cục bộ tĩnh thay vì dựa vào từng batch riêng lẻ. |
| Overfitting là gì? Giải pháp?                       | Là hiện tượng mô hình học VẸT tập Train (điểm cao) nhưng dự đoán trên tập Test thì siêu TỆ. Giải pháp: Dropout, Data Augmentation, Weight Decay, Early Stopping.                                                                      |

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                                                       | Thời gian | Hint (ẩn)                                         |
| --- | ----------------------------------------------------------------------------------------- | --------- | ------------------------------------------------- |
| 1   | Thêm `BatchNorm1d` và `Dropout` vào một mạng MLP.                                         | 2 phút    | Đặt BatchNorm(50) sau Linear(100,50), trước ReLU. |
| 2   | Viết nhanh 2 dòng code chuyển mô hình sang trạng thái Test, dự đoán, rồi chuyển về Train. | 1 phút    | `model.eval()`, `y = model(x)`, `model.train()`   |
