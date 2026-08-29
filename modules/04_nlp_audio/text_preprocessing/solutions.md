# Lời giải: Text Preprocessing

<details><summary><b>Tầng 1: Understand</b></summary>
- **Word-level:** Quá nhiều từ vựng (Vocabulary khổng lồ), không xử lý được từ mới (Out Of Vocabulary - OOV), ví dụ model học chữ "chạy" nhưng không biết chữ "chạy_đua" nếu nó viết dính liền (tiếng Đức thường xuyên như vậy).
- **Character-level:** Chuỗi token sinh ra quá dài, mô hình quên mất ngữ cảnh (vì bộ nhớ ngắn), và một chữ cái "c" chả có ý nghĩa ngữ nghĩa gì để model học.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>
```python
from transformers import AutoTokenizer
t1 = AutoTokenizer.from_pretrained("bert-base-uncased")
t2 = AutoTokenizer.from_pretrained("roberta-base")
print(t1.tokenize("unhappiness")) # ['un', '##hap', '##piness'] (WordPiece)
print(t2.tokenize("unhappiness")) # ['un', 'happ', 'iness'] (BPE - Note: Roberta dùng Byte-level BPE nên ký tự có thể khác xíu tuỳ phiên bản)
```
Mỗi model được train trên một thuật toán cắt từ khác nhau, tuyệt đối không dùng tokenizer của model A cho model B.
</details>

<details><summary><b>Tầng 3: Experiment</b></summary>
```python
encoded = tokenizer("Hello world")
print(tokenizer.decode(encoded["input_ids"]))
```
Sẽ in ra `[CLS] hello world [SEP]`.
- `[CLS]` (Classification): Được chèn ở đầu câu. Vector nhúng của nó sau khi đi qua mô hình sẽ được dùng đại diện cho toàn bộ câu (thường dùng cho bài toán phân loại).
- `[SEP]` (Separator): Dùng để ngăn cách nếu có 2 câu (ví dụ bài toán Question Answering: Câu hỏi [SEP] Ngữ cảnh).
</details>
