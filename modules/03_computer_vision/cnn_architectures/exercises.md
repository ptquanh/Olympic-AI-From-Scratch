# Bài tập: CNN Architectures

## Tầng 1: Understand

**1. Câu hỏi lý thuyết**
Skip Connection (Residual Connection) của ResNet giúp giải quyết hiện tượng gì?

## Tầng 2: Implement

**1. Thực hành code**
Tải ResNet18 từ `torchvision`, đóng băng toàn bộ trọng số, và thay lớp `.fc` cuối cùng thành 5 classes.

## Tầng 3: Experiment

**1. Khảo sát kiến trúc MobileNet**
MobileNet là một họ mạng CNN chuyên dùng cho điện thoại di động vì tốc độ rất nhanh.
Hãy dùng `torchvision.models.mobilenet_v2()` để tạo model. In ra tổng số lượng tham số (parameters) của model này và so sánh với ResNet18 (ResNet18 có khoảng 11 triệu tham số).
