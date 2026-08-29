# Lời giải: Language Modeling

<details><summary><b>Tầng 1: Understand</b></summary>

1. Greedy Search luôn chọn từ có xác suất cao nhất. Trong trường hợp này là từ "đẹp" (0.8).
2. BERT là mô hình Encoder-only, được huấn luyện để điền từ vào chỗ trống (Masked Language Modeling) dựa trên ngữ cảnh cả hai phía, không phải để sinh từ tiếp theo (Causal Language Modeling). Do đó, nó không phù hợp để sinh đoạn văn bản dài.
3. Perplexity = $e^{Loss}$. Nếu Loss = 2.5 thì Perplexity xấp xỉ $e^{2.5} \approx 12.18$.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

1. Tham khảo trong lab.ipynb. Code mẫu:

```python
from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")
print(generator("The future of AI is", max_new_tokens=20)[0]['generated_text'])
```

2. Temperature = 0.1: Văn bản sinh ra rất lặp đi lặp lại và an toàn. Temperature = 2.0: Văn bản sinh ra rất hỗn loạn, nhiều từ vô nghĩa hoặc sai ngữ pháp.

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

1. `TinyLlama` sinh ra văn bản tự nhiên hơn và có tính logic tốt hơn `gpt2` do được huấn luyện trên lượng dữ liệu lớn hơn và sử dụng kiến trúc hiện đại hơn (Llama), dù số lượng tham số không quá khác biệt.
2. `top_k=50` sẽ giới hạn mô hình chỉ được chọn từ trong 50 từ có xác suất cao nhất, giúp ngăn chặn việc mô hình chọn các từ quá phi lý khi dùng `temperature=0.7`. Điều này giúp văn bản sinh ra vừa có tính sáng tạo (nhờ temp > 0) vừa không bị "ảo giác" nặng.

</details>
