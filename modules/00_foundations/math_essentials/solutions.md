# Lời giải: Math Essentials

<details><summary><b>Tầng 1: Understand</b></summary>

Đạo hàm riêng biểu thị độ dốc (sự thay đổi) của hàm số khi chỉ xét sự thay đổi của MỘT BIẾN DUY NHẤT (giữ các biến khác không đổi). Trong AI, ta dùng đạo hàm riêng để tính xem mỗi trọng số $W_i$ đóng góp bao nhiêu vào việc làm sai số tăng lên/giảm xuống.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
import numpy as np
X = np.random.randn(10, 5) # 10 mẫu, 5 đặc trưng
W = np.random.randn(5)     # 5 trọng số
b = 1.5

y_pred = X @ W + b
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

Softmax function.

```python
def softmax(z):
    exp_z = np.exp(z)
    return exp_z / np.sum(exp_z)
```

</details>
