# Code Notes: Text Preprocessing

> ⚠️ **Online/optional appendix:** một số snippet bên dưới cần package hoặc model cache bổ sung và có thể tải dữ liệu ở lần chạy đầu. Chúng không competition-safe nếu profile chính thức không cho phép rõ ràng. Notebook chính của chương luôn có đường chạy fast/offline và không tự cài/tải.

## 🔑 Core Patterns

### Pattern 1: HuggingFace Tokenizer Cơ Bản

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
text = "Unbelievable! I'm learning AI."

# Cắt từ (Tokenize)
tokens = tokenizer.tokenize(text)
print(tokens) # ['un', '##bel', '##ie', '##vable', '!', 'i', "'", 'm', 'learning', 'ai', '.']

# Chuyển thành IDs
ids = tokenizer.convert_tokens_to_ids(tokens)

# Tự động từ A-Z (Rất hay dùng)
encoded = tokenizer(text, padding="max_length", max_length=15, truncation=True)
print(encoded["input_ids"])
print(encoded["attention_mask"])

```

## 🏋️ Bài Luyện Code Tay

| #   | Bài                                                                                                                             | Thời gian | Hint (ẩn)                                                                   |
| --- | ------------------------------------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------- |
| 1   | Viết lệnh dùng `AutoTokenizer` để tiền xử lý 1 list gồm 2 câu (batch) với padding và truncation tự động. Trả về tensor PyTorch. | 2 phút    | `tokenizer(list_texts, padding=True, truncation=True, return_tensors='pt')` |
| 2   | Loại bỏ URL và Emoji khỏi chuỗi văn bản bằng Regex                                                                              | 10p       | Dùng re.sub() với mẫu regex tương ứng                                       |

## 📋 API Cheat Sheet

| API             | Dùng khi                                        |
| --------------- | ----------------------------------------------- |
| `re.sub`        | deterministic normalization                     |
| `str.split`     | minimal offline tokenization                    |
| `AutoTokenizer` | model-matched tokenizer in online/cache profile |

### 🧠 Flashcards

| Hỏi                                            | Trả lời                                                                                |
| ---------------------------------------------- | -------------------------------------------------------------------------------------- |
| BPE (Byte Pair Encoding) giải quyết vấn đề gì? | Giải quyết vấn đề từ vựng quá lớn (OOV) bằng cách chia từ thành các sub-word phổ biến. |
| Tại sao phải chuẩn hóa Unicode (NFC/NFD)?      | Để đồng nhất các ký tự gõ theo cách khác nhau (VD: òa vs oà) về chung một mã.          |
