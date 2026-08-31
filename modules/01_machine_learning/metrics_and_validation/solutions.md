# Lời giải: Metrics & Validation

<details><summary><b>U-1 — Understand</b></summary>

Nếu báo động giả nhiều: Recall sẽ tăng (ít bỏ sót bệnh nhân), nhưng Precision sẽ giảm mạnh (phần lớn những ca báo bệnh đều là khỏe mạnh). Sự đánh đổi này là tất yếu, tùy theo bài toán (vd: y tế thì ưu tiên Recall, lọc spam thì ưu tiên Precision) mà ta chọn threshold phù hợp.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

- Precision = 50 / (50 + 20) = 50/70 ≈ 0.714
- Recall = 50 / (50 + 30) = 50/80 = 0.625
- F1 = `2 * (0.714 * 0.625) / (0.714 + 0.625) ≈ 0.667`

```python
precision = 50 / (50 + 20)
recall = 50 / (50 + 30)
f1 = 2 * precision * recall / (precision + recall)
assert abs(f1 - 2/3) < 1e-12

```

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

Nếu tạo `y = [0] * 990 + [1] * 10` rồi dùng `KFold(n_splits=5, shuffle=False)`, bốn test fold đầu không có positive và fold cuối có cả 10. Nếu bật shuffle, phân bố không còn tất định nhưng vẫn có thể lệch. `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` giữ mỗi test fold có 2 positive trong ví dụ này.

```python
import numpy as np
from sklearn.model_selection import StratifiedKFold
y = np.array([0] * 990 + [1] * 10)
X = np.zeros((len(y), 1))
counts = [int(y[test].sum()) for _, test in StratifiedKFold(5, shuffle=True, random_state=42).split(X, y)]
assert counts == [2, 2, 2, 2, 2]

```

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>

<details><summary><b>T-1 — Transfer</b></summary>

Sai lầm ở chỗ: `fit_transform` trên toàn bộ X nghĩa là tham số Mean và Std của tập Test ĐÃ BỊ DÙNG để scale tập Train. Tập Test không còn "ẩn" với mô hình nữa.
Cách làm đúng:

1. Chia Train/Test trước.
2. `scaler.fit(X_train)`
3. `X_train_scaled = scaler.transform(X_train)`
4. `X_test_scaled = scaler.transform(X_test)`
   Hoặc an toàn nhất là dùng `sklearn.pipeline.make_pipeline(StandardScaler(), LogisticRegression())`.

Threshold hoặc model selection cũng chỉ dùng train/validation; test/private data được giữ kín tới lần đánh giá cuối.

**Lỗi thường gặp:** fit preprocessing/chọn threshold trên test, dùng metric sai hoặc bỏ qua failure mode.

</details>

<details><summary><b>O-1 — Olympiad</b></summary>

Đáp án là một quy trình: baseline sớm, validation chống leakage, lưu seed/config, theo dõi metric và dành thời gian tái chạy artifact cuối. Chi tiết phụ thuộc profile kỳ thi; xem `olympiad_transfer.md`.

**Lỗi thường gặp:** áp luật của kỳ thi khác, không lưu config/artifact hoặc hết timebox mà chưa chạy infer cuối.

</details>
