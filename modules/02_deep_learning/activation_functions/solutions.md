# Lời giải: Activation Functions

<details><summary><b>Tầng 1: Understand</b></summary>
1. Sigmoid bóp dữ liệu về khoảng [0, 1], rất phù hợp để biến đổi output thành xác suất (Probability) trong bài toán phân loại nhị phân. Nếu dùng nó ở các Hidden Layer, nó sẽ gây ra Vanishing Gradient do đạo hàm quá nhỏ.
2. Đạo hàm của ReLU bằng 0 với mọi x < 0. Nếu trong quá trình huấn luyện, trọng số cập nhật khiến đầu vào của ReLU luôn âm, đạo hàm truyền ngược sẽ luôn bằng 0. Trọng số đó vĩnh viễn không bao giờ được cập nhật nữa (Nơ-ron chết).
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
relu = np.maximum(0, x)
relu_grad = (x > 0).astype(int)

tanh = np.tanh(x)
tanh_grad = 1 - tanh**2

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.plot(x, relu, label='ReLU')
ax1.plot(x, relu_grad, label='ReLU Grad', linestyle='--')
ax1.set_title("ReLU")
ax1.legend()

ax2.plot(x, tanh, label='Tanh')
ax2.plot(x, tanh_grad, label='Tanh Grad', linestyle='--')
ax2.set_title("Tanh")
ax2.legend()
plt.show()
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>
Output của lớp đầu tiên luôn bằng 0 (vì Input * Trọng số âm ra kết quả âm, đi qua ReLU biến thành 0). Vì Output bằng 0, đạo hàm của lớp đó cũng bằng 0. Do đó đạo hàm không thể truyền ngược về các lớp trước đó. Cả mạng Neural hoàn toàn tê liệt và Loss không suy suyển một chút nào trong suốt quá trình train.
</details>
