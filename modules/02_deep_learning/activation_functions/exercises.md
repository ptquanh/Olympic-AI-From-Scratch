# Bài tập: Activation Functions

## Tầng 1: Understand

**1. Tại sao Sigmoid thường chỉ dùng ở Layer cuối cùng?**

## Tầng 2: Implement

**1. Trực quan hóa**
Viết đoạn code dùng Matplotlib để vẽ đồ thị hàm ReLU và hàm Tanh trên khoảng từ -5 đến 5. Vẽ thêm đồ thị đạo hàm của chúng.

## Tầng 3: Experiment

**1. Dead ReLU Problem**
Thử khởi tạo một mạng MLP 5 tầng `Linear(10, 10)` kèm hàm `ReLU()`. Thay vì dùng trọng số mặc định ngẫu nhiên, hãy ép toàn bộ trọng số (weights) của lớp đầu tiên thành số âm (`p.data = torch.ones_like(p) * -1`). Điều gì xảy ra với output và đạo hàm của toàn bộ mạng?
