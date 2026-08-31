# Code Notes: Linear Regression

## 🔑 Core Patterns

### Pattern 1: Scikit-learn Linear Regression

```python
from sklearn.linear_model import LinearRegression

# 1. Khởi tạo
model = LinearRegression()

# 2. Huấn luyện (Yêu cầu X phải là ma trận 2D)
model.fit(X_train, y_train)

# 3. Trích xuất trọng số
w = model.coef_       # Trọng số cho các features
b = model.intercept_  # Bias (hệ số tự do)

# 4. Dự đoán
y_pred = model.predict(X_test)

```

**Ghi nhớ:** Luôn đảm bảo `X_train` là mảng 2D (vd: shape `(N, 1)` chứ không phải `(N,)`).

### Pattern 2: Ridge & Lasso (L2 / L1 Regularization)

```python
from sklearn.linear_model import Ridge, Lasso

ridge = Ridge(alpha=1.0) # L2 penalty
lasso = Lasso(alpha=0.1) # L1 penalty

```

**Ghi nhớ:** Tham số `alpha` càng lớn, mức độ "phạt" (regularization) càng mạnh, trọng số càng bị ép nhỏ lại.

## 📋 API Cheat Sheet

| Việc cần làm    | Code                                           | Link Docs                                                                                                                |
| --------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Tính MSE        | `mean_squared_error(y_true, y_pred)`           | [sklearn metrics](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics)                           |
| Feature đa thức | `PolynomialFeatures(degree=2)`                 | [sklearn preprocessing](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html) |
| Lấy MSE RMSE    | `mean_squared_error(y, y_pred, squared=False)` | [mean_squared_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html)          |

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                                            | Thời gian | Hint (ẩn)                              |
| --- | ------------------------------------------------------------------------------ | --------- | -------------------------------------- |
| 1   | Khởi tạo mô hình Sklearn, fit dữ liệu ngẫu nhiên, lấy RMSE.                    | 5 phút    | `LinearRegression().fit(X, y)`         |
| 2   | Viết lại update rule (bước cập nhật) của Gradient Descent bằng NumPy           | 5 phút    | `W = W - lr * (2/N * X.T @ (X@W - y))` |
| 3   | Train `Lasso` với `alpha=100`, kiểm tra xem bao nhiêu trọng số bị biến thành 0 | 5 phút    | `np.sum(model.coef_ == 0)`             |

## 🧠 Flashcards

| Hỏi                                                                    | Trả lời                                                                                 |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Nếu Training Error cao, Validation Error cũng cao thì mô hình bị gì?   | Underfitting (cần model phức tạp hơn, vd: tăng bậc đa thức).                            |
| Nếu Training Error rất thấp, nhưng Validation Error rất cao thì bị gì? | Overfitting (cần thêm dữ liệu, hoặc dùng Regularization L1/L2).                         |
| L1 và L2 khác nhau chỗ nào quan trọng nhất trong thực hành?            | L1 làm cho feature bị loại bỏ (hệ số = 0), L2 làm cho hệ số nhỏ dần nhưng không bằng 0. |
