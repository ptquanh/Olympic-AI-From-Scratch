# 📈 Logistic Regression (Hồi quy Logistic)

> **Track:** Foundation ⭐ | Contest 📖

## ① Prerequisite Check

- Hàm $e^x$ có đặc điểm gì?
- Bạn đã hiểu được Linear Regression (Linear Combination + Gradient Descent) chưa?
  _(Nếu chưa rõ, hãy xem lại `linear_regression`)_

## ② Learning Outcomes

- **Derive:** Hiểu được tại sao ta phải dùng hàm Sigmoid và hàm Binary Cross-Entropy Loss.
- **Implement:** Viết code Logistic Regression from scratch bằng NumPy.
- **Explain:** Hiểu khái niệm "Decision Boundary" (Đường phân chia).

## ③ Concept Map

`Linear Regression` → **`Logistic Regression`** → `Mạng Nơ-ron (Classification)`

## ④ Intuition (Trực giác)

Linear Regression dự đoán giá trị liên tục (vd: $120.5$). Nhưng nếu ta muốn dự đoán "Email này có phải Spam không?" (Chỉ có 0 hoặc 1), Linear Regression sẽ thất bại vì nó có thể dự đoán ra $-0.5$ hoặc $1.2$.
Để ép kết quả về xác suất (từ 0 đến 1), ta bọc hàm hồi quy tuyến tính bằng một hàm chữ S (Sigmoid).
Và vì ta đang tính xác suất, ta không thể dùng MSE (sẽ tạo ra hàm bị lồi lõm nhiều đáy), mà phải dùng **Cross-Entropy Loss**.

## ⑤ Math / Derivation

**1. Hàm Sigmoid**
$\sigma(z) = \frac{1}{1 + e^{-z}}$

**2. Hàm giả thuyết**
$\hat{y} = \sigma(XW)$

**3. Hàm mất mát (Binary Cross-Entropy / Log Loss)**
$J(W) = -\frac{1}{N} \sum_{i=1}^{N} [y_i \log(\hat{y}_i) + (1 - y_i)\log(1 - \hat{y}_i)]$

**4. Đạo hàm (Kỳ diệu: Giống hệt Linear Regression)**
$\frac{\partial J}{\partial W} = \frac{1}{N} X^T (\hat{y} - y)$

## ⑥ Worked Example

Có 1 điểm dữ liệu $x = [2.0]$, nhãn $y = 1$ (Spam).
Giả sử $W = [0.0]$.

1. Tính $z = 2.0 \times 0.0 = 0.0$
2. Tính xác suất $\hat{y} = \sigma(0) = 0.5$ (50% là Spam).
3. Tính Loss: $-[1 \times \log(0.5) + 0] \approx 0.69$
4. Tính Gradient: $dW = x \times (\hat{y} - y) = 2.0 \times (0.5 - 1.0) = -1.0$.
5. Cập nhật $W = 0 - 0.1 \times (-1.0) = 0.1$.
   Lần sau, $z = 2.0 \times 0.1 = 0.2$, $\hat{y} = \sigma(0.2) = 0.55$. (Xác suất tăng dần về 1).

## ⑦ From-Scratch

Xem `01_from_scratch.ipynb`

## ⑧ Framework

Xem `02_framework.ipynb`

## ⑨ Experiments

Xem `03_experiments.ipynb`

## ⑩ Misconceptions

- ❌ **Sai:** Logistic Regression là thuật toán Hồi quy (Regression).
- ✅ **Đúng:** Dù có chữ Regression, nó là thuật toán **Phân loại (Classification)**. (Lý do có chữ Regression là do phần lõi của nó là tổ hợp tuyến tính $XW$).
- ❌ **Sai:** Logistic Regression chỉ giải quyết bài toán Binary (2 classes).
- ✅ **Đúng:** Có thể dùng nó cho bài toán Multiclass thông qua phương pháp One-vs-Rest hoặc đổi hàm Sigmoid thành hàm Softmax (Multinomial Logistic Regression).

## ⑪ Code Notes

Xem `code_notes.md`

## ⑫ Exercises

Xem `exercises.md`

## ⑬ Olympiad Transfer

Xem `olympiad_transfer.md`

## ⑭ References

Xem `references.md`

## ⑮ Mastery Check

- Làm sao để mở rộng Logistic Regression từ 2 class lên 3 class?
- Đạo hàm của Logistic Regression giống hay khác Linear Regression? Tại sao Loss lại khác?

## ⑯ Time Estimate

Theory: ~1h, Code: ~1h, Exercises: ~1h
