# Code Notes: Logistic Regression

## 🔑 Core Patterns

### Pattern 1: Scikit-learn Logistic Regression

```python
from sklearn.linear_model import LogisticRegression

# 1. Khởi tạo (Mặc định nó dùng L2 Regularization, tham số là C)
# C = 1/alpha (C càng nhỏ = Regularization càng lớn)
model = LogisticRegression(C=1.0)

# 2. Huấn luyện
model.fit(X_train, y_train)

# 3. Dự đoán Nhãn (0 hoặc 1)
y_pred = model.predict(X_test)

# 4. Dự đoán Xác suất (Tỷ lệ %)
y_prob = model.predict_proba(X_test) # Trả về mảng 2D: [prob_class_0, prob_class_1]
```

**Ghi nhớ:** Hàm `predict_proba` rất quan trọng khi bạn muốn tự set ngưỡng (threshold) thay vì dùng 0.5 mặc định.

### Pattern 2: Đổi Threshold

```python
y_prob_positive = model.predict_proba(X_test)[:, 1] # Lấy cột xác suất của class 1
custom_y_pred = (y_prob_positive >= 0.8).astype(int) # Chỉ tin tưởng nếu xác suất >= 80%
```

## 📋 API Cheat Sheet

| Việc cần làm  | Code                             | Link Docs                                                                                      |
| ------------- | -------------------------------- | ---------------------------------------------------------------------------------------------- |
| Tính Accuracy | `accuracy_score(y_true, y_pred)` | [sklearn metrics](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics) |
| Lấy xác suất  | `model.predict_proba(X)[:, 1]`   |                                                                                                |

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                                          | Thời gian | Hint (ẩn)                |
| --- | ---------------------------------------------------------------------------- | --------- | ------------------------ |
| 1   | Viết hàm Sigmoid bằng NumPy                                                  | 2 phút    | `1 / (1 + np.exp(-x))`   |
| 2   | Khởi tạo mô hình Logistic Regression, fit và lấy mảng xác suất (của class 1) | 3 phút    | `predict_proba(X)[:, 1]` |

## 🧠 Flashcards

| Hỏi                                                                                                    | Trả lời                                                                                     |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| Tham số `C` trong LogisticRegression của Sklearn có ý nghĩa gì?                                        | Tỷ lệ nghịch của Regularization. `C` nhỏ -> Phạt mạnh (chống Overfit). `C` lớn -> Phạt nhẹ. |
| Nếu ta muốn hạn chế tối đa việc đoán lầm (chỉ đoán khi rất chắc chắn), ta nên tăng hay giảm threshold? | Tăng threshold (vd: 0.8 hoặc 0.9).                                                          |
