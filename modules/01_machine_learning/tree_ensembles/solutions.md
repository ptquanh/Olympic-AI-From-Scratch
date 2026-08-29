# Lời giải: Tree Ensembles

<details><summary><b>Tầng 1: Understand</b></summary>
Cấu trúc cây không thay đổi. Vì thuật toán chỉ tìm ngưỡng (threshold) phân chia dữ liệu sao cho giảm Impurity nhiều nhất. Nếu dữ liệu nhân lên 1 triệu lần, cái ngưỡng đó cũng tự động nhân lên 1 triệu (ví dụ thành `income > 1000000000`), còn lại cách chia nhánh hoàn toàn y hệt.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

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

Kết quả: LightGBM luôn nhanh hơn rất nhiều (thường nhanh gấp 5-10 lần).

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>
- Hiện tượng: Accuracy trên tập Train đạt 100% (Loss gần bằng 0), nhưng trên tập Test lại cực kỳ thấp. Đây là Overfitting kinh điển của Boosting khi dùng cây quá sâu (`max_depth=15`) kết hợp với số cây lớn.
- Khi sửa `max_depth=3`: Cây nông hơn (weak learner), Overfitting giảm đáng kể, kết quả trên tập Test sẽ tăng lên.
</details>
