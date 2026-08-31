# Lời giải: Activation Functions

<details><summary><b>U-1 — Understand</b></summary>
1. Sigmoid bóp dữ liệu về khoảng [0, 1], rất phù hợp để biến đổi output thành xác suất (Probability) trong bài toán phân loại nhị phân. Nếu dùng nó ở các Hidden Layer, nó sẽ gây ra Vanishing Gradient do đạo hàm quá nhỏ.
2. Đạo hàm ReLU bằng 0 khi pre-activation âm. Nếu một neuron nhận pre-activation âm cho mọi mẫu trong thời gian dài, nhánh qua ReLU không truyền gradient; tuy vậy bias/đường truyền khác hoặc batch tương lai có thể thay đổi trạng thái, nên cần đo activation/gradient trước khi kết luận neuron “chết”.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

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

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>
Chỉ khi **pre-activation** của lớp đầu âm cho toàn bộ mẫu thì ReLU trả 0 và gradient qua nhánh đó bằng 0. Dấu của trọng số âm một mình chưa đủ kết luận vì input/bias có thể âm hoặc dương. Hãy in tỷ lệ activation bằng 0 và gradient norm trên batch kiểm thử.

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>
