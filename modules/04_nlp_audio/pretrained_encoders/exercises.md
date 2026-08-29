# Bài tập: Pre-trained Encoders

## Tầng 1: Understand

**1. Masked Language Modeling**
BERT được "pre-train" bằng cách nào để có thể hiểu được ngữ pháp ngôn ngữ? (Gợi ý: Trò chơi điền vào chỗ trống).

## Tầng 2: Implement

**1. Semantic Search đơn giản**
Dùng thư viện `sentence-transformers`, tạo 1 mảng 3 tài liệu (corpus). Đưa vào 1 câu truy vấn (query). Tính toán vector, tính `util.cos_sim(query_emb, corpus_emb)` và in ra tài liệu có điểm cao nhất.

## Tầng 3: Experiment

**1. Đa ngôn ngữ**
Thử mô hình `paraphrase-multilingual-MiniLM-L12-v2`. So sánh vector của câu "Hello" và câu "Xin chào".
