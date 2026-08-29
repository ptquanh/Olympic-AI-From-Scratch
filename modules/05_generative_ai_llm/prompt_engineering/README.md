# Prompt Engineering

> **Thời gian học ước tính:** 2 giờ (theory: 1h, code: 0h, exercises: 1h)
> **Loại:** Concept Lesson
> **Track:** Foundation 📖 | Contest ⭐

## Prerequisite Check

Trước khi bắt đầu, bạn cần trả lời được:

1. LLM (như GPT-4, Gemini) sinh văn bản theo cơ chế nào?
2. Sự khác biệt giữa pre-training (để có base model) và instruction tuning (để có chat model)?

Nếu chưa → quay lại Language Modeling (Module 05).

## Learning Outcomes

Sau chương này, bạn sẽ có thể:

- [ ] Phân biệt và sử dụng thành thạo Zero-shot, Few-shot, và Chain-of-Thought prompting.
- [ ] Thiết kế prompt tối ưu cho các tác vụ NLP (Phân loại, trích xuất) với giới hạn 2000 tokens/lần gọi.
- [ ] Nắm được chiến thuật dùng LLM làm "trợ lý" viết code / debug trong thi đấu Olympic.

## Concept Map

```text
[Language Modeling] --> [PROMPT ENGINEERING] --> [Multimodal]
                              │
                              └── ứng dụng cực mạnh vào [Competition Pipeline]
```

## 1. Intuition — Tại Sao Cần Prompt Engineering?

Từ năm 2022, thay vì phải tốn hàng giờ viết code để fine-tune mô hình (như BERT) cho một bài toán NLP cụ thể (VD: phân loại tích cực/tiêu cực), ta có thể chỉ cần "ra lệnh" cho một LLM bằng ngôn ngữ tự nhiên: _"Hãy phân loại câu sau thành tích cực hay tiêu cực: [câu cần phân loại]"_.

Tuy nhiên, LLM không có suy nghĩ. Cách bạn đặt câu hỏi (Prompt) quyết định trực tiếp đến chất lượng câu trả lời. Đặc biệt trong các kỳ thi Olympic AI, **bạn được phép dùng LLM** (ChatGPT, Gemini) với tài khoản ban tổ chức cấp (giới hạn 2000 tokens/session). Dùng tốt prompt sẽ giúp bạn viết code nhanh gấp 10 lần.

## 2. Các Kỹ Thuật Prompt Cốt Lõi (In-Context Learning)

### 2.1 Zero-shot Prompting

Chỉ đưa ra mệnh lệnh, không đưa ví dụ.
_Ví dụ:_ "Dịch câu 'Hello world' sang tiếng Việt."

### 2.2 Few-shot Prompting

Đưa ra một vài ví dụ (input-output) để mô hình học theo định dạng (format) và ngữ cảnh. Cực kỳ hiệu quả cho các bài toán đặc thù.
_Ví dụ:_

```text
Tuyệt vời -> Positive
Tệ quá -> Negative
Sản phẩm này tạm được -> Neutral
Màu sắc hơi tối ->
```

### 2.3 Chain-of-Thought (CoT) Prompting

Yêu cầu mô hình suy luận từng bước thay vì trả lời ngay. Giúp tăng độ chính xác trong các bài toán logic, toán học.
_Ví dụ:_ "Hãy suy nghĩ từng bước một trước khi đưa ra câu trả lời." (Let's think step by step).

## 3. Chiến Thuật Dùng LLM Trong Thi Đấu (Giới hạn 2000 tokens)

Trong phòng thi, token rất quý giá. Đừng copy/paste toàn bộ đề thi dài 5 trang vào LLM.

- **Để viết code baseline:** "Viết một PyTorch training loop chuẩn cho bài toán Image Classification, dùng dataset định dạng thư mục. Có tính validation loss."
- **Để debug lỗi:** Copy đúng 5 dòng báo lỗi cuối cùng + 5 dòng code của bạn gây ra lỗi. Không copy toàn bộ notebook!
- **Prompt mẫu siêu ngắn gọn:** "Tôi đang thi Olympic AI. Nhiệm vụ: X. Vấn đề: Y. Viết code giải quyết Y ngắn gọn nhất có thể, không cần giải thích dòng code."

## 4. Common Mistakes & Misconceptions

> ❌ **Sai:** LLM biết tất cả mọi thứ nên cứ hỏi chung chung là được.
> ✅ **Đúng:** Hỏi chung chung ("Làm sao để giải bài này?") sẽ nhận được câu trả lời chung chung (vô dụng). Phải mô tả thật chi tiết bối cảnh: "Tôi có tensor A shape [32, 3, 224, 224]. Tôi muốn..."

> ❌ **Sai:** Càng cho nhiều few-shot examples càng tốt.
> ✅ **Đúng:** Càng nhiều ví dụ, prompt càng dài (tốn token), đôi khi làm nhiễu LLM. Chỉ cần 2-3 ví dụ bao quát các edge cases là đủ.
