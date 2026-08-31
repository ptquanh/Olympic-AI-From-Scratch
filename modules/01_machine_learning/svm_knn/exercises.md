# Bài tập: SVM & KNN

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Lựa chọn mô hình**
Giữa SVM và KNN, thuật toán nào "Lười biếng" (Lazy learning) và thuật toán nào cực kỳ nhạy cảm với dữ liệu chưa được chuẩn hóa (Scale)?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. SVC Kernel Trick**
Sử dụng dữ liệu `make_circles(n_samples=100, noise=0.1, factor=0.1)`. Thử train với `SVC(kernel='linear')` và `SVC(kernel='rbf')`. Cái nào chính xác hơn?

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Tác động của số K trong KNN**
Với KNN, hãy thử thay đổi số lượng hàng xóm `n_neighbors` từ 1 đến 50. Plot độ chính xác. Khi K quá nhỏ, hiện tượng gì xảy ra? Khi K bằng tổng số điểm dữ liệu, hiện tượng gì xảy ra?

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
