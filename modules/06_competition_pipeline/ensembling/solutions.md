# Solutions: Ensembling — Averaging, Blending và Stacking

Chỉ mở sau khi tự làm; đối chiếu cả hành vi và lý do.

## E-1

<details><summary>Mở lời giải</summary>

Bảng comparison trong solution không yêu cầu thứ hạng cố định; chọn bằng metric đã khai báo.

**Kết quả cần kiểm tra:** 5 dòng score và latency; OOF coverage=1; nêu lựa chọn dù ensemble không thắng.

**Lỗi thường gặp:** Trung bình nhãn 0/1 là soft voting. Soft voting gộp probability; nhãn cứng làm mất confidence.

</details>

## T-1

<details><summary>Mở lời giải</summary>

Thay StratifiedKFold bằng group splitter phù hợp; group của outer-validation không được xuất hiện trong bất kỳ base fit nào.

**Kết quả cần kiểm tra:** Base OOF và inner blend đều tách người; ID/class order được căn trước gộp.

**Lỗi thường gặp:** Fit meta-model trên output train là stacking hợp lệ. Dùng OOF để mỗi meta-feature được tạo khi dòng đó không nằm trong base training.

</details>

## O-1

<details><summary>Mở lời giải</summary>

Giữ base models và meta phù hợp đúng chiến lược đã đánh giá; notebook chọn trên validation rồi predict test, không tune test.

**Kết quả cần kiểm tra:** CSV 80 dòng, lựa chọn model có bằng chứng metric và ngân sách; lưu weight và split/config.

**Lỗi thường gặp:** Blend weight tốt nhất trên test có thể dùng. Test không có nhãn; chỉ chọn weight trên inner hold-out được phân bổ trước.

</details>

## Code đối chiếu chạy độc lập

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

Để tái hiện toàn bộ pipeline và số đo, chạy [starter.ipynb](starter.ipynb) → [solution.ipynb](solution.ipynb). Các phép thử không bắt buộc phương án cải tiến phải thắng baseline.
