# Bài tập: Unsupervised Learning

## Tầng 1: Understand

**1. Vấn đề của K-Means**
K-Means dùng khoảng cách Euclidean. Sẽ ra sao nếu dữ liệu của bạn có dạng hai vòng tròn đồng tâm (một vòng to, một vòng nhỏ ở giữa)? K-Means có phân loại được 2 cụm này không?

## Tầng 2: Implement

**1. PCA**
Chạy PCA `n_components=2` trên bộ dữ liệu Iris và in ra shape của tập dữ liệu mới.

## Tầng 3: Experiment

**1. Khảo sát DBSCAN**
Tìm hiểu thuật toán DBSCAN (Density-Based Spatial Clustering of Applications with Noise). Dùng `DBSCAN(eps=0.5, min_samples=5)` để gom cụm dữ liệu `make_moons(n_samples=200, noise=0.05)`. K-Means hay DBSCAN làm tốt hơn trên dữ liệu hình mặt trăng này?
