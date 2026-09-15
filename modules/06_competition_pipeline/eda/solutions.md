# Solutions: EDA — Khám phá dữ liệu trước baseline

Chỉ mở sau khi tự làm; đối chiếu cả hành vi và lý do.

## E-1

<details><summary>Mở lời giải</summary>

Đọc bảng `comparison` trong solution; after_event bị loại vì provenance, không vì mức tăng điểm.

**Kết quả cần kiểm tra:** Bảng 2 dòng gồm feature set, Macro F1 và quyết định; loại cột leakage bất kể điểm.

**Lỗi thường gặp:** Correlation cao nghĩa là feature tốt. Kiểm tra nguồn gốc và thời điểm; cột sau sự kiện bị loại dù điểm cao.

</details>

## T-1

<details><summary>Mở lời giải</summary>

ID bệnh nhân là group; xem ảnh theo class và giữ toàn bộ ảnh của người trong một partition.

**Kết quả cần kiểm tra:** Ghi image shape, ảnh lỗi, duplicate hash, class counts và split theo patient; không random split từng ảnh.

**Lỗi thường gặp:** Trùng bệnh nhân nghĩa là xóa dòng. Chỉ xóa bản ghi bị lặp thật; các lần đo khác nhau cần group split.

</details>

## O-1

<details><summary>Mở lời giải</summary>

Chạy starter, hoàn thành TODO rồi đối chiếu solution; dành 10 phút cuối đọc lại CSV và kiểm tra schema.

**Kết quả cần kiểm tra:** CSV 72 dòng, cột id/label, ID đúng thứ tự test; báo cáo ít nhất 3 findings có bằng chứng.

**Lỗi thường gặp:** EDA trên toàn bảng rồi tune theo mọi label là an toàn. Schema có thể xem toàn bảng; phân tích liên hệ target phục vụ lựa chọn model phải nằm trong train.

</details>

## Code đối chiếu chạy độc lập

```python
import pandas as pd
df = pd.DataFrame({'patient': ['A', 'A', 'B'], 'age': [20, 20, None]})
missing = df.isna().mean()
duplicates = df.duplicated().sum()
assert duplicates == 1
assert missing['age'] == 1 / 3
```

Để tái hiện toàn bộ pipeline và số đo, chạy [starter.ipynb](starter.ipynb) → [solution.ipynb](solution.ipynb). Các phép thử không bắt buộc phương án cải tiến phải thắng baseline.
