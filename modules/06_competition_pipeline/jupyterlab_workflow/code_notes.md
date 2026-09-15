# Code Notes: JupyterLab Workflow — Kernel sạch và bài nộp tái lập

## 🔑 Core Patterns

### Pattern 1 — Phép kiểm chứng tối thiểu

```python
from pathlib import Path
import numpy as np
folder = Path('outputs')
folder.mkdir(exist_ok=True)
weights = np.array([1.0, -1.0])
np.savez(folder / 'workflow_pattern.npz', weights=weights)
del weights
with np.load(folder / 'workflow_pattern.npz', allow_pickle=False) as saved:
    weights = saved['weights']
assert weights.tolist() == [1.0, -1.0]
```

**Ghi nhớ:** Chạy theo thứ tự, lưu artifact có schema, kiểm tra lại bằng dữ liệu đọc từ disk.

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

| Việc cần làm      | Code                               | Link Docs                                                              |
| ----------------- | ---------------------------------- | ---------------------------------------------------------------------- |
| Quản lý kernel    | `Running panel → Shut Down`        | [Docs](https://jupyterlab.readthedocs.io/en/stable/user/running.html)  |
| Thao tác notebook | `Restart Kernel and Run All Cells` | [Docs](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html) |
| Terminal          | `Launcher → Terminal`              | [Docs](https://jupyterlab.readthedocs.io/en/stable/user/terminal.html) |

## 🏋️ Bài Luyện Code Tay

Đóng tất cả tài liệu, mở notebook trống và hẹn giờ. Chỉ mở hint khi bí; chạy assert rồi ghi lỗi sai vào nhật ký học.

| #   | Bài                                                                         | Thời gian | Hint (ẩn)                                                                                                        |
| --- | --------------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------- |
| 1   | Tạo outputs bằng pathlib, ghi NPZ rồi reload trong 8 phút.                  | 8 phút    | <details><summary>Hint</summary>Đối chiếu input/output contract và thêm assert trước khi mở reference.</details> |
| 2   | Tạo notebook 3 cell chạy độc lập sau restart và kiểm tra CSV trong 10 phút. | 10 phút   | <details><summary>Hint</summary>Đối chiếu input/output contract và thêm assert trước khi mở reference.</details> |

## 🧠 Flashcards

| Hỏi                             | Trả lời                                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Restart có xóa file disk không? | Không; xóa RAM của kernel. File đã ghi vẫn tồn tại.                                                       |
| Kernel busy quá lâu thì làm gì? | Interrupt trước, xem cell đang chạy; nếu không phục hồi được thì restart rồi chạy lại từ artifact hợp lệ. |
