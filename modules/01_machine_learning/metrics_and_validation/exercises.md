# Bài tập: Metrics & Validation

## Tầng 1: Understand

**1. Sự đánh đổi (Trade-off)**
Nếu bạn cố tình báo động giả thật nhiều (tức là ngưỡng threshold cực thấp, hơi nghi ngờ là cho Bệnh luôn), điều gì sẽ xảy ra với Precision và Recall? Tại sao ta không thể có cả 2 cùng đạt 100% trong hầu hết các bài toán thực tế?

## Tầng 2: Implement

**1. Tính F1-Score**
Cho Confusion Matrix:

- TP = 50
- TN = 900
- FP = 20
- FN = 30
  Hãy tính bằng tay (hoặc máy tính bỏ túi) giá trị của Precision, Recall và F1-Score.

## Tầng 3: Experiment

**1. Lợi ích của StratifiedKFold**
Tạo dữ liệu mất cân bằng cực độ: 990 mẫu class 0, 10 mẫu class 1.
Chạy `KFold` (không stratified) với `n_splits=5`. Print ra số lượng mẫu class 1 trong từng fold (tập Test của từng fold). Bạn sẽ nhận thấy có fold KHÔNG CÓ BẤT KỲ MẪU CLASS 1 NÀO.
Sau đó đổi sang `StratifiedKFold` và quan sát sự khác biệt.

## Tầng 4: Transfer

**1. Data Leakage (Cực kỳ quan trọng)**
Đoạn code sau mô phỏng một sai lầm chết người mà 90% người mới học mắc phải:

```python
# Scale toàn bộ dữ liệu trước
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Rồi mới chia Train/Test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)
```

Tại sao cách làm này bị coi là rò rỉ dữ liệu (Data Leakage)? Cách làm đúng là gì?

## Tầng 5: Olympiad

_(Xem `olympiad_transfer.md`)_
