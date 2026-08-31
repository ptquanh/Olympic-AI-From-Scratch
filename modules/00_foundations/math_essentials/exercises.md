# Exercises: Math Essentials

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Phân biệt Phép Nhân**
Giả sử `A` và `B` là hai ma trận vuông $3 \times 3$ trong NumPy.

- Giải thích kết quả của `A * B`.
- Giải thích kết quả của `A @ B` (hoặc `np.dot(A, B)`).

**2. Trực giác Gradient**
Bạn đang đứng trên một ngọn núi có hình dạng là hàm số $f(x, y)$. Bạn muốn đi xuống thung lũng (cực tiểu). Bạn tính được gradient tại chỗ bạn đứng là $\nabla f = [2.5, -1.2]$.

- Hướng $[2.5, -1.2]$ là hướng đi lên hay đi xuống núi?
- Để xuống núi, bạn phải bước đi theo vector hướng nào?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Softmax Function (Toán + Code)**
Hàm Softmax dùng để biến đổi một vector các số thực thành phân phối xác suất (tổng bằng 1, các số dương). Công thức:
$Softmax(z_i) = \frac{e^{z_i}}{\sum_{j} e^{z_j}}$

- Viết code numpy (không dùng for loop) tính Softmax cho vector `z = np.array([2.0, 1.0, 0.1])`.

**2. Manual Matrix Multiplication**
Cho:
$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ và $B = \begin{bmatrix} 5 \\ 6 \end{bmatrix}$

- Tính nhẩm bằng tay kết quả $C = A \cdot B$.
- Viết script numpy để verify lại kết quả.

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Gradient Checking bằng Xấp Xỉ Số (Numeric Approximation)**
Cho hàm $f(x) = x^3 - 2x^2 + x$.

1. Tính bằng tay đạo hàm giải tích (analytic derivative) $f'(x)$.
2. Tại $x = 2$, giá trị đạo hàm chính xác là bao nhiêu?
3. Viết code xấp xỉ đạo hàm tại $x = 2$ bằng công thức xấp xỉ trung tâm (Central difference): $\frac{f(x+h) - f(x-h)}{2h}$ với $h=0.0001$.
4. So sánh sai số giữa giá trị chính xác và giá trị xấp xỉ.

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
