# Bài tập: Linear Regression

## Tầng 1: Understand

**1. Tại sao dùng bình phương trong MSE?**
Hàm Loss là MSE (Mean **Squared** Error), tại sao ta lại bình phương $(y_{pred} - y_{true})^2$ mà không lấy trị tuyệt đối $|y_{pred} - y_{true}|$?
(Gợi ý: Liên quan đến việc tính toán đạo hàm).

## Tầng 2: Implement

**1. Lỗi Gradient Descent**
Đoạn code Gradient Descent sau bị lỗi dẫn đến Loss không giảm. Hãy tìm và sửa lỗi.

```python
for i in range(100):
    y_pred = X.dot(W)
    loss = np.mean((y_pred - y)**2)

    dW = 2 * np.dot(X.T, (y_pred - y)) / len(y)

    W = W + lr * dW # Sửa dòng này
```

## Tầng 3: Experiment

**1. Tác động của Learning Rate**
Trong notebook `01_from_scratch.ipynb`, hãy thay đổi `learning_rate` thành `1.5`, `0.0001` và `0.1`.
Ghi lại hiện tượng xảy ra với Loss (nó giảm chậm, giảm nhanh, hay báo lỗi NaN?).

## Tầng 4: Transfer

**1. Polynomial Features**
Dữ liệu thực tế không bao giờ là đường thẳng. Cho dữ liệu hình Sin:
`X = np.linspace(0, 10, 100).reshape(-1, 1)`
`y = np.sin(X) + np.random.randn(100, 1)*0.1`
Bạn hãy dùng `PolynomialFeatures` (bậc 3, bậc 5, bậc 15) kết hợp `LinearRegression` để fit dữ liệu này. Đồ thị nào nhìn hợp lý nhất?

## Tầng 5: Olympiad

_(Xem `olympiad_transfer.md`)_
