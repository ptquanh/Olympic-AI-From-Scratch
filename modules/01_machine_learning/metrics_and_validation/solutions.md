# Lời giải: Metrics & Validation

<details><summary><b>Tầng 1: Understand</b></summary>

Nếu báo động giả nhiều: Recall sẽ tăng (ít bỏ sót bệnh nhân), nhưng Precision sẽ giảm mạnh (phần lớn những ca báo bệnh đều là khỏe mạnh). Sự đánh đổi này là tất yếu, tùy theo bài toán (vd: y tế thì ưu tiên Recall, lọc spam thì ưu tiên Precision) mà ta chọn threshold phù hợp.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

- Precision = 50 / (50 + 20) = 50/70 ≈ 0.714
- Recall = 50 / (50 + 30) = 50/80 = 0.625
- F1 = 2 _ (0.714 _ 0.625) / (0.714 + 0.625) ≈ 0.666
</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

Với `KFold` ngẫu nhiên, 10 mẫu class 1 có thể rơi hết vào 2-3 folds, khiến các fold còn lại bằng 0, khi tính AUC/F1 sẽ bị lỗi `UndefinedMetricWarning`. `StratifiedKFold` sẽ chia đều mỗi fold có đúng 2 mẫu class 1.

</details>

<details><summary><b>Tầng 4: Transfer</b></summary>

Sai lầm ở chỗ: `fit_transform` trên toàn bộ X nghĩa là tham số Mean và Std của tập Test ĐÃ BỊ DÙNG để scale tập Train. Tập Test không còn "ẩn" với mô hình nữa.
Cách làm đúng:

1. Chia Train/Test trước.
2. `scaler.fit(X_train)`
3. `X_train_scaled = scaler.transform(X_train)`
4. `X_test_scaled = scaler.transform(X_test)`
Hoặc an toàn nhất là dùng `sklearn.pipeline.make_pipeline(StandardScaler(), LogisticRegression())`.
</details>
