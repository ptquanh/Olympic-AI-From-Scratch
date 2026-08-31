# Bài tập: Logistic Regression

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Tại sao không dùng MSE?**
Trong phân loại, hàm Sigmoid sẽ làm cho giá trị dự đoán bị "bóp" lại vào khoảng (0, 1). Nếu bạn cố tình dùng MSE làm Loss Function, đồ thị Loss theo trọng số $W$ sẽ trông như thế nào? Tại sao thuật toán Gradient Descent dễ bị "kẹt" lại?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Multiclass Thresholding**
Bạn có 3 lớp. Giả sử `predict_proba` trả về `[0.3, 0.4, 0.3]`. Class được dự đoán sẽ là gì? Dùng hàm NumPy nào để lấy ra nhãn dự đoán (0, 1, hoặc 2)?

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Impact of C**
Sử dụng dữ liệu (Overfit) từ `make_classification(n_samples=50, n_features=20, n_informative=2)`.
Chạy `LogisticRegression` với `C=1000` (ít phạt) và `C=0.01` (phạt nhiều).
So sánh độ lớn trung bình của các trọng số `np.mean(np.abs(model.coef_))` ở 2 trường hợp.

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.

## T-1 — Transfer

**Learning outcome:** Chuyển kỹ thuật sang dữ liệu mới mà không leakage, dùng metric và failure mode phù hợp.

**1. Xử lý Mất cân bằng lớp (Imbalanced Data)**
Nếu bạn đoán "Giao dịch có phải lừa đảo không?", data thật có 99% không lừa đảo, 1% lừa đảo.
Nếu mô hình dự đoán mọi thứ là "Không lừa đảo", độ chính xác (Accuracy) vẫn là 99%. Nhưng mô hình vô dụng!
Trong `LogisticRegression` của Sklearn, có một tham số giúp "phạt nặng" hơn khi mô hình đoán sai class 1. Hãy tra cứu tài liệu và tìm tham số đó (Bắt đầu bằng chữ `class_...`).

**Kết quả mong đợi:** Pipeline chạy trên dữ liệu/bối cảnh mới, metric phù hợp và phân tích ít nhất một failure mode.

## O-1 — Olympiad

**Learning outcome:** Dựng baseline theo đúng competition profile, timebox và artifact nộp có thể chạy lại.

_(Xem `olympiad_transfer.md`)_

**Kết quả mong đợi:** Baseline tái lập được trong timebox, validation đúng, metric và checklist file cần nộp.
