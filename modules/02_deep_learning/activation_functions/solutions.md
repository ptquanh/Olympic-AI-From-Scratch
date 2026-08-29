# Lời giải: Activation Functions

<details><summary><b>Tầng 1: Understand</b></summary>
Sigmoid bóp dữ liệu về khoảng [0, 1], rất phù hợp để biến đổi output thành xác suất (Probability) trong bài toán phân loại nhị phân. Nếu dùng nó ở các Hidden Layer, nó sẽ gây ra Vanishing Gradient do đạo hàm quá nhỏ.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

# ReLU và Đạo hàm
relu = np.maximum(0, x)
relu_grad = np.where(x > 0, 1, 0)

# Tanh và Đạo hàm
tanh = np.tanh(x)
tanh_grad = 1 - tanh**2

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(x, relu, label="ReLU")
axs[0].plot(x, relu_grad, label="ReLU Derivative", linestyle="--")
axs[0].set_title("ReLU")
axs[0].legend()

axs[1].plot(x, tanh, label="Tanh")
axs[1].plot(x, tanh_grad, label="Tanh Derivative", linestyle="--")
axs[1].set_title("Tanh")
axs[1].legend()

plt.show()
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

Vì toàn bộ input weights đã bị ép thành âm, khi nhân với input dương (giả sử dữ liệu chuẩn hóa từ 0-1), kết quả phép nhân (tổng tích) sẽ luôn là số âm.
Khi giá trị âm đi qua `ReLU()`, nó bị ép thành số `0`.
Hệ quả:

1. Toàn bộ mạng từ tầng 2 trở đi chỉ nhận được toàn số 0.
2. Khi thực hiện `backward()`, đạo hàm của ReLU tại `x <= 0` bằng `0`. Toàn bộ gradient truyền ngược về lớp đầu tiên sẽ bằng `0`. Trọng số không bao giờ được cập nhật nữa $\\rightarrow$ **Mạng đã bị Dead ReLU hoàn toàn ngay từ epoch đầu tiên**.
</details>
