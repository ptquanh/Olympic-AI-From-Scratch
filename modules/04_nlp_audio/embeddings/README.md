# Embeddings (Biểu diễn từ)

> **Track:** Foundation ⭐ | Contest 📖

## ① Prerequisite Check

- Bạn có hiểu khái niệm Vector trong không gian N chiều không?

## ② Learning Outcomes

- Hiểu ý tưởng chuyển 1 từ (một ID nguyên đơn) thành 1 vector chứa nhiều số thực (Dense vector).
- Đoán nhận ý nghĩa ngữ nghĩa của từ thông qua khoảng cách Cosine Similarity.
- Nắm được khái niệm Word2Vec.

## ③ Concept Map

Text Preprocessing ➔ **Embeddings** ➔ Mạng Neural (RNN/Transformer).

## ④ Intuition

Nếu ta dùng One-hot encoding (ví dụ "Chó" là `[1, 0, 0]`, "Mèo" là `[0, 1, 0]`), khoảng cách giữa mọi từ đều bằng nhau. Máy tính không biết "Chó" và "Mèo" là động vật, còn "Bàn" là đồ vật.
Dense Embedding gán cho "Chó" một vector `[0.9, -0.3, 0.2]` và "Mèo" là `[0.8, -0.2, 0.1]`. Các số thực này mã hóa các thuộc tính (động vật, lắm lông, 4 chân...). Nhờ vậy, "Chó" và "Mèo" sẽ nằm rất gần nhau trong không gian.

## ⑤ Math/Derivation

$$ \text{Cosine Similarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|} $$
Đo độ tương đồng bằng góc giữa 2 vector. Bằng 1 là y hệt nhau, 0 là không liên quan, -1 là trái nghĩa.

## ⑥ Worked Example

Công thức huyền thoại của Word2Vec:

`King - Man + Woman = Queen`
Toán học trên vector đã phản ánh được giới tính và tước vị!

## ⑩ Misconceptions

❌ **Sai:** Ma trận nhúng (Embedding matrix) là thứ gì đó siêu phức tạp và cố định.
✅ **Đúng:** Trong PyTorch, `nn.Embedding(vocab_size, embed_dim)` đơn thuần chỉ là một Lookup Table (bảng tra cứu). Nó chứa các biến số (weights) có thể học được và cập nhật liên tục qua Backpropagation giống y hệt như weights của lớp Linear.

## ⑯ Time Estimate

Theory: ~1h, Code: ~1h, Exercises: ~1h
