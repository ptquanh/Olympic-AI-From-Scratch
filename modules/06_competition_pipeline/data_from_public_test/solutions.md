# Solutions: Public Test — Pseudo-labeling và Test-Time Augmentation

Chỉ mở sau khi tự làm; đối chiếu cả hành vi và lý do.

## U-1

<details><summary>Mở lời giải</summary>

Max của hai dòng là 0.9 và 0.55; trung bình xác suất 0.8 và 0.4 là 0.6.

**Kết quả cần kiểm tra:** Mask [True,False], nhãn được chọn [1], TTA class 1=0.6.

**Lỗi thường gặp:** Public test công khai nên được tìm nhãn thật để train. Chỉ dùng input được cung cấp theo đúng quy chế; tên chương không có nghĩa đi lấy nhãn test.

</details>

## I-1

<details><summary>Mở lời giải</summary>

Dùng mask.any() trước concatenate/fit; notebook có assert cho nhánh này.

**Kết quả cần kiểm tra:** Không có mẫu được chọn; model giữ baseline, không gọi fit trên mảng rỗng.

**Lỗi thường gặp:** TTA biến đổi nào cũng được. Chỉ dùng phép giữ ý nghĩa nhãn; bài localization cần biến đổi ngược output.

</details>

## E-1

<details><summary>Mở lời giải</summary>

Threshold dùng trên cùng probability baseline nên tập được chọn lồng nhau; score có thể tăng hoặc giảm. Reflection hợp lệ trong dữ liệu synthetic, không mặc định cho ảnh chữ số.

**Kết quả cần kiểm tra:** Bảng threshold/count/Macro F1; count không tăng khi tau tăng với cùng baseline. Nêu một giới hạn chuyển sang ảnh.

**Lỗi thường gặp:** Confidence cao chứng minh pseudo-label đúng. Model có thể sai tự tin, đặc biệt khi distribution shift; giữ validation tách biệt.

</details>

## Code đối chiếu chạy độc lập

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

Để tái hiện toàn bộ pipeline và số đo, chạy [lab.ipynb](lab.ipynb). Các phép thử không bắt buộc phương án cải tiến phải thắng baseline.
