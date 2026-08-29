# Olympiad Transfer: Linear Regression

## 1. Nhận diện trong đề

Nếu đề bài là bài toán **Dự đoán một giá trị thực liên tục** (vd: Giá nhà, số lượng sản phẩm bán được, tuổi thọ...). Metric đánh giá là **MSE, RMSE, MAE**.
Linear Regression (thường là Ridge) thường được dùng làm **Baseline đầu tiên** trước khi thử các mô hình phức tạp.

## 2. Baseline tối thiểu

- **Code:** `sklearn.linear_model.Ridge`
- **Thời gian code:** 2 phút.
- Gần như luôn được nộp đầu tiên để làm mốc so sánh (Benchmark). Nếu mô hình Deep Learning của bạn chạy kém hơn cả Ridge Regression, chứng tỏ code DL có lỗi hoặc data preprocessing bị sai.

## 3. Metric & Validation

Đề thi Regression thường dùng **RMSE** (Root Mean Squared Error) vì nó phạt các sai số lớn mạnh hơn MAE, và cùng đơn vị với nhãn Y (dễ diễn giải).

- Validation: Dùng `KFold` (không dùng `StratifiedKFold` vì Y là biến liên tục).

## 4. Failure modes (Lỗi thường gặp)

1. **Quên scale dữ liệu:** Linear Regression / Ridge cực kỳ nhạy cảm với độ lớn của biến (ví dụ: biến Diện Tích tính bằng mét vuông (trăm), biến Tiền tính bằng tỷ). **Phải dùng StandardScaler** trước khi đưa vào mô hình.
2. **Nhiễu (Outliers):** Nếu có 1 căn nhà 10m2 nhưng giá 1000 tỷ (sai dữ liệu), MSE của LR sẽ bị kéo lệch kinh khủng. Cần loại bỏ outlier.

## 5. Sau baseline (Bước cải thiện)

1. Bước 1: Log-transform cho biến Y (nếu biến Y có phân phối lệch (skewed), vd thu nhập, giá nhà). Predict xong phải `np.exp` ngược lại.
2. Bước 2: Bỏ LR, chuyển sang Tree-based models (XGBoost, LightGBM) vì Linear Regression không học được tương tác phi tuyến nếu ta không tự tạo tính năng (Feature Engineering).

## 6. Phân bổ thời gian (Contest)

| Vòng           | Setup Baseline LR |
| -------------- | ----------------- |
| Sơ loại (4h)   | < 10 phút         |
| Chung kết (6h) | < 10 phút         |
