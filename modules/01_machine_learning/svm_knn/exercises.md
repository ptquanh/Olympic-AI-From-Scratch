# Bài tập: SVM & KNN

## Tầng 1: Understand

**1. Lựa chọn mô hình**
Giữa SVM và KNN, thuật toán nào "Lười biếng" (Lazy learning) và thuật toán nào cực kỳ nhạy cảm với dữ liệu chưa được chuẩn hóa (Scale)?

## Tầng 2: Implement

**1. SVC Kernel Trick**
Sử dụng dữ liệu `make_circles(n_samples=100, noise=0.1, factor=0.1)`. Thử train với `SVC(kernel='linear')` và `SVC(kernel='rbf')`. Cái nào chính xác hơn?

## Tầng 3: Experiment

**1. Tác động của số K trong KNN**
Với KNN, hãy thử thay đổi số lượng hàng xóm `n_neighbors` từ 1 đến 50. Plot độ chính xác. Khi K quá nhỏ, hiện tượng gì xảy ra? Khi K bằng tổng số điểm dữ liệu, hiện tượng gì xảy ra?
