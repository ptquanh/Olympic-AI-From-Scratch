# Math Essentials (Cheat Sheet)

> **Thời gian học ước tính:** 2 giờ (theory: 1h, code: 0.5h, exercises: 0.5h)
> **Loại:** Concept Lesson
> **Track:** Foundation ⭐ | Contest 📖

## Prerequisite Check

Trước khi bắt đầu, bạn cần trả lời được:

1. Làm sao để nhân 2 ma trận bằng NumPy?
2. Ý nghĩa hình học của đạo hàm (derivative) là gì?

Nếu chưa → tiếp tục học chương này.

## Learning Outcomes

Sau chương này, bạn sẽ có thể:

- [ ] Nhân ma trận bằng tay (kích thước nhỏ) và bằng NumPy, giải thích quy tắc shape
- [ ] Tính đạo hàm riêng (partial derivative) cho hàm 2 biến đơn giản
- [ ] Giải thích thuật toán Gradient Descent bằng trực giác (người mù xuống núi)
- [ ] Tính mean, variance, covariance từ dữ liệu mẫu

## Concept Map

```text
[Regex & Data Handling] --> [CHƯƠNG NÀY]  --> [Visualization]
                          │
                          ├── dùng trong [Tính Loss & Backpropagation]
                          └── nền tảng cho [Đọc hiểu các paper/công thức]
```

## 1. Intuition — Tại Sao Cần Toán?

Machine Learning thực chất là các bài toán **Tối ưu hóa (Optimization)** dựa trên dữ liệu.

- **Đại số tuyến tính (Linear Algebra):** Ngôn ngữ để biểu diễn dữ liệu (vector, ma trận, tensor) và thực hiện tính toán hàng loạt (song song).
- **Giải tích (Calculus):** Công cụ để tìm ra hướng đi tốt nhất (đạo hàm/gradient) nhằm tối ưu hóa mô hình (giảm sai số).
- **Xác suất & Thống kê (Probability & Statistics):** Ngôn ngữ để biểu diễn sự không chắc chắn và đánh giá mô hình.

Bạn **không cần** phải giải tay các phương trình vi phân phức tạp. Bạn chỉ cần hiểu **trực giác** (intuition) và biết cách **chuyển công thức thành code NumPy/PyTorch**.

## 2. Đại Số Tuyến Tính (Linear Algebra)

### Dot Product (Tích vô hướng)

Tích vô hướng của 2 vector $a$ và $b$ trả về một số vô hướng (scalar). Nó đo lường sự "tương đồng" về hướng của 2 vector.
$a \cdot b = a_1b_1 + a_2b_2 + ... + a_nb_n$

### Matrix Multiplication (Nhân Ma Trận)

Nếu có ma trận $A$ kích thước $(M \times N)$ và ma trận $B$ kích thước $(N \times K)$, thì kết quả $C = A \cdot B$ sẽ có kích thước $(M \times K)$.
Quy tắc: **Lấy Hàng của A nhân vô hướng với Cột của B.**

## 3. Giải Tích (Calculus)

### Đạo Hàm (Derivative)

Đạo hàm $f'(x)$ (hay $\frac{df}{dx}$) cho biết: nếu ta tăng $x$ lên một chút xíu, thì hàm $f(x)$ thay đổi thế nào?
Ý nghĩa hình học: Độ dốc (slope) của tiếp tuyến tại điểm $x$.

### Gradient

Nếu hàm có nhiều biến $f(x, y)$, thì Gradient (kí hiệu $\nabla f$) là một vector chứa các đạo hàm riêng theo từng biến.
$\nabla f = \left[ \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right]$
**Trực giác quan trọng nhất của AI:** Gradient luôn chỉ theo hướng làm hàm $f$ **TĂNG NHANH NHẤT**.

### Gradient Descent (Người mù xuống núi)

Nếu $f(x)$ là hàm sai số (Loss function), ta muốn tìm $x$ để sai số nhỏ nhất.
Cách làm:

1. Đứng ở một điểm $x$ ngẫu nhiên.
2. Tìm độ dốc (Gradient). Gradient chỉ hướng lên dốc.
3. Đi ngược lại hướng Gradient một bước nhỏ (nhân với Learning Rate).
4. Lặp lại cho đến khi đến đáy thung lũng (Gradient = 0).

$x_{new} = x_{old} - \text{learning\_rate} \times \nabla f(x_{old})$

## 4. Xác Suất & Thống Kê (Statistics)

- **Mean ($\mu$):** Giá trị trung bình.
- **Variance ($\sigma^2$):** Phương sai. Đo mức độ phân tán của dữ liệu. Phương sai cao nghĩa là dữ liệu trải rộng.
- **Standard Deviation ($\sigma$):** Độ lệch chuẩn. Căn bậc 2 của phương sai. Cùng đơn vị với dữ liệu gốc.
- **Normal Distribution:** Phân phối chuẩn (hình quả chuông). Rất nhiều dữ liệu trong tự nhiên (chiều cao, cân nặng, sai số đo lường) tuân theo phân phối này.

## 5. Common Mistakes & Misconceptions

> ❌ **Sai:** Nhân 2 ma trận bằng phép nhân `*` trong Python.
> ✅ **Đúng:** Phép `*` trong NumPy là Element-wise multiplication (nhân từng phần tử). Để nhân ma trận thật sự, phải dùng `np.dot(A, B)` hoặc toán tử `@` (ví dụ `A @ B`).

> ❌ **Sai:** Học thuộc lòng các quy tắc đạo hàm phức tạp (như đạo hàm của hàm lượng giác, logarit bậc cao) để thi AI.
> ✅ **Đúng:** Các framework (PyTorch/TensorFlow) có cơ chế AutoGrad (tự động tính đạo hàm). Bạn chỉ cần hiểu Chain Rule (quy tắc chuỗi) để biết gradient chảy từ đầu ra về đầu vào như thế nào.
