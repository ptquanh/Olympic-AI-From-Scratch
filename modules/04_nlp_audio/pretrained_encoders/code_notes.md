# Code Notes: Pretrained Encoders

> ⚠️ **Online/optional appendix:** một số snippet bên dưới cần package hoặc model cache bổ sung và có thể tải dữ liệu ở lần chạy đầu. Chúng không competition-safe nếu profile chính thức không cho phép rõ ràng. Notebook chính của chương luôn có đường chạy fast/offline và không tự cài/tải.

## 🔑 Core Patterns

### Pattern 1: Sentence Transformers (Cực mạnh cho Semantic Search)

```python
from sentence_transformers import SentenceTransformer, util

# Tải mô hình
model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = ["The cat plays outside", "A kitten is playing outdoors", "I love playing guitar"]
embeddings = model.encode(sentences)

# Tính cosine similarity giữa câu 0 và câu 1
cos_sim = util.cos_sim(embeddings[0], embeddings[1])
print("Similarity:", cos_sim.item()) # Rất cao vì 2 câu đồng nghĩa

```

### 🏋️ Bài Luyện Code Tay

| #   | Bài                                               | Thời gian | Hint (ẩn)                                           |
| --- | ------------------------------------------------- | --------- | --------------------------------------------------- |
| 1   | Load mô hình BERT và AutoTokenizer từ HuggingFace | 10p       | Dùng `AutoModel.from_pretrained`                    |
| 2   | Trích xuất [CLS] token embedding từ câu đầu vào   | 15p       | Lấy output ở vị trí [:, 0, :] của last_hidden_state |

## 📋 API Cheat Sheet

| API                             | Dùng khi                               |
| ------------------------------- | -------------------------------------- |
| `AutoTokenizer.from_pretrained` | online/cache-prepared learning profile |
| `AutoModel.from_pretrained`     | online/cache-prepared learning profile |
| `local_files_only=True`         | fail safely when offline               |

### 🧠 Flashcards

| Hỏi                                    | Trả lời                                                                           |
| -------------------------------------- | --------------------------------------------------------------------------------- |
| Token [CLS] dùng để làm gì trong BERT? | Chứa thông tin tổng hợp của toàn bộ câu, thường dùng cho bài toán Classification. |
| Tại sao gọi BERT là AutoEncoder Model? | Vì mục tiêu huấn luyện của nó là Masked Language Modeling (đoán từ bị che).       |
