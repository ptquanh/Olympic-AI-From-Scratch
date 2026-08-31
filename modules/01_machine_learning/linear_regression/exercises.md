# Bài tập: Linear Regression

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Tại sao dùng bình phương trong MSE?**
Hàm Loss là MSE (Mean **Squared** Error), tại sao ta lại bình phương $(y_{pred} - y_{true})^2$ mà không lấy trị tuyệt đối $|y_{pred} - y_{true}|$?
(Gợi ý: Liên quan đến việc tính toán đạo hàm).

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Lỗi Gradient Descent**
Đoạn code Gradient Descent sau bị lỗi dẫn đến Loss không giảm. Hãy tìm và sửa lỗi.

```python
for i in range(100):
    y_pred = X.dot(W)
    loss = np.mean((y_pred - y)**2)

    dW = 2 * np.dot(X.T, (y_pred - y)) / len(y)

    W = W + lr * dW # Sửa dòng này

```

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Tác động của Learning Rate**
Trong notebook `01_from_scratch.ipynb`, hãy thay đổi `learning_rate` thành `1.5`, `0.0001` và `0.1`.
Ghi lại hiện tượng xảy ra với Loss (nó giảm chậm, giảm nhanh, hay báo lỗi NaN?).

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.

## T-1 — Transfer

**Learning outcome:** Chuyển kỹ thuật sang dữ liệu mới mà không leakage, dùng metric và failure mode phù hợp.

**1. Polynomial Features**
Nhiều quan hệ thực tế không tuyến tính theo feature gốc. Cho dữ liệu hình Sin:

`X = np.linspace(0, 10, 100).reshape(-1, 1)`

`y = np.sin(X) + np.random.randn(100, 1)*0.1`
Bạn hãy dùng `PolynomialFeatures` (bậc 3, bậc 5, bậc 15) kết hợp `LinearRegression` để fit dữ liệu này. Đồ thị nào nhìn hợp lý nhất?

**Kết quả mong đợi:** Pipeline chạy trên dữ liệu/bối cảnh mới, metric phù hợp và phân tích ít nhất một failure mode.

## O-1 — Olympiad

**Learning outcome:** Dựng baseline theo đúng competition profile, timebox và artifact nộp có thể chạy lại.

_(Xem `olympiad_transfer.md`)_

**Kết quả mong đợi:** Baseline tái lập được trong timebox, validation đúng, metric và checklist file cần nộp.
