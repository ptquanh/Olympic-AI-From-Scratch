# Bài tập: Metrics & Validation

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Sự đánh đổi (Trade-off)**
Nếu bạn cố tình báo động giả thật nhiều (tức là ngưỡng threshold cực thấp, hơi nghi ngờ là cho Bệnh luôn), điều gì sẽ xảy ra với Precision và Recall? Tại sao ta không thể có cả 2 cùng đạt 100% trong hầu hết các bài toán thực tế?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Tính F1-Score**
Cho Confusion Matrix:

- TP = 50
- TN = 900
- FP = 20
- FN = 30
  Hãy tính bằng tay (hoặc máy tính bỏ túi) giá trị của Precision, Recall và F1-Score.

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Lợi ích của StratifiedKFold**
Tạo dữ liệu mất cân bằng cực độ: 990 mẫu class 0, 10 mẫu class 1.
Chạy `KFold` (không stratified) với `n_splits=5`. Print ra số lượng mẫu class 1 trong từng fold (tập Test của từng fold). Bạn sẽ nhận thấy có fold KHÔNG CÓ BẤT KỲ MẪU CLASS 1 NÀO.
Sau đó đổi sang `StratifiedKFold` và quan sát sự khác biệt.

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.

## T-1 — Transfer

**Learning outcome:** Chuyển kỹ thuật sang dữ liệu mới mà không leakage, dùng metric và failure mode phù hợp.

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

**Kết quả mong đợi:** Pipeline chạy trên dữ liệu/bối cảnh mới, metric phù hợp và phân tích ít nhất một failure mode.

## O-1 — Olympiad

**Learning outcome:** Dựng baseline theo đúng competition profile, timebox và artifact nộp có thể chạy lại.

_(Xem `olympiad_transfer.md`)_

**Kết quả mong đợi:** Baseline tái lập được trong timebox, validation đúng, metric và checklist file cần nộp.
