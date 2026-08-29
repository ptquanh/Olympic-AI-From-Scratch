# Olympiad Transfer: Logistic Regression

## 1. Nhận diện trong đề

Nếu đề bài là bài toán **Phân loại (Classification)**:

- Binary: Khách có nợ xấu không? Chó hay Mèo?
- Multiclass: Nhận diện chữ số (0-9). Phân loại loại hoa.
  Metric thường dùng: **Accuracy, F1-Score, AUC-ROC**.

## 2. Baseline tối thiểu

- **Code:** `sklearn.linear_model.LogisticRegression`
- Nếu dữ liệu không cân bằng, nhớ dùng `LogisticRegression(class_weight='balanced')`.
- Thời gian setup: 2 phút. Phải có Pipeline gồm StandardScaler + LogisticRegression.

## 3. Metric & Validation

- Validation: Luôn luôn dùng **StratifiedKFold** để đảm bảo tỷ lệ class giữa các fold là như nhau. Đừng dùng KFold thường.
- Tuyệt đối không nhìn vào Accuracy nếu data bị imbalance (90% class 0, 10% class 1). Hãy nhìn vào **F1-Macro** hoặc **AUC**.

## 4. Failure modes (Lỗi thường gặp)

1. **Quên scale dữ liệu:** LR cũng cực kỳ nhạy cảm với scale giống Linear Regression. Bắt buộc dùng `StandardScaler`. Mặc định LR trong sklearn sẽ bị báo lỗi "ConvergenceWarning: lbfgs failed to converge" nếu không scale data.
2. **Không chỉnh Threshold:** LR mặc định lấy ngưỡng 0.5. Nếu Metric của đề bài là F1-Score, bạn thường phải dùng một vòng lặp for để tìm ra ngưỡng tốt nhất (vd: 0.35, 0.42...) giúp tối đa hóa F1 trên tập Validation. Đừng mù quáng nộp thẳng threshold 0.5.

## 5. Sau baseline (Bước cải thiện)

- Đối với bảng dữ liệu (Tabular), LR chỉ là baseline để bạn đảm bảo data không có lỗi. Đối thủ thực sự là **XGBoost, LightGBM, CatBoost**. Ngay sau khi chạy xong LR, hãy code LGBM.

## 6. Phân bổ thời gian (Contest)

| Vòng           | Setup Baseline LR | Tìm ngưỡng Threshold Tối ưu  |
| -------------- | ----------------- | ---------------------------- |
| Sơ loại (4h)   | < 10 phút         | Không cần (dành sức cho XGB) |
| Chung kết (6h) | < 10 phút         | Có thể (khi blend model)     |
