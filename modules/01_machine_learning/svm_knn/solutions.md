# Lời giải: SVM & KNN

<details><summary><b>Tầng 1: Understand</b></summary>
Cả hai đều nhạy cảm với việc Scale dữ liệu (đều dùng khoảng cách hình học), nên BẮT BUỘC phải dùng StandardScaler trước.
Tuy nhiên, KNN là "Lazy learning", nó không hề có quá trình "học" (Loss, Gradient, Weight). Nó chỉ đơn giản là nhớ toàn bộ tập Train vào RAM, rồi lúc Predict thì mang ra đo khoảng cách. Do đó KNN predict rất chậm nếu dữ liệu lớn.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
from sklearn.datasets import make_circles
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

X, y = make_circles(n_samples=100, noise=0.1, factor=0.1)

svc_linear = SVC(kernel='linear').fit(X, y)
print("Linear Kernel:", accuracy_score(y, svc_linear.predict(X)))

svc_rbf = SVC(kernel='rbf').fit(X, y)
print("RBF Kernel:", accuracy_score(y, svc_rbf.predict(X)))
```

Kết quả: Kernel `linear` sẽ thất bại nặng nề (khoảng 50%). Kernel `rbf` (phóng dữ liệu lên chiều không gian vô hạn) sẽ dễ dàng tìm được đường bao vòng tròn (100%).

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>
- Khi K = 1: Mô hình tin tưởng tuyệt đối vào người hàng xóm gần nhất (Overfitting kinh khủng). Nếu có nhiễu (noise) thì sẽ phân loại sai ngay.
- Khi K = N (Tổng số data): Mô hình sẽ bỏ phiếu theo số đông, và luôn luôn dự đoán ra Class có số lượng áp đảo nhất trong tập dữ liệu (Underfitting).
</details>
