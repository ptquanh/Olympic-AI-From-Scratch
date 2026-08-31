# Lời giải: Tree Ensembles

<details><summary><b>U-1 — Understand</b></summary>
Cấu trúc cây không thay đổi. Vì thuật toán chỉ tìm ngưỡng (threshold) phân chia dữ liệu sao cho giảm Impurity nhiều nhất. Nếu dữ liệu nhân lên 1 triệu lần, cái ngưỡng đó cũng tự động nhân lên 1 triệu (ví dụ thành `income > 1000000000`), còn lại cách chia nhánh hoàn toàn y hệt.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

```python
import time
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
import lightgbm as lgb

X, y = make_classification(n_samples=1000, n_features=20)

start = time.time()
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X, y)
print("RF Time:", time.time() - start)

start = time.time()
lgbm = lgb.LGBMClassifier(n_estimators=100)
lgbm.fit(X, y)
print("LGBM Time:", time.time() - start)

```

Kết quả phụ thuộc kích thước, độ thưa, hardware và cấu hình. Hãy báo runtime đo được trên cùng split/tham số; không kết luận LightGBM luôn nhanh hơn hoặc tốt hơn.

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>
- Hiện tượng: Accuracy trên tập Train đạt 100% (Loss gần bằng 0), nhưng trên tập Test lại cực kỳ thấp. Đây là Overfitting kinh điển của Boosting khi dùng cây quá sâu (`max_depth=15`) kết hợp với số cây lớn.
- Khi sửa `max_depth=3`: Cây nông hơn (weak learner), Overfitting giảm đáng kể, kết quả trên tập Test sẽ tăng lên.

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>
