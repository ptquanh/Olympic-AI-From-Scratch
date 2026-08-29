# Lời giải: SVM & KNN

<details><summary><b>Tầng 1: Understand</b></summary>

Bước tiền xử lý BẮT BUỘC là **Chuẩn hóa dữ liệu (Data Scaling)**, sử dụng `StandardScaler` hoặc `MinMaxScaler`. Điều này đưa tất cả các đặc trưng về cùng một khoảng giá trị, giúp khoảng cách Euclidean không bị thiên lệch bởi một vài biến có giá trị quá lớn.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

`SVC(kernel='linear')` sẽ có độ chính xác khoảng 50% vì nó cố gắng kẻ 1 đường thẳng xuyên qua 2 hình tròn lồng nhau, điều này là bất khả thi.
`SVC(kernel='rbf')` (Radial Basis Function) sẽ có độ chính xác 100% vì nó dùng "Kernel Trick" để đẩy dữ liệu lên số chiều cao hơn, biến nó thành có thể phân tách bằng mặt phẳng, rồi khi chiếu về 2D sẽ có hình vòng tròn bao bọc.

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

accs = []
for k in range(1, 21):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    accs.append(accuracy_score(y_test, knn.predict(X_test)))

plt.plot(range(1, 21), accs, marker='o')
plt.xlabel('K')
plt.ylabel('Accuracy')
plt.title('KNN Accuracy vs K')
plt.xticks(range(1, 21))
plt.grid()
plt.show()
```

Khi $k=1$, mô hình dễ bị nhiễu. Khi $k$ lớn dần, mô hình ổn định hơn, nhưng nếu $k$ quá lớn (gần bằng số lượng tập Train), mô hình lại bị thiên lệch về class đa số.

</details>
