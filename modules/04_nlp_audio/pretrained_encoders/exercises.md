# Bài tập: Pre-trained Encoders

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Masked Language Modeling**
BERT được "pre-train" bằng cách nào để có thể hiểu được ngữ pháp ngôn ngữ? (Gợi ý: Trò chơi điền vào chỗ trống).

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Semantic Search đơn giản**
Dùng thư viện `sentence-transformers`, tạo 1 mảng 3 tài liệu (corpus). Đưa vào 1 câu truy vấn (query). Tính toán vector, tính `util.cos_sim(query_emb, corpus_emb)` và in ra tài liệu có điểm cao nhất.

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Đa ngôn ngữ**
Thử mô hình `paraphrase-multilingual-MiniLM-L12-v2`. So sánh vector của câu "Hello" và câu "Xin chào".

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
