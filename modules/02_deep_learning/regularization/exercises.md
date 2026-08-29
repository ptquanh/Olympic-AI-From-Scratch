# Bài tập: Regularization

## Tầng 1: Understand

**1. BatchNorm giúp ích gì?**
**2. Dropout lúc Predict**
Khi bạn gọi `model.eval()`, cơ chế Dropout có tiếp tục "rơi rụng" nơ-ron nữa không? Nếu không, nó làm gì?

## Tầng 2: Implement

**1. Early Stopping cơ bản**
Viết một đoạn logic đơn giản bên trong Training Loop: Nếu Loss trên tập Validation không giảm sau 5 epoch liên tiếp, hãy in ra chữ "Early Stopped" và dùng lệnh `break` để ngừng vòng lặp huấn luyện.

## Tầng 3: Experiment

**1. L2 Regularization (Weight Decay)**
Huấn luyện 1 mạng MLP đa lớp trên một bộ dữ liệu nhỏ (vd: 50 mẫu). Lần 1: dùng Adam (weight_decay=0). Lần 2: dùng AdamW (weight_decay=0.1). In ra biểu đồ phân phối giá trị của tất cả các trọng số (Weights histogram). Bạn thấy weight decay đã làm gì với các trọng số?
