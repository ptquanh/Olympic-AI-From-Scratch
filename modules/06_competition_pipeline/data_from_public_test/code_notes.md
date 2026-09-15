# Code Notes: Public Test — Pseudo-labeling và Test-Time Augmentation

## 🔑 Core Patterns

### Pattern 1 — Phép kiểm chứng tối thiểu

```python
import numpy as np
p = np.array([[0.1, 0.9], [0.55, 0.45]])
mask = p.max(axis=1) >= 0.85
pseudo = p.argmax(axis=1)
assert mask.tolist() == [True, False]
views = np.array([[[0.2, 0.8]], [[0.6, 0.4]]])
average = views.mean(axis=0)
assert np.allclose(average, [[0.4, 0.6]])
```

**Ghi nhớ:** Giữ validation ngoài pool nhãn giả; gộp probability theo trục view trước quyết định class.

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

| Việc cần làm      | Code                     | Link Docs                                                                                                     |
| ----------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Confidence mask   | `np.max(p, axis=1)`      | [Docs](https://numpy.org/doc/stable/reference/generated/numpy.max.html)                                       |
| Gộp góc nhìn      | `np.mean(views, axis=0)` | [Docs](https://numpy.org/doc/stable/reference/generated/numpy.mean.html)                                      |
| Self-training API | `SelfTrainingClassifier` | [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html) |

## 🏋️ Bài Luyện Code Tay

Đóng tất cả tài liệu, mở notebook trống và hẹn giờ. Chỉ mở hint khi bí; chạy assert rồi ghi lỗi sai vào nhật ký học.

| #   | Bài                                                                 | Thời gian | Hint (ẩn)                                                                                                        |
| --- | ------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------- |
| 1   | Viết chọn pseudo-label có nhánh pool rỗng trong 8 phút.             | 8 phút    | <details><summary>Hint</summary>Đối chiếu input/output contract và thêm assert trước khi mở reference.</details> |
| 2   | Gộp 3 view probability, assert shape và tổng xác suất trong 6 phút. | 10 phút   | <details><summary>Hint</summary>Đối chiếu input/output contract và thêm assert trước khi mở reference.</details> |

## 🧠 Flashcards

| Hỏi                                 | Trả lời                                                                                    |
| ----------------------------------- | ------------------------------------------------------------------------------------------ |
| Khi nào không thêm nhãn giả?        | Quy chế không cho phép, không có mẫu vượt ngưỡng, hoặc kiểm định cho thấy chất lượng giảm. |
| Validation có nằm trong pool không? | Không trong lab này; phải giữ evaluation độc lập với dữ liệu bổ sung cho training.         |
