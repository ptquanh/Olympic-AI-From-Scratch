# 📈 Linear Regression (Hồi quy tuyến tính)

> **Track:** Foundation ⭐ | Contest 📖

## ① Prerequisite Check

- Bạn có biết phương trình đường thẳng $y = ax + b$ là gì không?
- Đạo hàm của $x^2$ là gì?
- Phép nhân hai ma trận (hoặc dot product) hoạt động thế nào?
  _(Nếu chưa rõ, hãy xem lại `00_foundations/math_essentials`)_

## ② Learning Outcomes

- **Derive:** Tự diễn giải công thức Gradient Descent cho Linear Regression.
- **Implement:** Viết code Linear Regression from scratch bằng NumPy.
- **Predict:** Sử dụng `sklearn.linear_model.LinearRegression` để dự đoán dữ liệu thật.
- **Explain:** Phân biệt được L1 (Lasso) và L2 (Ridge) Regularization.

## ③ Concept Map

`Toán nền tảng` → **`Linear Regression`** → `Logistic Regression` / `Mạng Nơ-ron (Deep Learning)`

## ④ Intuition (Trực giác)

Giả sử bạn cần dự đoán giá nhà dựa trên diện tích. Rõ ràng nhà càng rộng thì giá càng cao.
Làm sao để máy tính học được mối quan hệ này?
Chúng ta yêu cầu máy tính vẽ một đường thẳng đi qua các điểm dữ liệu (diện tích, giá nhà) sao cho "sai số" giữa đường thẳng đó và các điểm dữ liệu thực tế là NHỎ NHẤT.

## ⑤ Math / Derivation

**1. Hàm giả thuyết (Hypothesis)**
Với 1 biến: $y = wx + b$
Với nhiều biến (Ma trận): $\hat{Y} = XW$ (Đã gộp bias $b$ vào $W$ bằng cách thêm cột 1 vào $X$)

**2. Hàm mất mát (Loss Function - MSE)**
$J(W) = \frac{1}{N} \sum_{i=1}^{N} (\hat{y}_i - y_i)^2 = \frac{1}{N} ||XW - Y||^2$

**3. Đạo hàm (Gradients)**
Để tối thiểu hóa $J(W)$, ta tìm đạo hàm theo $W$:
$\frac{\partial J}{\partial W} = \frac{2}{N} X^T (XW - Y)$

**4. Cập nhật trọng số (Gradient Descent)**
$W = W - \alpha \frac{\partial J}{\partial W}$ (với $\alpha$ là learning rate).

## ⑥ Worked Example

Có 2 điểm dữ liệu: $(1, 2)$ và $(2, 4)$.
Khởi tạo $w = 0, b = 0$. $\alpha = 0.1$.
Dự đoán: $\hat{y}_1 = 0(1) + 0 = 0$, $\hat{y}_2 = 0(2) + 0 = 0$.
Gradients (bỏ qua $2/N$ cho đơn giản):
$dw = 1*(0-2) + 2*(0-4) = -2 - 8 = -10$.
$db = (0-2) + (0-4) = -6$.
Cập nhật:
$w = 0 - 0.1(-10) = 1.0$
$b = 0 - 0.1(-6) = 0.6$
Sau 1 bước, đường thẳng từ $y=0$ thành $y=1x + 0.6$ (Tiến rất gần tới đáp án $y=2x$).

## ⑦ From-Scratch

Xem `01_from_scratch.ipynb`

## ⑧ Framework

Xem `02_framework.ipynb`

## ⑨ Experiments

Xem `03_experiments.ipynb`

## ⑩ Misconceptions

- ❌ **Sai:** Linear Regression không thể mô hình hóa dữ liệu dạng cong (phi tuyến).
- ✅ **Đúng:** Bạn có thể dùng PolynomialFeatures (vd: thêm $x^2, x^3$) để tạo biến mới, Linear Regression vẫn hoạt động và fit được đường cong.
- ❌ **Sai:** Learning rate càng lớn mô hình học càng nhanh.
- ✅ **Đúng:** Learning rate quá lớn sẽ làm Gradient Descent "văng" ra khỏi đáy (diverge) và Loss sẽ tiến tới vô cực (NaN).

## ⑪ Code Notes

Xem `code_notes.md`

## ⑫ Exercises

Xem `exercises.md`

## ⑬ Olympiad Transfer

Xem `olympiad_transfer.md`

## ⑭ References

Xem `references.md`

## ⑮ Mastery Check

- Nếu cho bạn 1 ma trận X và Y, bạn có tự code vòng lặp tính `dW` và cập nhật $W$ không cần nhìn tài liệu không?
- Bạn có giải thích được tại sao L1 lại tạo ra vector trọng số thưa (nhiều số 0) không?

## ⑯ Time Estimate

Theory: ~1h, Code: ~1.5h, Exercises: ~1h
