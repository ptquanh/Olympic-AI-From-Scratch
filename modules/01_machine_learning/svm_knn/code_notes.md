# Code Notes: SVM & KNN

## 🔑 Core Patterns

### Pattern 1: Support Vector Machine

```python
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# SVM BẮT BUỘC phải scale dữ liệu, ta dùng pipeline cho an toàn
model = make_pipeline(StandardScaler(), SVC(kernel='rbf', C=1.0))

# Fit
model.fit(X_train, y_train)
```

### Pattern 2: K-Nearest Neighbors

```python
from sklearn.neighbors import KNeighborsClassifier

# KNN cũng cần scale vì nó tính khoảng cách
knn = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
knn.fit(X_train, y_train)
```

## 📋 API Cheat Sheet

| Việc cần làm | Code                                     | Link Docs                                                                                            |
| ------------ | ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Khởi tạo SVM | `SVC(kernel='linear', C=1.0)`            | [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)                        |
| Khởi tạo KNN | `KNeighborsClassifier(n_neighbors=5)`    | [KNN](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) |
| Pipeline     | `make_pipeline(StandardScaler(), SVC())` | [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html)    |

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                                        | Thời gian | Hint (ẩn)                                |
| --- | -------------------------------------------------------------------------- | --------- | ---------------------------------------- |
| 1   | Khởi tạo mô hình KNN phân loại với 3 hàng xóm.                             | 2 phút    | `KNeighborsClassifier(n_neighbors=3)`    |
| 2   | Viết mã chuẩn hóa dữ liệu bằng StandardScaler rồi fit SVM (dùng Pipeline). | 4 phút    | `make_pipeline(StandardScaler(), SVC())` |

## 🧠 Flashcards

| Hỏi                                                | Trả lời                                                                                                        |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Support Vectors trong thuật toán SVM là gì?        | Là những điểm dữ liệu nằm sát nhất với đường phân cách. Mô hình SVM được định hình HOÀN TOÀN bởi các điểm này. |
| Nếu K trong KNN là số chẵn, điều gì có thể xảy ra? | Có thể xảy ra trường hợp hòa (vd: 2 phiếu lớp A, 2 phiếu lớp B). K nên là số lẻ.                               |
