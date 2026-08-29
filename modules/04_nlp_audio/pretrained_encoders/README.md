# Pre-trained Encoders (BERT & Co.)

> **Track:** Foundation ⭐ | Contest ⭐

## ① Giới thiệu

Thay vì huấn luyện Word2Vec cho từng từ, hay huấn luyện Transformer từ đầu (rất tốn kém), ta tải các mô hình khổng lồ (như BERT) đã được huấn luyện đọc hàng tỷ trang Wikipedia.

## ② Learning Outcomes

- Hiểu khái niệm Pre-training và Fine-tuning.
- Khám phá sức mạnh của `sentence-transformers` để nhúng (embed) cả 1 câu dài thành 1 vector duy nhất.
- Ứng dụng ngay lập tức cho Semantic Search (Tìm kiếm theo ngữ nghĩa).

## ③ Concept Map

Transformer ➔ **Pretrained Encoders** ➔ RAG (Retrieval-Augmented Generation).

## ④ Intuition

Từ "Bank" trong "River bank" (bờ sông) và "Bank account" (tài khoản ngân hàng) là 2 nghĩa khác nhau. Word2Vec thất bại vì nó gán cho chữ "Bank" 1 vector duy nhất.
BERT (Encoder của Transformer) đọc CẢ CÂU một lúc (Self-Attention), nên vector của chữ "Bank" phụ thuộc vào các chữ xung quanh nó (Contextualized Embedding).

## ⑤ Math/Derivation

Thay vì lấy vector của 1 từ, ta lấy trung bình cộng (Mean Pooling) vector của tất cả các từ trong câu (sắp xếp bởi BERT) để tạo ra Sentence Embedding.

## ⑥ Worked Example

Tìm kiếm theo ngữ nghĩa:
Câu hỏi: "Tôi bị đau đầu"
Tài liệu 1: "Triệu chứng nhức mỏi hộp sọ..."
Tài liệu 2: "Cửa hàng bán quần áo..."
Bằng cách so sánh Cosine Similarity giữa Sentence Embeddings, hệ thống sẽ biết Tài liệu 1 khớp với Câu hỏi, dù chúng KHÔNG CÓ TỪ NÀO TRÙNG NHAU. (Search truyền thống thất bại vụ này).

## ⑯ Time Estimate

Theory: ~1h, Code: ~1h, Exercises: ~1h
