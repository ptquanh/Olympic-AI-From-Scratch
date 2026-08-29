# Bài tập: Unsupervised

## Tầng 1: Understand

**1. Tại sao PCA lại có thể dùng để nén dữ liệu?**
Ví dụ 1 tấm ảnh có 1000 pixel (1000 chiều). Nếu ta chạy PCA n_components=100, ta mất đi 900 chiều dữ liệu. Vậy tại sao khi khôi phục lại ảnh, nó vẫn gần giống ảnh gốc?

## Tầng 2: Implement

**1. Trực quan hóa dữ liệu cao chiều**
Chạy PCA n_components=2 trên bộ dữ liệu MNIST và vẽ Scatter Plot màu sắc theo nhãn chữ số.

## Tầng 3: Experiment

**1. Tìm K tối ưu cho K-Means**
Sử dụng phương pháp Elbow (Khuỷu tay) để vẽ biểu đồ WCSS (Within-Cluster-Sum-of-Squares) tương ứng với số lượng cụm K từ 1 đến 10. Chỉ ra điểm khuỷu tay và xác định K tối ưu.
