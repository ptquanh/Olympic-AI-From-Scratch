# Transformer (Encoder/Decoder)

> **Track:** Foundation ⭐ | Contest ⭐

## ① Prerequisite Check

- Bạn có chắc chắn mình đã hiểu Multi-Head Attention và Causal Masking ở bài trước không?
- Bạn có nhớ Layer Normalization và Residual Connection (Skip-connection) là gì không?

## ② Learning Outcomes

- Hiểu được cấu trúc toàn cảnh của mô hình Transformer (Encoder và Decoder).
- Tự tay code Positional Encoding bằng hàm Sin/Cos để truyền đạt khái niệm về vị trí từ cho mô hình.
- Xây dựng hoàn chỉnh một block Transformer Encoder.
- Hiểu được sự khác biệt giữa Self-Attention và Cross-Attention trong Decoder.

## ③ Concept Map

Attention Mechanism ➔ **Transformer** ➔ Pretrained Encoders (BERT) ➔ Large Language Models (GPT).
Đây là trùm cuối của Deep Learning cổ điển. Bạn đang chạm tay vào kiến trúc đã khai sinh ra ChatGPT.

## ④ Intuition

Mô hình Seq2Seq (như dịch máy) cần 2 phần:

1. **Encoder (Người đọc):** Đọc toàn bộ câu gốc (VD: Tiếng Anh), tìm ra mối liên hệ giữa tất cả các từ trong câu đó bằng Multi-Head Attention, rồi nén lại thành một tập hợp các ma trận đặc trưng sâu sắc nhất.
2. **Decoder (Người viết):** Viết ra từng từ một (VD: Tiếng Việt). Khi viết từ thứ 3, nó phải tự nhìn lại 2 từ trước đó (Self-Attention có Masking để không nhìn trộm tương lai), đồng thời phải "hỏi" Người Đọc (Cross-Attention) xem "Ở bên câu Tiếng Anh, từ nào tương ứng với từ tôi đang định viết?".

## ⑤ Math/Derivation

$$ \text{PositionalEncoding}_{(pos, 2i)} = \sin(pos / 10000^{2i/d_{model}}) $$
$$ \text{PositionalEncoding}_{(pos, 2i+1)} = \cos(pos / 10000^{2i/d_{model}}) $$
Trong đó:

- $pos$: vị trí của từ trong câu (0, 1, 2...).
- $i$: chiều thứ $i$ trong vector nhúng (embedding).
- Sự xen kẽ sin/cos giúp mô hình dễ dàng học được khoảng cách tương đối giữa các từ. Dịch chuyển tuyến tính $pos + k$ có thể được biểu diễn dưới dạng phép quay ma trận tuyến tính.

## ⑥ Worked Example

Lắp ráp 1 Encoder Block:

1. `x = x + SelfAttention(LayerNorm(x))` (Chuẩn hóa $\rightarrow$ Chú ý $\rightarrow$ Cộng Residual).
2. `x = x + FeedForward(LayerNorm(x))` (Chuẩn hóa $\rightarrow$ FFN $\rightarrow$ Cộng Residual).
   _Lưu ý: Original paper dùng Post-LN (Attention xong mới Norm). Nhưng các LLM hiện đại như GPT-3, LLaMA đều dùng Pre-LN (Norm xong mới Attention) vì nó ổn định hơn rất nhiều khi huấn luyện mạng sâu hàng trăm layer._

## ⑩ Misconceptions

❌ **Sai:** Hàm Feed Forward (FFN) trong Transformer chỉ là một lớp Linear bình thường.
✅ **Đúng:** FFN trong Transformer thường phình to ra 4 lần (VD: từ 512 lên 2048) ở hidden layer rồi bóp lại về 512. Đây chính là nơi mô hình "lưu trữ kiến thức" (Memory/Facts), còn Attention là nơi "rút trích ngữ cảnh" (Routing).

## ⑮ Mastery Check

- Nếu thay hàm Sin/Cos bằng một chuỗi số đếm (0, 1, 2, 3...) và đưa vào mạng thì có được không? Tại sao?
- Cross-Attention trong Decoder lấy Query, Key, Value từ đâu?

## ⑯ Time Estimate

Theory: ~3h, Code: ~3h, Exercises: ~2h
