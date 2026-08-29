# Lời giải: Pretrained Encoders

<details><summary><b>Tầng 1: Understand</b></summary>
BERT được huấn luyện bằng bài toán Masked Language Modeling (MLM). Người ta che đi 15% số từ trong câu (bằng token `[MASK]`) và bắt mô hình phải dự đoán xem từ bị che đi là từ gì, dựa vào văn cảnh xung quanh. Trải qua hàng tỷ câu, mô hình vô tình học được toàn bộ cấu trúc và ý nghĩa của ngôn ngữ.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')
corpus = ["Trời hôm nay rất đẹp", "Tôi muốn ăn phở", "Deep learning là một nhánh của AI"]
query = "Hôm nay ăn gì?"

corpus_emb = model.encode(corpus)
query_emb = model.encode(query)

scores = util.cos_sim(query_emb, corpus_emb)[0]
best_idx = torch.argmax(scores)
print(corpus[best_idx]) # Tôi muốn ăn phở
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>
Các mô hình Multilingual đã liên kết các ngôn ngữ khác nhau vào chung một không gian vector. Nên cosine similarity của "Hello" và "Xin chào" rất lớn (>0.9).
</details>
