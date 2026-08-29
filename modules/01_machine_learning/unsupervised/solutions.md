# Lời giải: Unsupervised

<details><summary><b>Tầng 1: Understand</b></summary>

PCA không chỉ là vứt đi 900 chiều ngẫu nhiên. Nó phân tích phương sai (sự thay đổi) của dữ liệu, và kết hợp tuyến tính các đặc trưng để tìm ra 100 trục (Principal Components) đại diện TỐT NHẤT cho những phần ảnh bị thay đổi nhiều nhất giữa các mẫu. 900 chiều bị vứt đi là những trục có mức độ biến thiên cực thấp (chứa ít thông tin hoặc chỉ là nhiễu). Do đó ảnh khôi phục lại vẫn nhìn ra hình dạng gốc.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load MNIST cỡ nhỏ
digits = load_digits()
X, y = digits.data, digits.target

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='tab10', alpha=0.6)
plt.colorbar(scatter, ticks=range(10))
plt.title('PCA on Digits (MNIST)')
plt.show()
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

```python
from sklearn.cluster import KMeans
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
```

Khi vẽ biểu đồ, ta sẽ thấy độ dốc giảm mạnh và chững lại tại điểm k=3 hoặc 4. Đó chính là khuỷu tay.

</details>
