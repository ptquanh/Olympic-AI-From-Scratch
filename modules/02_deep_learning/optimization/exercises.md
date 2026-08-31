# Bài tập: Optimization

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Tại sao Learning Rate (Tốc độ học) lại là tham số quan trọng nhất?**

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Cài đặt Adam**
Thay vì dùng SGD như chương trước, hãy sử dụng Adam. Tạo Optimizer. Trực quan hóa giá trị Learning rate của `CosineAnnealingLR` qua 100 epochs bằng Matplotlib (bằng cách lấy `scheduler.get_last_lr()[0]`).

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. SGD vs Adam trên hàm Rosenbrock**
Tạo hai biến $x=2.0$ và $y=2.0$ (với `requires_grad=True`). Cố gắng tối thiểu hóa hàm Rosenbrock $f(x, y) = (1-x)^2 + 100(y - x^2)^2$. Thử chạy 1000 bước bằng SGD (lr=0.01) và Adam (lr=0.01). Vẽ quỹ đạo của cả hai. Optimizer nào hội tụ nhanh hơn?

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
