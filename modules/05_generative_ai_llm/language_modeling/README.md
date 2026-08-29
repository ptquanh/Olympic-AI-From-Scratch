# Language Modeling

> **Thời gian học ước tính:** 3 giờ (theory: 1.5h, code: 0.5h, exercises: 1h)
> **Loại:** Concept Lesson
> **Track:** Foundation ⚡ | Contest 📖

## Prerequisite Check

Trước khi bắt đầu, bạn cần trả lời được:

1. Embedding là gì? Làm sao chuyển một từ thành vector?
2. Softmax function hoạt động như thế nào và dùng để làm gì trong phân loại đa lớp?
3. RNN/Transformer xử lý sequence như thế nào (tổng quan)?

Nếu chưa → quay lại các chương Text Preprocessing, Embeddings, và Transformer (Module 04).

## Learning Outcomes

Sau chương này, bạn sẽ có thể:

- [ ] Phân biệt được Autoregressive (Causal) LM và Masked LM.
- [ ] Tính toán và giải thích được Perplexity (PPL).
- [ ] Viết code sử dụng mô hình LM có sẵn để sinh văn bản (text generation).

## Concept Map

```text
[Embeddings & Transformer] ──→ [LANGUAGE MODELING] ──→ [Fine-tuning Patterns]
                                      │
                                      ├── nền tảng cho [Prompt Engineering]
                                      └── ứng dụng trong [Text Generation]
```

## 1. Intuition — Tại Sao Cần?

Language Model (Mô hình ngôn ngữ) giải quyết bài toán: **Cho một chuỗi từ, xác suất từ tiếp theo xuất hiện là bao nhiêu?**
Thay vì phải code các quy tắc ngữ pháp phức tạp, ta cho mô hình đọc hàng tỷ tài liệu. Mô hình sẽ tự học được cách đoán từ tiếp theo sao cho tự nhiên nhất (như con người nói). Tính năng tự động điền (Autocomplete) trên điện thoại chính là một dạng Language Model.

## 2. Các Loại Language Modeling

### 2.1 Causal (Autoregressive) Language Modeling

- **Mục tiêu:** Dự đoán token tiếp theo dựa trên các token trước đó.
- **Mô hình tiêu biểu:** GPT (Generative Pre-trained Transformer).
- **Ứng dụng:** Chatbot, sinh văn bản, dịch máy (dạng text-to-text).
- **Đặc điểm:** Chỉ nhìn được ngữ cảnh bên trái (Left-to-Right).

### 2.2 Masked Language Modeling (MLM)

- **Mục tiêu:** Dự đoán token bị che khuất ở giữa câu dựa trên ngữ cảnh xung quanh (cả trái và phải).
- **Mô hình tiêu biểu:** BERT, RoBERTa.
- **Ứng dụng:** Trích xuất đặc trưng (embeddings), phân loại văn bản, trích xuất thông tin.
- **Đặc điểm:** Không thích hợp để sinh văn bản dài liên tục.

## 3. Math & Evaluation: Perplexity (PPL)

Language Model tính xác suất của một câu (chuỗi token) $W = (w_1, w_2, ..., w_N)$ bằng quy tắc dây chuyền:
$$ P(W) = \prod*{i=1}^{N} P(w_i | w_1, ..., w*{i-1}) $$

**Perplexity (PPL)** đo lường mức độ "bối rối" của mô hình khi gặp dữ liệu thực tế. PPL càng thấp, mô hình dự đoán càng tốt.
$$ PPL(W) = P(w*1, ..., w_N)^{-\frac{1}{N}} = \exp \left( -\frac{1}{N} \sum*{i=1}^{N} \log P(w*i | w_1, ..., w*{i-1}) \right) $$
Bản chất PPL chính là hàm mũ của **Cross Entropy Loss**.

## 4. Worked Example: Text Generation

Giả sử ta có một mô hình rất nhỏ với từ vựng $V = \{\text{"Tôi", "thích", "học", "AI"}\}$.
Câu đầu vào: `["Tôi", "thích"]`

Mô hình dự đoán xác suất từ tiếp theo:

- $P(\text{"học"} | \text{"Tôi", "thích"}) = 0.7$
- $P(\text{"AI"} | \text{"Tôi", "thích"}) = 0.2$
- $P(\text{"Tôi"} | \text{"Tôi", "thích"}) = 0.05$
- $P(\text{"thích"} | \text{"Tôi", "thích"}) = 0.05$

Tham lam (Greedy Search) sẽ chọn từ có xác suất cao nhất: `"học"`.
Câu mới: `["Tôi", "thích", "học"]`. Lặp lại bước trên để sinh từ tiếp theo.

## 5. Common Mistakes & Misconceptions

> ❌ **Sai:** BERT có thể dùng để làm chatbot trả lời câu hỏi trực tiếp.
> ✅ **Đúng:** BERT là Masked LM, chỉ phù hợp trích xuất đặc trưng (encoder). Chatbot (như ChatGPT) dùng GPT (Causal LM - decoder) để sinh text từng từ một.

> ❌ **Sai:** Loss của Language Model càng về 0 thì mô hình càng thông minh.
> ✅ **Đúng:** Loss về gần 0 có thể do mô hình đã học thuộc lòng (overfit) tập dữ liệu huấn luyện. Khi đo PPL trên tập test, PPL sẽ vọt lên rất cao.
