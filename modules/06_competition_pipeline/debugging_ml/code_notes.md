# Code Notes: Debugging ML — Tìm lỗi bằng kiểm chứng nhỏ

## 🔑 Core Patterns

### Pattern 1 — Phép kiểm chứng tối thiểu

```python
import numpy as np
X = np.array([[-1.0], [1.0]])
y = np.array([0.0, 1.0])
w = np.zeros(1)
p = 1 / (1 + np.exp(-(X @ w)))
gradient = X.T @ (p - y) / len(y)
assert np.allclose(gradient, [-0.5])
w -= 0.1 * gradient
assert np.allclose(w, [0.05])
```

**Ghi nhớ:** Shape trước, loss ban đầu sau, gradient check rồi tiny-overfit; thay một giả thuyết mỗi lần.

### Pattern 2 — Submission contract

```python
import numpy as np
import pandas as pd
ids = np.array(['test_0', 'test_1'])
predictions = np.array([1, 0])
submission = pd.DataFrame({'id': ids, 'label': predictions})
assert submission.columns.tolist() == ['id', 'label']
assert submission['id'].is_unique
assert submission['id'].tolist() == ids.tolist()
assert submission['label'].isin([0, 1]).all()
```

**Ghi nhớ:** Kiểm tra đúng hàng và label mapping trước nộp; score không phát hiện được CSV lệch ID. Contract thực tế phải lấy từ đề.

## 📋 API Cheat Sheet

| Việc cần làm       | Code                        | Link Docs                                                                                   |
| ------------------ | --------------------------- | ------------------------------------------------------------------------------------------- |
| BCE ổn định        | `np.logaddexp(0, logits)`   | [Docs](https://numpy.org/doc/stable/reference/generated/numpy.logaddexp.html)               |
| Đo sai số          | `np.linalg.norm(g - g_num)` | [Docs](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html)             |
| Finite differences | `scipy.optimize.check_grad` | [Docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.check_grad.html) |

## 🏋️ Bài Luyện Code Tay

Đóng tất cả tài liệu, mở notebook trống và hẹn giờ. Chỉ mở hint khi bí; chạy assert rồi ghi lỗi sai vào nhật ký học.

| #   | Bài                                                               | Thời gian | Hint (ẩn)                                                                                                        |
| --- | ----------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------- |
| 1   | Code centered finite difference cho vector 3 chiều trong 12 phút. | 8 phút    | <details><summary>Hint</summary>Đối chiếu input/output contract và thêm assert trước khi mở reference.</details> |
| 2   | Viết assert bắt y shape (n,1) và NaN input trong 8 phút.          | 10 phút   | <details><summary>Hint</summary>Đối chiếu input/output contract và thêm assert trước khi mở reference.</details> |

## 🧠 Flashcards

| Hỏi                            | Trả lời                                                                |
| ------------------------------ | ---------------------------------------------------------------------- |
| Vì sao dùng float64 khi check? | Giảm sai số làm tròn trong hiệu hai loss gần nhau.                     |
| Nếu gradcheck fail ở ReLU=0?   | Đó là điểm không khả vi; chọn điểm trơn hoặc kiểm tra nhánh hoạt động. |
