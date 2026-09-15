# Code Notes: Validation — Đo đúng khả năng tổng quát hóa

## 🔑 Core Patterns

### Pattern 1 — Phép kiểm chứng tối thiểu

```python
import numpy as np
from sklearn.model_selection import GroupKFold
groups = np.repeat(np.arange(6), 2)
coverage = np.zeros(len(groups), dtype=int)
for tr, va in GroupKFold(3).split(np.zeros((12, 1)), groups=groups):
    assert set(groups[tr]).isdisjoint(groups[va])
    coverage[va] += 1
assert np.all(coverage == 1)
```

**Ghi nhớ:** Split đúng đơn vị độc lập trước, sau đó fit toàn bộ preprocessing trong mỗi fold.

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

| Việc cần làm   | Code                                                | Link Docs                                                                                              |
| -------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Tách group     | `GroupKFold(n_splits=3)`                            | [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html)      |
| Giữ tỷ lệ nhãn | `StratifiedKFold(3, shuffle=True, random_state=42)` | [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html) |
| Tách thời gian | `TimeSeriesSplit(n_splits=3, gap=1)`                | [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) |

## 🏋️ Bài Luyện Code Tay

Đóng tất cả tài liệu, mở notebook trống và hẹn giờ. Chỉ mở hint khi bí; chạy assert rồi ghi lỗi sai vào nhật ký học.

| #   | Bài                                                               | Thời gian | Hint (ẩn)                                                                                                        |
| --- | ----------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------- |
| 1   | Tạo group split và assert không giao group trong 8 phút.          | 8 phút    | <details><summary>Hint</summary>Đối chiếu input/output contract và thêm assert trước khi mở reference.</details> |
| 2   | Viết OOF coverage rồi cố ý gán một fold hai lần để phát hiện lỗi. | 10 phút   | <details><summary>Hint</summary>Đối chiếu input/output contract và thêm assert trước khi mở reference.</details> |

## 🧠 Flashcards

| Hỏi                              | Trả lời                                                                                   |
| -------------------------------- | ----------------------------------------------------------------------------------------- |
| Khi nào chọn time split?         | Khi mục tiêu dự đoán tương lai; kiểm tra cả cửa sổ tạo feature và thời gian label có sẵn. |
| Vì sao OOF F1 khác mean fold F1? | F1 không tuyến tính và các fold có thể có kích thước/phân bố khác nhau.                   |
