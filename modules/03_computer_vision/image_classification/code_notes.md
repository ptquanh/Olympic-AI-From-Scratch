# Code Notes: Competition Pipeline

## 🔑 Core Patterns: Transfer Learning

```python
import torch.nn as nn
import torchvision.models as models

# 1. Tải mô hình đã được huấn luyện trên ImageNet
model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)

# 2. (Tùy chọn) Đóng băng toàn bộ trọng số cũ để không bị phá hỏng
for param in model.parameters():
    param.requires_grad = False

# 3. Sửa lớp cuối (Linear) cho bài toán 2 classes của mình
# ResNet18 có lớp cuối tên là 'fc' (Fully Connected), in_features = 512
model.fc = nn.Linear(512, 2)

```

## 📋 API Cheat Sheet

| Việc cần làm           | Code                                                | Link Docs                                                       |
| ---------------------- | --------------------------------------------------- | --------------------------------------------------------------- |
| torchvision.transforms | `transforms.Compose([transforms.Resize(256), ...])` | [Transforms](https://pytorch.org/vision/stable/transforms.html) |
| PIL Image              | `Image.open("path.jpg").convert('RGB')`             | [Pillow Docs](https://pillow.readthedocs.io/)                   |

## 🏋️ Bài Luyện Code Tay

1. Viết hàm split stratified từ metadata, không đọc test label.
2. Viết kiểm tra submission: đúng cột, đúng số dòng, ID duy nhất.

## 🧠 Flashcards

| Hỏi                                                                              | Trả lời                                                                                                                                                                                                                           |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tại sao tập Validation KHÔNG ĐƯỢC làm Augmentation (ví dụ: xoay ảnh ngẫu nhiên)? | Vì tập Validation dùng để đo lường khả năng thực sự của mô hình trên dữ liệu chuẩn. Nếu xoay ngẫu nhiên, Loss và Accuracy sẽ nhảy lung tung (noisy), khiến bạn không thể biết mô hình đang tiến bộ hay thụt lùi.                  |
| Transfer Learning vs Fine-tuning?                                                | Transfer Learning thường là "đóng băng" phần thân, chỉ train lớp cái đầu (classifier). Fine-tuning là "phá băng" một phần hoặc toàn bộ thân để train lại với Learning Rate rất nhỏ, giúp mô hình thích nghi sâu hơn với data mới. |
