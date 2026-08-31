# Bài tập: Tree Ensembles

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Tại sao không cần Scale?**
Tree-based model chia nhánh dựa trên logic IF-ELSE (ví dụ `if income > 1000`). Theo bạn, nếu biến `income` được nhân với 1,000,000 thì cấu trúc cây có thay đổi không? Tại sao?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Random Forest vs LightGBM**
Sử dụng dữ liệu `make_classification(n_samples=1000, n_features=20)`. Viết code đo thời gian huấn luyện của `RandomForestClassifier(n_estimators=100)` và `LGBMClassifier(n_estimators=100)`. Ai nhanh hơn?

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Overfitting in XGBoost**
Khởi tạo `XGBClassifier(n_estimators=1000, max_depth=15, learning_rate=0.1)`. Train mô hình trên một tập dữ liệu nhỏ (100 mẫu). Sau đó đánh giá trên tập Test. Bạn thấy hiện tượng gì?
Sửa lại `max_depth=3` và so sánh.

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
