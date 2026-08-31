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
- [ ] Thiết kế prompt có hợp đồng đầu ra, ví dụ kiểm thử và ngân sách ngữ cảnh rõ ràng.
- [ ] Kiểm tra quyền dùng LLM theo đúng kỳ thi, năm và giai đoạn trước khi áp dụng chiến thuật hỗ trợ code/debug.

## Concept Map

```text
[Language Modeling] --> [PROMPT ENGINEERING] --> [Finetuning Patterns]
                              │
                              └── ứng dụng cực mạnh vào [Competition Pipeline]

```

## 1. Intuition — Tại Sao Cần Prompt Engineering?

Từ năm 2022, thay vì phải tốn hàng giờ viết code để fine-tune mô hình (như BERT) cho một bài toán NLP cụ thể (VD: phân loại tích cực/tiêu cực), ta có thể chỉ cần "ra lệnh" cho một LLM bằng ngôn ngữ tự nhiên: _"Hãy phân loại câu sau thành tích cực hay tiêu cực: [câu cần phân loại]"_.

LLM dự đoán token tiếp theo và có thể tạo câu trả lời sai nhưng nghe hợp lý. Prompt tốt giúp mô tả nhiệm vụ, dữ liệu, ràng buộc và định dạng đầu ra; nó không thay thế kiểm thử. Trong thi đấu, **không mặc định LLM được phép dùng**: quyền truy cập, công cụ, thời điểm và ngân sách phụ thuộc từng competition profile.

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

## 3. Chiến thuật chung và giới hạn theo profile

Các kỹ thuật dưới đây chỉ dùng khi quy chế hiện hành cho phép. Không gửi dữ liệu thi, khóa API hoặc thông tin cá nhân vào dịch vụ ngoài phạm vi Ban tổ chức phê duyệt.

- **Để viết code baseline:** "Viết một PyTorch training loop chuẩn cho bài toán Image Classification, dùng dataset định dạng thư mục. Có tính validation loss."
- **Để debug lỗi:** Copy đúng 5 dòng báo lỗi cuối cùng + 5 dòng code của bạn gây ra lỗi. Không copy toàn bộ notebook!
- **Prompt mẫu siêu ngắn gọn:** "Tôi đang thi Olympic AI. Nhiệm vụ: X. Vấn đề: Y. Viết code giải quyết Y ngắn gọn nhất có thể, không cần giải thích dòng code."

### Hồ sơ PTIT 2026 — kiểm chứng 2026-08-31

Nguồn chính thức PTIT công bố LLM chỉ được dùng trong giai đoạn đầu của mỗi vòng, trong môi trường kiểm soát, giới hạn 2.000 token cho mỗi phiên chat. Đây là **luật PTIT 2026**, không áp sang OlpAI, VOAI hay IOAI. Lịch và thể lệ có thể được điều chỉnh; phải đọc thông báo mới nhất trước ngày thi.

- [Mô tả môi trường và giới hạn LLM PTIT 2026](https://ai.ptit.edu.vn/olympic-ai-ptit-2026-dong-cong-dang-ky-cac-doi-buoc-vao-giai-doan-chuan-bi-cho-vong-so-loai/)
- [Thông báo điều chỉnh lịch PTIT 2026](https://ai.ptit.edu.vn/thong-bao-dieu-chinh-lich-thi-olympic-ai-ptit-2026/)

### VOAI 2026 và IOAI 2026

Không tái sử dụng giới hạn PTIT. Với VOAI, kiểm tra thông báo chính thức của mùa 2026; với IOAI, kiểm tra contest rules đúng năm. Nếu quy chế không cho phép hoặc không nói rõ, coi LLM là không competition-safe.

## 4. Common Mistakes & Misconceptions

> ❌ **Sai:** LLM biết tất cả mọi thứ nên cứ hỏi chung chung là được.
> ✅ **Đúng:** Hỏi chung chung ("Làm sao để giải bài này?") sẽ nhận được câu trả lời chung chung (vô dụng). Phải mô tả thật chi tiết bối cảnh: "Tôi có tensor A shape [32, 3, 224, 224]. Tôi muốn..."

> ❌ **Sai:** Càng cho nhiều few-shot examples càng tốt.
> ✅ **Đúng:** Càng nhiều ví dụ, prompt càng dài (tốn token), đôi khi làm nhiễu LLM. Chỉ cần 2-3 ví dụ bao quát các edge cases là đủ.

## ⑯ Time Estimate

Theory: ~1h · Practice: ~1.5h · Exercises: ~1h
