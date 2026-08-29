# Bài tập: Tree Ensembles

## Tầng 1: Understand

**1. Tại sao không cần Scale?**
Tree-based model chia nhánh dựa trên logic IF-ELSE (ví dụ `if income > 1000`). Theo bạn, nếu biến `income` được nhân với 1,000,000 thì cấu trúc cây có thay đổi không? Tại sao?

## Tầng 2: Implement

**1. Random Forest vs LightGBM**
Sử dụng dữ liệu `make_classification(n_samples=1000, n_features=20)`. Viết code đo thời gian huấn luyện của `RandomForestClassifier(n_estimators=100)` và `LGBMClassifier(n_estimators=100)`. Ai nhanh hơn?

## Tầng 3: Experiment

**1. Overfitting in XGBoost**
Khởi tạo `XGBClassifier(n_estimators=1000, max_depth=15, learning_rate=0.1)`. Train mô hình trên một tập dữ liệu nhỏ (100 mẫu). Sau đó đánh giá trên tập Test. Bạn thấy hiện tượng gì?
Sửa lại `max_depth=3` và so sánh.
