# Code Notes: Tree Ensembles

> ⚠️ **Online/optional appendix:** một số snippet bên dưới cần package hoặc model cache bổ sung và có thể tải dữ liệu ở lần chạy đầu. Chúng không competition-safe nếu profile chính thức không cho phép rõ ràng. Notebook chính của chương luôn có đường chạy fast/offline và không tự cài/tải.

## 🔑 Core Patterns

### Pattern 1: LightGBM cơ bản

```python
import lightgbm as lgb
from sklearn.metrics import accuracy_score

# 1. Khởi tạo
model = lgb.LGBMClassifier(n_estimators=100, learning_rate=0.1, random_state=42)

# 2. Fit
model.fit(X_train, y_train)

# 3. Predict
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

```

### Pattern 2: Xem mức độ quan trọng của Features (Feature Importance)

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tạo DataFrame chứa feature importances
importance_df = pd.DataFrame({
    'Feature': X_train.columns,
    'Importance': model.feature_importances_
}).sort_values(by='Importance', ascending=False)

sns.barplot(x='Importance', y='Feature', data=importance_df.head(10))
plt.title('Top 10 Quan Trọng Nhất')
plt.show()

```

**Ghi nhớ:** Plot Feature Importance là bước cực kỳ quan trọng trong thi đấu để biết cột dữ liệu nào đóng góp nhiều nhất, từ đó tập trung Feature Engineering vào cột đó.

## 📋 API Cheat Sheet

| Việc cần làm           | Code                                                   | Link Docs                                                                                                 |
| ---------------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| Khởi tạo XGBoost       | `import xgboost as xgb; model = xgb.XGBClassifier()`   | [xgboost](https://xgboost.readthedocs.io/en/stable/python/python_api.html)                                |
| Khởi tạo Random Forest | `from sklearn.ensemble import RandomForestClassifier`  | [sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) |
| Khởi tạo LightGBM      | `import lightgbm as lgb; model = lgb.LGBMClassifier()` | [lightgbm](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMClassifier.html)              |

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                                     | Thời gian | Hint (ẩn)                                                  |
| --- | ----------------------------------------------------------------------- | --------- | ---------------------------------------------------------- |
| 1   | Viết đoạn mã vẽ biểu đồ Feature Importance của `model` trên matplotlib. | 5 phút    | Dùng `model.feature_importances_`                          |
| 2   | Khởi tạo mô hình LightGBM với 200 cây và learning rate 0.05             | 2 phút    | `lgb.LGBMClassifier(n_estimators=200, learning_rate=0.05)` |

## 🧠 Flashcards

| Hỏi                                                               | Trả lời                                                                            |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Điểm yếu lớn nhất của Decision Tree là gì?                        | Dễ bị Overfitting (Học thuộc lòng tập dữ liệu).                                    |
| Bagging (như Random Forest) giúp cải thiện mô hình bằng cách nào? | Giảm phương sai (Variance) bằng cách lấy trung bình dự đoán của nhiều cây độc lập. |
