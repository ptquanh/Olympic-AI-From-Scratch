# Lời giải: Unsupervised Learning

<details><summary><b>U-1 — Understand</b></summary>
Không thể phân loại được. Vì K-Means gom cụm dựa trên khoảng cách hình học tới tâm (Centroid). Dữ liệu dạng vòng tròn đồng tâm sẽ khiến K-Means bị nhầm lẫn và chia dữ liệu thành 2 nửa (trái và phải, hoặc trên và dưới). Giải pháp là dùng thuật toán dựa trên mật độ như DBSCAN.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print(X_pca.shape) # Output: (150, 2)

```

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>
DBSCAN làm tốt hơn hẳn. K-Means sẽ cắt 2 vầng trăng thành 2 khối hình cầu (phân loại sai bét). DBSCAN gom theo mật độ điểm (density), nên nó sẽ luồn lách theo hình vầng trăng khuyết và nhận diện hoàn hảo 2 cụm này.

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>
