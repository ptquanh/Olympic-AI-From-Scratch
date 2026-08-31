# Lời giải: SVM & KNN

<details><summary><b>U-1 — Understand</b></summary>
KNN và SVM dùng RBF/poly thường nhạy với scale vì khoảng cách/dot product bị feature biên độ lớn chi phối. StandardScaler trong pipeline là baseline tốt cho feature liên tục, nhưng không phải luật tuyệt đối (ví dụ dữ liệu đã cùng scale hoặc feature nhị phân/sparse cần scaler phù hợp).
Tuy nhiên, KNN là "Lazy learning", nó không hề có quá trình "học" (Loss, Gradient, Weight). Nó chỉ đơn giản là nhớ toàn bộ tập Train vào RAM, rồi lúc Predict thì mang ra đo khoảng cách. Do đó KNN predict rất chậm nếu dữ liệu lớn.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

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

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>
- Khi K = 1: Mô hình tin tưởng tuyệt đối vào người hàng xóm gần nhất (Overfitting kinh khủng). Nếu có nhiễu (noise) thì sẽ phân loại sai ngay.
- Khi K = N (Tổng số data): Mô hình sẽ bỏ phiếu theo số đông, và luôn luôn dự đoán ra Class có số lượng áp đảo nhất trong tập dữ liệu (Underfitting).

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>
