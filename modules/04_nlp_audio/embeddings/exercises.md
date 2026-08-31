# Bài tập: Embeddings

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Tại sao không dùng One-Hot?**
Nếu từ điển có 50,000 từ. Thay vì dùng `nn.Embedding(50000, 256)`, ta dùng 1 lớp `nn.Linear(50000, 256)` và cho One-hot vector vào có được không? Sự khác biệt là gì?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Cosine Similarity**
Cho 2 vector $A = [1, 2, 3]$ và $B = [1.1, 1.9, 3.2]$. Tính cosine similarity giữa chúng.

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Độ tương đồng của nn.Embedding ngẫu nhiên**
Khởi tạo 1 `nn.Embedding(10, 100)`. Lấy vector của từ 0 và từ 1. Tính cosine similarity. Bạn thấy nó gần 0 hay gần 1? Tại sao?

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
