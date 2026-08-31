# Bài tập: Activation Functions

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Tại sao Sigmoid thường chỉ dùng ở Layer cuối cùng?**
**2. Hạn chế của ReLU**
Tại sao ReLU lại gây ra hiện tượng "Dead Neurons" (Nơ-ron chết)?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Trực quan hóa**
Viết đoạn code dùng Matplotlib để vẽ đồ thị hàm ReLU và hàm Tanh trên khoảng từ -5 đến 5. Vẽ thêm đồ thị đạo hàm của chúng.

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Dead ReLU Problem**
Thử khởi tạo một mạng MLP 5 tầng `Linear(10, 10)` kèm hàm `ReLU()`. Thay vì dùng trọng số mặc định ngẫu nhiên, hãy ép toàn bộ trọng số (weights) của lớp đầu tiên thành số âm (`p.data = torch.ones_like(p) * -1`). Điều gì xảy ra với output và đạo hàm của toàn bộ mạng?

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
