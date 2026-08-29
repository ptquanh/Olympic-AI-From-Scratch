# Code Notes: Math Essentials

## 🔑 Core Patterns (Phải nhớ)

### Pattern 1: Dot Product & Matrix Multiplication

```python
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
dot_prod = np.dot(a, b) # 1*4 + 2*5 + 3*6 = 32

A = np.random.rand(4, 3)
B = np.random.rand(3, 2)
C = A @ B # Nhân ma trận (Matrix Multiplication). Shape: (4, 2)
```

**Ghi nhớ:** Dùng `@` cho Matrix Multiplication. Bắt buộc chiều kích thước giữa $(M, N) \times (N, K)$.

### Pattern 2: Căn chỉnh chiều dữ liệu (Reshape & Transpose)

```python
X = np.array([[1, 2], [3, 4], [5, 6]]) # Shape (3, 2)
W = np.array([[0.1, 0.2], [0.3, 0.4]]) # Shape (2, 2)

# Y = X * W^T
Y = X @ W.T
```

**Ghi nhớ:** Ký hiệu `.T` là ma trận chuyển vị (đảo hàng thành cột). Thường xuyên dùng khi tính $X \cdot W^T$.

### Pattern 3: Đạo hàm số học (Numeric Derivative)

Dùng để kiểm tra đạo hàm (Gradient Checking) khi không có AutoGrad.

```python
def f(x): return x**2
x = 3.0
h = 1e-5 # Số rất nhỏ
# Định nghĩa đạo hàm: (f(x+h) - f(x-h)) / 2h (Central difference)
grad = (f(x + h) - f(x - h)) / (2 * h)
# KQ: ~6.0
```

**Ghi nhớ:** Đây là cách máy tính "xấp xỉ" đạo hàm bằng cách tính độ dốc của đoạn thẳng rất nhỏ.

## 📋 API Cheat Sheet

| Việc cần làm                | Code                   | Docs                           |
| --------------------------- | ---------------------- | ------------------------------ |
| Trung bình (Mean)           | `np.mean(X, axis=0)`   | Tính dọc theo cột              |
| Độ lệch chuẩn (Std)         | `np.std(X, axis=0)`    | Thường dùng để Normalize       |
| Căn bậc 2                   | `np.sqrt(X)`           |                                |
| e mũ x                      | `np.exp(X)`            | Dùng trong hàm Softmax/Sigmoid |
| Lấy phần tử lớn nhất        | `np.max(X, axis=1)`    | Tính dọc theo hàng             |
| Vị trí của phần tử lớn nhất | `np.argmax(X, axis=1)` | Dùng lấy class dự đoán         |

## 🏋️ Bài Luyện Code Tay

**Quy tắc:** Đóng tất cả tài liệu. Mở notebook trống. Hẹn giờ.

| #   | Bài                                                                                                                            | Thời gian | Hint (chỉ xem khi bí)             |
| --- | ------------------------------------------------------------------------------------------------------------------------------ | --------- | --------------------------------- |
| 1   | Cho vector dự đoán `y_pred` và thực tế `y_true`. Viết hàm tính sai số MSE: $\frac{1}{n}\sum (y\_pred - y\_true)^2$ bằng NumPy. | 5 phút    | `np.mean((y_pred - y_true)**2)`   |
| 2   | Code 1 bước cập nhật Gradient Descent: `w_new = w_old - lr * grad`                                                             | 3 phút    | Đơn giản chỉ là biểu thức đại số. |

## 🧠 Flashcards (Hỏi → Trả lời)

| Hỏi                                                                                   | Trả lời                                                                             |
| ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Ma trận A (3, 4) nhân ma trận B (4, 5) ra ma trận C shape bao nhiêu?                  | Shape C = (3, 5).                                                                   |
| Nếu hàm Loss đang ở đáy thung lũng (cực tiểu), thì Gradient bằng mấy?                 | Bằng 0 vector.                                                                      |
| Tại sao AI ưu tiên dùng `np.mean(..., axis=0)` thay vì vòng lặp for tính tổng chia N? | Để tận dụng Vectorization (C-backend), tính toán song song nhanh hơn hàng trăm lần. |
