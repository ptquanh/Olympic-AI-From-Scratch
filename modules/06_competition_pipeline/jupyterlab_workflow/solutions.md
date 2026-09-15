# Solutions: JupyterLab Workflow — Kernel sạch và bài nộp tái lập

Chỉ mở sau khi tự làm; đối chiếu cả hành vi và lý do.

## U-1

<details><summary>Mở lời giải</summary>

Kernel giữ scale=2 cho đến khi cell A được chạy lại.

**Kết quả cần kiểm tra:** Output cũ [2,6], fresh run [3,9]; nêu document khác kernel.

**Lỗi thường gặp:** Save notebook là save model. Save lưu cell/output; array và model trong RAM phải được xuất riêng.

</details>

## I-1

<details><summary>Mở lời giải</summary>

Dùng np.load(..., allow_pickle=False) trong context manager; biến phải được khôi phục từ artifact trước predict.

**Kết quả cần kiểm tra:** np.allclose trước/sau=True; CSV đúng ID và schema.

**Lỗi thường gặp:** Đóng tab là giải phóng GPU. Kernel có thể còn chạy; mở Running panel để shutdown đúng tiến trình.

</details>

## E-1

<details><summary>Mở lời giải</summary>

Dừng cell dài bằng Interrupt, đọc lỗi và restart nếu state không còn rõ; lưu kiểm tra tự làm trong nhật ký học.

**Kết quả cần kiểm tra:** Ghi kết quả replay, cell bị interrupt và cách phục hồi; không đánh dấu đạt thao tác chưa làm.

**Lỗi thường gặp:** Terminal dùng cùng Python với kernel. Có thể khác môi trường; kiểm tra sys.executable ở notebook và python ở terminal.

</details>

## Code đối chiếu chạy độc lập

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

Để tái hiện toàn bộ pipeline và số đo, chạy [lab.ipynb](lab.ipynb). Các phép thử không bắt buộc phương án cải tiến phải thắng baseline.
