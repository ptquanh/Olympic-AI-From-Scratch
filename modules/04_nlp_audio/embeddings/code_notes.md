# Code Notes: Embeddings

## 🔑 Core Patterns

### Pattern 1: Tầng Embedding của PyTorch

```python
import torch
import torch.nn as nn

# Từ điển có 10,000 từ. Mỗi từ được biểu diễn bằng vector 256 chiều.
embed_layer = nn.Embedding(num_embeddings=10000, embedding_dim=256)

# Giả sử ta có 1 câu gồm 3 từ (IDs: 5, 200, 9999)
input_ids = torch.tensor([[5, 200, 9999]])

# Trích xuất vector nhúng
word_vectors = embed_layer(input_ids)
print(word_vectors.shape) # (1, 3, 256)

```

## 🏋️ Bài Luyện Code Tay

| #   | Bài                                                                       | Thời gian | Hint (ẩn)                                   |
| --- | ------------------------------------------------------------------------- | --------- | ------------------------------------------- |
| 1   | Viết hàm tính Cosine Similarity giữa 2 vector A và B (Pytorch 1D Tensors) | 3 phút    | `(A @ B) / (torch.norm(A) * torch.norm(B))` |

| 2 | Viết code tính TF-IDF thuần bằng numpy | 20p | Count frequency, chia cho document freq |

## 📋 API Cheat Sheet

| API                                     | Dùng khi         |
| --------------------------------------- | ---------------- |
| `torch.nn.Embedding`                    | ID lookup table  |
| `torch.nn.functional.cosine_similarity` | batched cosine   |
| `torch.nn.functional.normalize`         | L2 normalization |

### 🧠 Flashcards

| Hỏi                                      | Trả lời                                                                                                         |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Khác biệt chính giữa TF-IDF và Word2Vec? | TF-IDF dựa trên tần suất từ (thống kê), Word2Vec dựa trên ngữ cảnh xung quanh từ (học từ neural net).           |
| Nhược điểm của Word2Vec là gì?           | Không xử lý được từ chưa từng thấy (OOV) và mỗi từ chỉ có 1 vector cố định dù ngữ nghĩa thay đổi theo ngữ cảnh. |
