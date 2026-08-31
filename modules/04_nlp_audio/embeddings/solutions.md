# Lời giải: Embeddings

<details><summary><b>U-1 — Understand</b></summary>
Về mặt Toán học, đưa One-hot vector kích thước 50,000 vào `nn.Linear(50000, 256)` (tức là nhân ma trận $[1 \times 50000] \cdot [50000 \times 256]$) SẼ CHO RA KẾT QUẢ Y HỆT như việc "bốc" hàng thứ $i$ trong `nn.Embedding(50000, 256)`. Tuy nhiên, về mặt Máy tính (Computer Science), nhân ma trận khổng lồ chứa 49,999 số 0 là vô cùng tốn CPU/GPU và RAM. `nn.Embedding` đơn giản chỉ là Lookup Table (trỏ tới ô nhớ và lấy ra) nên cực kỳ nhanh.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>
(1*1.1 + 2*1.9 + 3*3.2) / (sqrt(14) * sqrt(15.06)) = 14.5 / (3.74 * 3.88) = 0.999. Rất gần 1.

```python
import numpy as np
a = np.array([1.0, 2.0, 3.0])
b = np.array([1.1, 1.9, 3.2])
cosine = a @ b / (np.linalg.norm(a) * np.linalg.norm(b))
assert 0.99 < cosine <= 1.0

```

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>
Với hai vector Gaussian độc lập và được chuẩn hóa, cosine có kỳ vọng 0 và độ lệch chuẩn xấp xỉ `1/sqrt(d)`, khoảng 0.1 khi `d=100`. Một lần khởi tạo cụ thể không bắt buộc bằng 0; hãy lặp nhiều seed và báo mean/std trước khi kết luận.

```python
import numpy as np
values = []
for seed in range(200):
    rng = np.random.default_rng(seed)
    a, b = rng.normal(size=(2, 100))
    values.append(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))
assert abs(np.mean(values)) < 0.03
assert 0.06 < np.std(values) < 0.14

```

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>
