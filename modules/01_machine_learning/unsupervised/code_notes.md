# Code Notes: Unsupervised Learning

## 🔑 Core Patterns

### Pattern 1: K-Means Clustering

```python
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. Khởi tạo mô hình gom thành 3 cụm
kmeans = KMeans(n_clusters=3, random_state=42)

# 2. Gom cụm và gán nhãn cho dữ liệu X
clusters = kmeans.fit_predict(X)

# 3. Trực quan hóa
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='red', marker='X')
plt.show()
```

### Pattern 2: Giảm chiều với PCA

```python
from sklearn.decomposition import PCA

# 1. Giảm xuống 2 chiều
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# 2. Xem mức độ dữ liệu được giữ lại
print(f"Variance ratio: {sum(pca.explained_variance_ratio_):.2f}")
```

## 📋 API Cheat Sheet

| Việc cần làm      | Code                                   | Link Docs                                                                               |
| ----------------- | -------------------------------------- | --------------------------------------------------------------------------------------- |
| Phân cụm K-Means  | `KMeans(n_clusters=k).fit_predict(X)`  | [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) |
| Giảm chiều PCA    | `PCA(n_components=2).fit_transform(X)` | [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) |
| Thuật toán DBSCAN | `DBSCAN(eps=0.5, min_samples=5)`       | [DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html) |

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                  | Thời gian | Hint (ẩn)                             |
| --- | ---------------------------------------------------- | --------- | ------------------------------------- |
| 1   | Viết đoạn mã K-Means với k=5 và tính nhãn cụm cho X. | 3 phút    | `KMeans(n_clusters=5).fit_predict(X)` |
| 2   | Khởi tạo mô hình PCA giảm xuống 3 chiều.             | 2 phút    | `PCA(n_components=3)`                 |

## 🧠 Flashcards

| Hỏi                                | Trả lời                                                                                                                   |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Mục đích của thuật toán PCA là gì? | Giảm số chiều của dữ liệu trong khi vẫn giữ lại phần lớn thông tin (phương sai) để mô hình chạy nhanh hơn và chống nhiễu. |
| Nhược điểm của K-Means là gì?      | Phải chọn k từ trước. Không xử lý tốt cụm có hình dạng không tròn (non-spherical). Rất nhạy cảm với Outlier.              |
