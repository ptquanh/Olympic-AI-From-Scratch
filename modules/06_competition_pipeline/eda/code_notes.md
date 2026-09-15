# Code Notes: EDA — Khám phá dữ liệu trước baseline

## 🔑 Core Patterns

### Pattern 1 — Phép kiểm chứng tối thiểu

```python
import pandas as pd
df = pd.DataFrame({'patient': ['A', 'A', 'B'], 'age': [20, 20, None]})
missing = df.isna().mean()
duplicates = df.duplicated().sum()
assert duplicates == 1
assert missing['age'] == 1 / 3
```

**Ghi nhớ:** Chọn khóa duplicate theo ý nghĩa bản ghi; missing rate là tỷ lệ ô thiếu, không phải số dòng thiếu bất kỳ cột nào.

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

| Việc cần làm | Code                             | Link Docs                                                                             |
| ------------ | -------------------------------- | ------------------------------------------------------------------------------------- |
| Missing mask | `df.isna()`                      | [Docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html)       |
| Duplicate    | `df.duplicated(subset=keys)`     | [Docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html) |
| Đếm class    | `y.value_counts(normalize=True)` | [Docs](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html)  |

## 🏋️ Bài Luyện Code Tay

Đóng tất cả tài liệu, mở notebook trống và hẹn giờ. Chỉ mở hint khi bí; chạy assert rồi ghi lỗi sai vào nhật ký học.

| #   | Bài                                                          | Thời gian | Hint (ẩn)                                                                                                        |
| --- | ------------------------------------------------------------ | --------- | ---------------------------------------------------------------------------------------------------------------- |
| 1   | Tạo báo cáo missing và duplicate có assert trên bảng 4 dòng. | 8 phút    | <details><summary>Hint</summary>Đối chiếu input/output contract và thêm assert trước khi mở reference.</details> |
| 2   | Viết kiểm tra ID và số dòng của submission rồi đọc CSV lại.  | 10 phút   | <details><summary>Hint</summary>Đối chiếu input/output contract và thêm assert trước khi mở reference.</details> |

## 🧠 Flashcards

| Hỏi                                   | Trả lời                                                              |
| ------------------------------------- | -------------------------------------------------------------------- |
| Vì sao xem sample theo class?         | Mẫu ngẫu nhiên nhỏ dễ bỏ sót class hiếm.                             |
| Feature nào bị loại trước thử nghiệm? | Feature không có lúc dự đoán hoặc chứa thông tin target sau sự kiện. |
