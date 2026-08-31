# Bài tập: Regularization

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. BatchNorm giúp ích gì?**
**2. Dropout lúc Predict**
Khi bạn gọi `model.eval()`, cơ chế Dropout có tiếp tục "rơi rụng" nơ-ron nữa không? Nếu không, nó làm gì?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Early Stopping cơ bản**
Viết một đoạn logic đơn giản bên trong Training Loop: Nếu Loss trên tập Validation không giảm sau 5 epoch liên tiếp, hãy in ra chữ "Early Stopped" và dùng lệnh `break` để ngừng vòng lặp huấn luyện.

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. L2 Regularization (Weight Decay)**
Huấn luyện 1 mạng MLP đa lớp trên một bộ dữ liệu nhỏ (vd: 50 mẫu). Lần 1: dùng Adam (weight_decay=0). Lần 2: dùng AdamW (weight_decay=0.1). In ra biểu đồ phân phối giá trị của tất cả các trọng số (Weights histogram). Bạn thấy weight decay đã làm gì với các trọng số?

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
