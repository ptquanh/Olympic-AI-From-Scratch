# Code Notes: Ensembling — Averaging, Blending và Stacking

## 🔑 Core Patterns

### Pattern 1 — Phép kiểm chứng tối thiểu

```python
import numpy as np
p_a = np.array([[0.2, 0.8], [0.9, 0.1]])
p_b = np.array([[0.6, 0.4], [0.5, 0.5]])
assert p_a.shape == p_b.shape
p = 0.25 * p_a + 0.75 * p_b
assert np.allclose(p.sum(axis=1), 1)
labels = (p[:, 1] >= 0.5).astype(int)
assert labels.tolist() == [1, 0]
```

**Ghi nhớ:** Căn hàng bằng ID, căn cột bằng classes_; học mọi trọng số trên dữ liệu được phép dùng cho model selection.

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

| Việc cần làm        | Code                 | Link Docs                                                                                          |
| ------------------- | -------------------- | -------------------------------------------------------------------------------------------------- |
| Clone model         | `clone(estimator)`   | [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html)                  |
| Stacking tham chiếu | `StackingClassifier` | [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html) |
| Chấm probability    | `log_loss(y, p)`     | [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html)            |

## 🏋️ Bài Luyện Code Tay

Đóng tất cả tài liệu, mở notebook trống và hẹn giờ. Chỉ mở hint khi bí; chạy assert rồi ghi lỗi sai vào nhật ký học.

| #   | Bài                                                                | Thời gian | Hint (ẩn)                                                                                                        |
| --- | ------------------------------------------------------------------ | --------- | ---------------------------------------------------------------------------------------------------------------- |
| 1   | Gộp 2 file probability sau join ID và reorder class trong 10 phút. | 8 phút    | <details><summary>Hint</summary>Đối chiếu input/output contract và thêm assert trước khi mở reference.</details> |
| 2   | Tạo OOF matrix 2 cột có coverage assert trong 15 phút.             | 10 phút   | <details><summary>Hint</summary>Đối chiếu input/output contract và thêm assert trước khi mở reference.</details> |

## 🧠 Flashcards

| Hỏi                           | Trả lời                                                                            |
| ----------------------------- | ---------------------------------------------------------------------------------- |
| Khi nào giữ single model?     | Khi ensemble không cải thiện validation đủ đáng tin hoặc vượt ngân sách inference. |
| Blending khác stacking ở đâu? | Blending học trên hold-out; stacking học trên OOF của các base models.             |
