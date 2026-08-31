# Bài tập: Unsupervised Learning

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Vấn đề của K-Means**
K-Means dùng khoảng cách Euclidean. Sẽ ra sao nếu dữ liệu của bạn có dạng hai vòng tròn đồng tâm (một vòng to, một vòng nhỏ ở giữa)? K-Means có phân loại được 2 cụm này không?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. PCA**
Chạy PCA `n_components=2` trên bộ dữ liệu Iris và in ra shape của tập dữ liệu mới.

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Khảo sát DBSCAN**
Tìm hiểu thuật toán DBSCAN (Density-Based Spatial Clustering of Applications with Noise). Dùng `DBSCAN(eps=0.5, min_samples=5)` để gom cụm dữ liệu `make_moons(n_samples=200, noise=0.05)`. K-Means hay DBSCAN làm tốt hơn trên dữ liệu hình mặt trăng này?

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
