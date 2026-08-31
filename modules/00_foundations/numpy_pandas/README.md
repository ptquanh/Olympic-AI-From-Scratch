# NumPy & Pandas

> **Thời gian học ước tính:** 3 giờ (theory: 1h, code: 1h, exercises: 1h)
> **Loại:** Concept Lesson
> **Track:** Foundation ⭐ | Contest 📖

## Prerequisite Check

Trước khi bắt đầu, bạn cần trả lời được:

1. Phân biệt List và Dictionary trong Python?
2. Tại sao dùng vòng lặp `for` lồng nhau lại chạy chậm?

Nếu chưa → quay lại chương `python_essentials`.

## Learning Outcomes

Sau chương này, bạn sẽ có thể:

- [ ] Tạo, reshape, slice NumPy arrays
- [ ] Giải thích broadcasting rules bằng ví dụ cụ thể
- [ ] Đọc, filter, merge, groupby Pandas DataFrame
- [ ] Vectorize operations thay vì dùng for loop

## Concept Map

```text
[Python Essentials] --> [CHƯƠNG NÀY] --> [Feature Engineering]
                             │
                             ├── dùng trong [Linear Regression]
                             └── nền tảng cho [Mọi thao tác dữ liệu]

```

## 1. Intuition — Tại Sao Cần NumPy & Pandas?

Python gốc (Vanilla Python) với List và vòng lặp `for` hoạt động cực kỳ chậm khi xử lý dữ liệu lớn (hàng triệu phần tử). Điều này do Python là ngôn ngữ thông dịch (interpreted) và tự động quản lý kiểu dữ liệu (dynamically typed).

**NumPy** (Numerical Python) giải quyết vấn đề này bằng cách lưu trữ dữ liệu trong mảng C đồng nhất (chỉ chứa 1 kiểu dữ liệu, vd: số thực) và đẩy các vòng lặp tính toán xuống ngôn ngữ C bên dưới. Tốc độ có thể tăng hàng trăm lần nhờ cơ chế **Vectorization**.

**Pandas** được xây dựng trên nền NumPy, cung cấp cấu trúc dữ liệu `DataFrame` (giống bảng Excel) và `Series` (giống 1 cột trong Excel), giúp xử lý dữ liệu dạng bảng, missing values, và chuỗi thời gian cực kỳ dễ dàng.

## 2. NumPy: Cốt lõi toán học

- **ndarray**: Cấu trúc mảng n-chiều. Mỗi mảng có `shape` (kích thước) và `dtype` (kiểu dữ liệu).
- **Vectorization**: Thay vì viết `for i in range(len(a)): c[i] = a[i] + b[i]`, bạn chỉ cần viết `c = a + b`.
- **Broadcasting**: Cơ chế thần kỳ giúp tính toán giữa 2 mảng không cùng kích thước (vd: mảng 2D cộng với mảng 1D). Quy tắc: đi từ chiều cuối cùng lên trước, nếu bằng nhau hoặc một trong hai bằng 1 thì hợp lệ.

## 3. Pandas: Xử lý dữ liệu bảng

- **DataFrame**: Bảng 2 chiều có nhãn hàng (index) và nhãn cột (columns).
- **read_csv**: Hàm mạnh mẽ nhất để nạp dữ liệu.
- **Lọc (Filtering)**: `df[df['age'] > 18]`
- **Gộp (Groupby & Merge)**: Công cụ phân tích dữ liệu vô giá.

## 4. Worked Example: Từ For Loop sang NumPy

Cho 2 vector $A$ và $B$ mỗi vector có 10 triệu phần tử. Tính $C = A \cdot B$ (dot product).

```python
import numpy as np
import time

# Tạo dữ liệu
A = np.random.rand(10000000)
B = np.random.rand(10000000)

# Dùng Vanilla Python (For Loop)
start = time.time()
dot_product = 0
for i in range(len(A)):
    dot_product += A[i] * B[i]
print(f"For loop mất: {time.time() - start:.4f} giây")
# ~ 2.5 giây

# Dùng NumPy (Vectorized)
start = time.time()
dot_product_np = np.dot(A, B) # Hoặc A @ B
print(f"NumPy mất: {time.time() - start:.4f} giây")
# ~ 0.01 giây (Nhanh hơn 250 lần!)

```

## 5. Common Mistakes & Misconceptions

> ❌ **Sai:** Dùng `iterrows()` cho mọi phép biến đổi dù đã có phép toán vectorized.
> ✅ **Đúng:** Ưu tiên NumPy ufunc, Pandas `.str` và phép toán theo cột. `.apply()` vẫn gọi Python cho nhiều trường hợp; loop chỉ hợp lý khi logic không thể biểu diễn rõ bằng API vectorized và đã đo hiệu năng.

> ❌ **Sai:** Thay đổi dữ liệu trực tiếp trên slice của DataFrame mà không rõ nó là View hay Copy, dẫn đến lỗi `SettingWithCopyWarning`.
> ✅ **Đúng:** Dùng `.copy()` nếu bạn thực sự muốn tách riêng một bảng mới. Dùng `.loc[]` để gán giá trị một cách an toàn.

> ❌ **Sai:** Dùng `list` rồi kỳ vọng `a * 2` nhân từng phần tử.
> ✅ **Đúng:** Dùng `np.ndarray` có dtype/shape rõ cho tính toán vectorized; `list` vẫn phù hợp với collection nhỏ, không đồng nhất hoặc logic Python thông thường.

## ⑯ Time Estimate

Theory: ~2h · Code: ~2h · Exercises: ~1.5h
