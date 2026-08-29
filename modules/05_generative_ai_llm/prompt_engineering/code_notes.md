# Code Notes: Prompt Engineering

## 🔑 Core Patterns

### Pattern 1: Cấu trúc System Prompt + User Prompt (API)

```python
# Mô tả: Cách gọi API tiêu chuẩn cho Chat Model
# Khi nào dùng: Khi muốn LLM tuân thủ chặt chẽ một vai trò
messages = [
    {"role": "system", "content": "Bạn là một trợ lý ảo thông minh. Luôn trả lời ngắn gọn trong 1 câu."},
    {"role": "user", "content": "Thủ đô của Pháp là gì?"}
]
# response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
```

**Ghi nhớ:** Phân tách rõ Ràng giữa `system` (định hướng hành vi) và `user` (yêu cầu cụ thể).

### Pattern 2: Ép kiểu output thành JSON

```python
# Mô tả: Hướng dẫn LLM trả về đúng chuẩn JSON để lập trình xử lý
prompt = '''
Phân loại câu sau: "Sản phẩm này tốt".
Hãy trả về ĐÚNG MỘT JSON object có định dạng:
{"sentiment": "positive" | "negative", "confidence": float}
Không giải thích gì thêm.
'''
```

**Ghi nhớ:** Luôn cung cấp cấu trúc (schema) mẫu và thêm câu thần chú "Không giải thích gì thêm".

## 📋 API Cheat Sheet

| Việc cần làm    | Prompt Mẫu (Tiết kiệm Token)                                            |
| --------------- | ----------------------------------------------------------------------- |
| Fix bug PyTorch | `Fix bug: [Paste error]. Code: [Paste 5 lines]. Only code, no text.`    |
| Viết Regex      | `Write regex for Python to extract emails from text. Just the pattern.` |

## 🏋️ Bài Luyện Code Tay

**Quy tắc:** Đóng tài liệu. Mở notebook trống. Hẹn giờ.

| #   | Bài                                                                        | Thời gian | Hint (ẩn)                               |
| --- | -------------------------------------------------------------------------- | --------- | --------------------------------------- |
| 1   | Viết một few-shot prompt (text) với 3 ví dụ để phân loại tin giả/tin thật. | 5 phút    | Cấu trúc: Text: ... -> Label: Fake/Real |

## 🧠 Flashcards

| Hỏi                                | Trả lời                                                                                    |
| ---------------------------------- | ------------------------------------------------------------------------------------------ |
| In-context learning là gì?         | Khả năng LLM "học" được task ngay từ prompt mà không cần cập nhật trọng số.                |
| Zero-shot khác Few-shot thế nào?   | Zero-shot không đưa ví dụ mẫu. Few-shot đưa 1 vài ví dụ mẫu.                               |
| Tại sao nên dùng Chain of Thought? | Ép LLM suy luận tuần tự, giảm thiểu việc đoán mò và sinh ra kết quả vô lý (hallucination). |
