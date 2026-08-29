# Bài tập: Logistic Regression

## Tầng 1: Understand

**1. Tại sao không dùng MSE?**
Trong phân loại, hàm Sigmoid sẽ làm cho giá trị dự đoán bị "bóp" lại vào khoảng (0, 1). Nếu bạn cố tình dùng MSE làm Loss Function, đồ thị Loss theo trọng số $W$ sẽ trông như thế nào? Tại sao thuật toán Gradient Descent dễ bị "kẹt" lại?

## Tầng 2: Implement

**1. Multiclass Thresholding**
Bạn có 3 lớp. Giả sử `predict_proba` trả về `[0.3, 0.4, 0.3]`. Class được dự đoán sẽ là gì? Dùng hàm NumPy nào để lấy ra nhãn dự đoán (0, 1, hoặc 2)?

## Tầng 3: Experiment

**1. Impact of C**
Sử dụng dữ liệu (Overfit) từ `make_classification(n_samples=50, n_features=20, n_informative=2)`.
Chạy `LogisticRegression` với `C=1000` (ít phạt) và `C=0.01` (phạt nhiều).
So sánh độ lớn trung bình của các trọng số `np.mean(np.abs(model.coef_))` ở 2 trường hợp.

## Tầng 4: Transfer

**1. Xử lý Mất cân bằng lớp (Imbalanced Data)**
Nếu bạn đoán "Giao dịch có phải lừa đảo không?", data thật có 99% không lừa đảo, 1% lừa đảo.
Nếu mô hình dự đoán mọi thứ là "Không lừa đảo", độ chính xác (Accuracy) vẫn là 99%. Nhưng mô hình vô dụng!
Trong `LogisticRegression` của Sklearn, có một tham số giúp "phạt nặng" hơn khi mô hình đoán sai class 1. Hãy tra cứu tài liệu và tìm tham số đó (Bắt đầu bằng chữ `class_...`).

## Tầng 5: Olympiad

_(Xem `olympiad_transfer.md`)_
