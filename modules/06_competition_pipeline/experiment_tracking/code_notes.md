# Code Notes: Experiment Tracking — Ghi lại để tái lập quyết định

## 🔑 Core Patterns

### Pattern 1 — Phép kiểm chứng tối thiểu

```python
import json
from hashlib import sha256
def config_hash(config):
    """Return a content hash for a JSON-serializable configuration."""
    payload = json.dumps(config, sort_keys=True, separators=(',', ':'))
    return sha256(payload.encode('utf-8')).hexdigest()
assert config_hash({'C': 1.0, 'seed': 42}) == config_hash({'seed': 42, 'C': 1.0})
assert config_hash({'C': 1.0}) != config_hash({'C': 0.1})
```

**Ghi nhớ:** Lưu điều kiện tạo kết quả, không chỉ kết quả; hash chỉ có ý nghĩa khi biết nó bao phủ nội dung nào.

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

| Việc cần làm      | Code                                 | Link Docs                                                             |
| ----------------- | ------------------------------------ | --------------------------------------------------------------------- |
| Canonical config  | `json.dumps(config, sort_keys=True)` | [Docs](https://docs.python.org/3/library/json.html#json.dumps)        |
| Data fingerprint  | `hashlib.sha256(data)`               | [Docs](https://docs.python.org/3/library/hashlib.html#hashlib.sha256) |
| Model persistence | `joblib.dump/load`                   | [Docs](https://scikit-learn.org/stable/model_persistence.html)        |

## 🏋️ Bài Luyện Code Tay

Đóng tất cả tài liệu, mở notebook trống và hẹn giờ. Chỉ mở hint khi bí; chạy assert rồi ghi lỗi sai vào nhật ký học.

| #   | Bài                                                           | Thời gian | Hint (ẩn)                                                                                                        |
| --- | ------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------- |
| 1   | Tạo canonical config hash và kiểm tra key order trong 8 phút. | 8 phút    | <details><summary>Hint</summary>Đối chiếu input/output contract và thêm assert trước khi mở reference.</details> |
| 2   | Viết JSON log có split/metric và đọc lại trong 10 phút.       | 10 phút   | <details><summary>Hint</summary>Đối chiếu input/output contract và thêm assert trước khi mở reference.</details> |

## 🧠 Flashcards

| Hỏi                                                  | Trả lời                                                                                       |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Vì sao không dùng timestamp làm bằng chứng duy nhất? | Timestamp không cho biết data, config hoặc code đã thay đổi gì.                               |
| Có thể load model lạ bằng joblib không?              | Chỉ load artifact do bạn tạo hoặc nguồn tin cậy; định dạng này có thể thực thi code khi load. |
