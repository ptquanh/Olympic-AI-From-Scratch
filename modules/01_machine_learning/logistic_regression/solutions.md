# Lời giải: Logistic Regression

<details><summary><b>U-1 — Understand</b></summary>

Với **mô hình logistic tuyến tính**, MSE sau sigmoid nói chung không còn convex và gradient chứa thêm thừa số `p(1-p)`, nên gradient nhỏ khi sigmoid bão hòa. Binary cross-entropy kết hợp logit cho objective convex theo trọng số của mô hình tuyến tính và gradient `p-y` thuận lợi hơn. Tính convex này không còn được bảo đảm khi logistic output nằm sau một neural network phi tuyến.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

Dự đoán là class 1 (vì 0.4 lớn nhất). Với một vector dùng `np.argmax(probs)`; với batch `(n, classes)` dùng `axis=1`.

```python
import numpy as np
probs = np.array([[0.3, 0.4, 0.3]])
pred = np.argmax(probs, axis=1)
assert pred.tolist() == [1]

```

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

`C` là nghịch đảo độ mạnh regularization trong scikit-learn. Thông thường `C=0.01` cho norm trọng số nhỏ hơn `C=1000`, nhưng không có ngưỡng tuyệt đối `0.1` hay `10` đúng cho mọi dữ liệu. Cố định dataset/solver/max_iter và assert quan hệ đo được thay vì hard-code trị số.

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>

<details><summary><b>T-1 — Transfer</b></summary>

Tham số là `class_weight='balanced'`. scikit-learn đặt trọng số lớp tỉ lệ nghịch với tần suất `n_samples / (n_classes * count_class)`; với tỷ lệ 99:1, **tỷ số** trọng số positive/negative là 99. Đây không phải lời giải duy nhất: vẫn phải chọn metric và threshold trên validation.

```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(class_weight="balanced", random_state=42)
assert model.class_weight == "balanced"

```

**Lỗi thường gặp:** fit preprocessing/chọn threshold trên test, dùng metric sai hoặc bỏ qua failure mode.

</details>

<details><summary><b>O-1 — Olympiad</b></summary>

Đáp án là một quy trình: baseline sớm, validation chống leakage, lưu seed/config, theo dõi metric và dành thời gian tái chạy artifact cuối. Chi tiết phụ thuộc profile kỳ thi; xem `olympiad_transfer.md`.

**Lỗi thường gặp:** áp luật của kỳ thi khác, không lưu config/artifact hoặc hết timebox mà chưa chạy infer cuối.

</details>
