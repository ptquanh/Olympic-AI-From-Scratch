# Lời giải: Math Essentials

<details><summary><b>Tầng 1: Understand</b></summary>

**1. Phân biệt Phép Nhân**

- `A * B`: Phép nhân từng phần tử (Element-wise multiplication). Nó lấy phần tử ở hàng $i$ cột $j$ của ma trận $A$ nhân tương ứng với phần tử ở hàng $i$ cột $j$ của ma trận $B$. Trả về ma trận $3 \times 3$.
- `A @ B` (hoặc `np.dot(A, B)`): Phép nhân ma trận tiêu chuẩn (Matrix multiplication). Nó tuân theo quy tắc "Lấy hàng của A nhân vô hướng (dot product) với cột của B".

**2. Trực giác Gradient**

- Hướng `[2.5, -1.2]` là hướng đi **lên núi (dốc nhất)**. (Vì tính chất cốt lõi của Gradient là luôn chỉ theo hướng làm hàm số tăng nhanh nhất).
- Để xuống núi (tìm cực tiểu), bạn phải bước đi theo **hướng ngược lại** của vector Gradient, tức là `[-2.5, 1.2]`. Đây chính là nguyên lý của thuật toán Gradient Descent.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

**1. Softmax Function (Toán + Code)**

```python
import numpy as np

z = np.array([2.0, 1.0, 0.1])

# 1. Tính e^z cho từng phần tử
exp_z = np.exp(z)

# 2. Tính tổng các phần tử e^z
sum_exp_z = np.sum(exp_z)

# 3. Chia từng phần tử cho tổng
softmax_z = exp_z / sum_exp_z

print(softmax_z)
# Kết quả: [0.65900114 0.24243297 0.09856589]
# Tổng luôn luôn bằng 1
```

**2. Manual Matrix Multiplication**

- **Tính nhẩm bằng tay:**
  Dòng 1: $1 \times 5 + 2 \times 6 = 5 + 12 = 17$
  Dòng 2: $3 \times 5 + 4 \times 6 = 15 + 24 = 39$
  Kết quả $C = \begin{bmatrix} 17 \\ 39 \end{bmatrix}$ (kích thước $2 \times 1$)

- **Code kiểm chứng:**

```python
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [5],
    [6]
])

C = A @ B  # hoặc np.dot(A, B)
print(C)
# [[17]
#  [39]]
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

**Gradient Checking bằng Xấp Xỉ Số (Numeric Approximation)**

**1. Tính tay đạo hàm giải tích:**
Hàm số: $f(x) = x^3 - 2x^2 + x$
Đạo hàm: $f'(x) = 3x^2 - 4x + 1$

**2. Tính giá trị chính xác tại x = 2:**
$f'(2) = 3(2)^2 - 4(2) + 1 = 12 - 8 + 1 = 5$

**3. & 4. Xấp xỉ đạo hàm bằng code và so sánh sai số:**

```python
def f(x):
    return x**3 - 2 * x**2 + x

x = 2.0
h = 0.0001

# Áp dụng công thức Central Difference
numeric_grad = (f(x + h) - f(x - h)) / (2 * h)

analytic_grad = 5.0
error = abs(numeric_grad - analytic_grad)

print(f"Đạo hàm giải tích (chính xác): {analytic_grad}")
print(f"Đạo hàm xấp xỉ (Numeric):     {numeric_grad}")
print(f"Sai số: {error:.10f}")
# Output:
# Đạo hàm giải tích (chính xác): 5.0
# Đạo hàm xấp xỉ (Numeric):     5.00000001000072
# Sai số: 0.0000000100
```

Sai số vô cùng nhỏ ($10^{-8}$), cho thấy công thức xấp xỉ hoạt động cực kỳ chính xác. Trong thực tế, các framework như PyTorch vẫn thường dùng phương pháp này để Unit Test cho các hàm tính Gradient nội bộ của nó (gọi là kĩ thuật Gradient Checking).

</details>
