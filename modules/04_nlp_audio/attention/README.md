# Attention Mechanism

> **Track:** Foundation ⭐ | Contest ⭐

## ① Prerequisite Check

- Bạn có hiểu cơ bản về nhân ma trận (Matrix Multiplication) trong PyTorch không?
- Bạn có nhớ hàm Softmax dùng để biến đổi mảng số thành phân bố xác suất có tổng bằng 1 không?

## ② Learning Outcomes

- Hiểu được ý tưởng "truy vấn" (Query, Key, Value) bắt nguồn từ cơ sở dữ liệu.
- Tự tay cài đặt `Scaled Dot-Product Attention` từ Numpy/PyTorch thuần.
- Mở rộng lên thành `Multi-Head Attention`.
- Nắm vững các bước biến đổi hình dạng (shape) của tensor xuyên suốt quá trình.

## ③ Concept Map

Biểu diễn từ (Embeddings) ➔ **Attention Mechanism** ➔ Transformer ➔ LLM (GPT, BERT).
Attention là trái tim của mọi mô hình AI hiện đại nhất hiện nay.

## ④ Intuition

Nếu bạn vào thư viện tìm sách:

- **Query (Q):** Điều bạn muốn tìm (VD: "Sách nấu ăn").
- **Key (K):** Tiêu đề/thể loại của từng cuốn sách trên giá.
- **Value (V):** Nội dung thực sự của cuốn sách đó.

Bạn sẽ so sánh độ khớp giữa `Query` của bạn và các `Key`. Cuốn nào khớp nhất sẽ có trọng số cao nhất. Cuối cùng bạn đọc nội dung `Value` của những cuốn có trọng số cao đó. Self-Attention áp dụng y hệt tư duy này: mỗi từ trong câu đóng vai trò Q để "hỏi" tất cả các từ khác (bao gồm chính nó) xem nó nên "chú ý" vào từ nào nhất để hiểu đúng ngữ cảnh.

## ⑤ Math/Derivation

$$ \text{Attention}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V $$
Trong đó:

- $Q, K, V$ là các ma trận đặc trưng của chuỗi đầu vào.
- Tích vô hướng $Q K^T$ đo lường độ tương đồng (chú ý) giữa các từ.
- Chia cho $\sqrt{d_k}$ (Scaled) để tránh việc tích vô hướng quá lớn khiến Gradient của Softmax bị triệt tiêu (Vanishing Gradient).
- $\text{softmax}$ chuyển đổi điểm số thành trọng số từ $0$ đến $1$ (tổng bằng $1$).
- Cuối cùng nhân với $V$ để lấy ra thông tin thực sự cần thiết.

## ⑥ Worked Example

Giả sử ta có câu "Ngân hàng", gồm 2 từ. Q, K, V là các ma trận 2x3.
$Q = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix}$, $K = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix}$, $V = \begin{bmatrix} 10 & 20 \\ 30 & 40 \end{bmatrix}$

1. $QK^T$: $\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$
2. Chia scale (giả sử bỏ qua) và Softmax theo hàng:
   $\begin{bmatrix} 0.73 & 0.27 \\ 0.27 & 0.73 \end{bmatrix}$
3. Nhân $V$:
   $\begin{bmatrix} 0.73 \cdot 10 + 0.27 \cdot 30 & ... \\ ... & ... \end{bmatrix} = \begin{bmatrix} 15.4 & 25.4 \\ 24.6 & 34.6 \end{bmatrix}$

## ⑩ Misconceptions

❌ **Sai:** Attention tự động hiểu được thứ tự của các từ trong câu.
✅ **Đúng:** Attention KHÔNG HỀ có khái niệm về thứ tự. Câu "A đánh B" và "B đánh A" sẽ ra cùng một tập hợp tập hợp trọng số chú ý nếu không có Positional Encoding (học ở chương sau). Bản chất nó chỉ là phép toán trên tập hợp (Set).

## ⑮ Mastery Check

- Tại sao phải chia cho $\sqrt{d_k}$?
- Multi-Head Attention có gì tốt hơn Single-Head Attention?
- Sự khác biệt giữa `q.view(...)` và `q.reshape(...)` hoặc `q.transpose(...)` trong thao tác chia Head là gì?

## ⑯ Time Estimate

Theory: ~2h, Code: ~3h, Exercises: ~2h
