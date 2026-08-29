# Text Preprocessing

> **Track:** Foundation ⭐ | Contest 📖

## ① Prerequisite Check

- Bạn có nhớ Regex (biểu thức chính quy) dùng để làm sạch chuỗi không?
- Bạn có hiểu tại sao máy tính không thể đọc trực tiếp các ký tự "A", "B", "C" không?

## ② Learning Outcomes

- Hiểu được vòng đời từ chuỗi văn bản thuần (Raw text) biến thành mảng số nguyên (Input IDs).
- Phân biệt Word-level Tokenization và Subword-level Tokenization (BPE, WordPiece).
- Hiểu tại sao phải Padding (đệm) và Truncation (cắt xén) câu.

## ③ Concept Map

**Text Preprocessing** ➔ Embeddings ➔ Mạng Neural (RNN/Transformer).
Không có bước này, không có mô hình NLP nào có thể chạy được.

## ④ Intuition

Giống như khi dịch mã Morse, chữ cái phải được chuyển thành tín hiệu `.` và `-`. Máy tính chỉ hiểu số (Toán học).
Để máy tính học được ý nghĩa của câu "I love AI", ta phải chia câu thành các mảnh nhỏ (gọi là Token).

- Cắt theo từ: `["I", "love", "AI"]` -> ID: `[10, 52, 99]`
- Cắt theo Subword (từ phụ): `["I", "lo", "##ve", "AI"]` (Giúp đối phó với những từ chưa từng gặp bao giờ).

Vì mỗi câu có độ dài ngắn khác nhau, nhưng ma trận thì phải vuông vức, ta cần chèn thêm số 0 (Padding) cho các câu ngắn, và cắt bớt phần đuôi (Truncation) của các câu dài.

## ⑤ Math/Derivation

$$ \text{Vocabulary Size} = V $$
Mỗi token được ánh xạ thành một số nguyên duy nhất từ $0$ đến $V-1$. Kích thước $V$ càng lớn, mô hình càng nhớ được nhiều từ nhưng lại tốn RAM (vì ma trận nhúng sẽ phình to). Subword Tokenization giúp tối ưu $V$ ở mức 30,000 - 50,000 mà vẫn bao quát toàn bộ ngôn ngữ.

## ⑥ Worked Example

Văn bản: "He is playing"

1. Tokenizer: `["He", "is", "play", "##ing"]`
2. ID mapping: `[45, 12, 109, 32]`
3. Padding (max_len=6): `[45, 12, 109, 32, 0, 0]`
4. Attention Mask: `[1, 1, 1, 1, 0, 0]` (Báo cho mô hình biết số 0 là đồ giả, đừng chú ý).

## ⑩ Misconceptions

❌ **Sai:** Cứ dùng khoảng trắng (Space) để cắt chữ là xong.
✅ **Đúng:** Cắt theo khoảng trắng (Word-level) sẽ tạo ra quá nhiều từ vựng (Out-Of-Vocabulary) như `play`, `playing`, `played`. Subword Tokenization giải quyết triệt để chuyện này bằng cách tách hậu tố `##ing`, `##ed`.

## ⑯ Time Estimate

Theory: ~1h, Code: ~1h, Exercises: ~1h
