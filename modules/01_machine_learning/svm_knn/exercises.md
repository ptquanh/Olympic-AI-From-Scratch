# Bài tập: SVM & KNN

## Tầng 1: Understand

**1. Tại sao SVM cần Scale dữ liệu?**
Mô hình SVM cố gắng tối đa hóa khoảng cách (margin) giữa các điểm dữ liệu và siêu phẳng (hyperplane). Khoảng cách này được tính bằng khoảng cách hình học (Euclidean). Nếu một đặc trưng có giá trị từ 1-1000 và đặc trưng khác có giá trị từ 0-1, khoảng cách sẽ bị chi phối hoàn toàn bởi đặc trưng đầu tiên. Vì vậy, bước tiền xử lý BẮT BUỘC trước khi dùng SVM (và KNN) là gì?

## Tầng 2: Implement

**1. Thử nghiệm Kernel**
Dùng dữ liệu `make_circles(n_samples=100, factor=0.3, noise=0.05)` (Dữ liệu hình vòng tròn lồng nhau, không thể phân tách tuyến tính bằng đường thẳng).
Thử train `SVC(kernel='linear')` và đo độ chính xác.
Sau đó đổi sang `SVC(kernel='rbf')` và đo lại độ chính xác. Bạn rút ra kết luận gì?

## Tầng 3: Experiment

**1. Chọn K cho KNN**
Với bộ dữ liệu Iris, dùng vòng lặp thử số lượng k từ 1 đến 20 cho KNeighborsClassifier. Vẽ biểu đồ độ chính xác tương ứng với từng K và tìm k tối ưu. So sánh kết quả khi k=1 và k=20.
