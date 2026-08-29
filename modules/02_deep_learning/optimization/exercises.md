# Bài tập: Optimization

## Tầng 1: Understand

**1. Tại sao Learning Rate (Tốc độ học) lại là tham số quan trọng nhất?**

## Tầng 2: Implement

**1. Cài đặt Adam**
Thay vì dùng SGD như chương trước, hãy sử dụng Adam. Tạo Optimizer. Trực quan hóa giá trị Learning rate của `CosineAnnealingLR` qua 100 epochs bằng Matplotlib (bằng cách lấy `scheduler.get_last_lr()[0]`).

## Tầng 3: Experiment

**1. SGD vs Adam trên hàm Rosenbrock**
Tạo hai biến $x=2.0$ và $y=2.0$ (với `requires_grad=True`). Cố gắng tối thiểu hóa hàm Rosenbrock $f(x, y) = (1-x)^2 + 100(y - x^2)^2$. Thử chạy 1000 bước bằng SGD (lr=0.01) và Adam (lr=0.01). Vẽ quỹ đạo của cả hai. Optimizer nào hội tụ nhanh hơn?
