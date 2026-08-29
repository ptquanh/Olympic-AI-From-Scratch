# Lời giải: Unsupervised Learning

<details><summary><b>Tầng 1: Understand</b></summary>
Không thể phân loại được. Vì K-Means gom cụm dựa trên khoảng cách hình học tới tâm (Centroid). Dữ liệu dạng vòng tròn đồng tâm sẽ khiến K-Means bị nhầm lẫn và chia dữ liệu thành 2 nửa (trái và phải, hoặc trên và dưới). Giải pháp là dùng thuật toán dựa trên mật độ như DBSCAN.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print(X_pca.shape) # Output: (150, 2)
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>
DBSCAN làm tốt hơn hẳn. K-Means sẽ cắt 2 vầng trăng thành 2 khối hình cầu (phân loại sai bét). DBSCAN gom theo mật độ điểm (density), nên nó sẽ luồn lách theo hình vầng trăng khuyết và nhận diện hoàn hảo 2 cụm này.
</details>
