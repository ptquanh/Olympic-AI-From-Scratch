# Code Notes: Metrics & Validation

## 🔑 Core Patterns

### Pattern 1: Báo cáo phân loại (Classification Report)

```python
from sklearn.metrics import classification_report

# Rất hữu ích để xem nhanh toàn cảnh
print(classification_report(y_true, y_pred))

```

**Ghi nhớ:** Luôn dùng cái này khi làm bài tập phân loại. Cột `support` báo cho bạn biết số lượng dữ liệu mỗi class (giúp phát hiện imbalance).

### Pattern 2: ROC-AUC

```python
from sklearn.metrics import roc_auc_score

# CHÚ Ý: Phải truyền vào y_prob (xác suất), không phải y_pred (0,1)
y_prob = model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_prob)
print(f'AUC: {auc:.4f}')

```

### Pattern 3: K-Fold an toàn với Cross_val_score

```python
from sklearn.model_selection import StratifiedKFold, cross_val_score

# StratifiedKFold đảm bảo tỷ lệ class giữa các fold là như nhau
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf, scoring='f1_macro')

```

**Ghi nhớ:** Luôn set `shuffle=True, random_state=42`. Nếu dữ liệu mất cân bằng, bắt buộc dùng `StratifiedKFold`.

## 📋 API Cheat Sheet

| Việc cần làm      | Code                                                | Link Docs                                                                                                           |
| ----------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Chia Train/Test   | `train_test_split(X, y, test_size=0.2, stratify=y)` | [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) |
| Đếm số lượng nhãn | `np.unique(y, return_counts=True)`                  |                                                                                                                     |

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                               | Thời gian | Hint (ẩn)                                                 |
| --- | ----------------------------------------------------------------- | --------- | --------------------------------------------------------- |
| 1   | Viết hàm F1-Score từ TP, TN, FP, FN                               | 3 phút    | `p = TP/(TP+FP); r = TP/(TP+FN); 2*p*r/(p+r)`             |
| 2   | Import StratifiedKFold và cross_val_score, chạy một pipeline mẫu. | 5 phút    | `cross_val_score(model, X, y, cv=skf, scoring='roc_auc')` |

## 🧠 Flashcards

| Hỏi                                                 | Trả lời                                                                          |
| --------------------------------------------------- | -------------------------------------------------------------------------------- |
| Stratify trong `train_test_split` có tác dụng gì?   | Đảm bảo tỷ lệ các class trong tập Train và Test giống như trong tập dữ liệu gốc. |
| Nếu AUC = 0.5 thì mô hình của bạn hoạt động ra sao? | Tương đương với đoán mò (Random guess).                                          |
