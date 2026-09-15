# Solutions: Validation — Đo đúng khả năng tổng quát hóa

Chỉ mở sau khi tự làm; đối chiếu cả hành vi và lý do.

## E-1

<details><summary>Mở lời giải</summary>

Solution `run_cv` đo cả hai; diễn giải chênh lệch bằng việc nhớ người, không gọi row CV là model tốt hơn.

**Kết quả cần kiểm tra:** Bảng mean, sample std, OOF F1 và overlap; group overlap=0, coverage mọi dòng=1.

**Lỗi thường gặp:** StratifiedKFold ngăn mọi leakage. Nó giữ tỷ lệ class, không tách người hoặc thứ tự thời gian.

</details>

## T-1

<details><summary>Mở lời giải</summary>

Sort ngày, dùng cửa sổ tăng dần; độ dài gap xuất phát từ độ trễ label, không mặc định bằng số ngày lookback.

**Kết quả cần kiểm tra:** Vẽ ít nhất 3 cửa sổ train/gap/validation; chứng minh mọi feature và label train đã có trước mốc validation.

**Lỗi thường gặp:** CV std là sai số tin cậy của điểm cuối. Các lần fit phụ thuộc nhau; ghi spread mô tả, không gọi confidence interval.

</details>

## O-1

<details><summary>Mở lời giải</summary>

Giữ group CV cho mục tiêu người mới, refit KNN pipeline trên labeled data; test chỉ dùng predict.

**Kết quả cần kiểm tra:** Có fold assignment, coverage assertions, 128 dòng CSV đúng ID; nêu giới hạn score cho người mới.

**Lỗi thường gặp:** OOF nghĩa là feature engineering trước CV cũng được. Mỗi transformer có fit phải nằm trong pipeline riêng mỗi fold.

</details>

## Code đối chiếu chạy độc lập

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

Để tái hiện toàn bộ pipeline và số đo, chạy [starter.ipynb](starter.ipynb) → [solution.ipynb](solution.ipynb). Các phép thử không bắt buộc phương án cải tiến phải thắng baseline.
