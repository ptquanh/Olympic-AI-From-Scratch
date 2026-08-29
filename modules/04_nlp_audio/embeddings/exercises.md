# Bài tập: Embeddings

## Tầng 1: Understand

**1. Tại sao không dùng One-Hot?**
Nếu từ điển có 50,000 từ. Thay vì dùng `nn.Embedding(50000, 256)`, ta dùng 1 lớp `nn.Linear(50000, 256)` và cho One-hot vector vào có được không? Sự khác biệt là gì?

## Tầng 2: Implement

**1. Cosine Similarity**
Cho 2 vector $A = [1, 2, 3]$ và $B = [1.1, 1.9, 3.2]$. Tính cosine similarity giữa chúng.

## Tầng 3: Experiment

**1. Độ tương đồng của nn.Embedding ngẫu nhiên**
Khởi tạo 1 `nn.Embedding(10, 100)`. Lấy vector của từ 0 và từ 1. Tính cosine similarity. Bạn thấy nó gần 0 hay gần 1? Tại sao?
