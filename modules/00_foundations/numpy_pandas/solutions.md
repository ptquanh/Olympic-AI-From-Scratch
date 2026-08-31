# Lời giải: NumPy & Pandas

<details><summary><b>U-1 — Understand</b></summary>

**1. Lỗi Broadcasting**

- A có shape `(4, 3)`, B có shape `(4,)`. Broadcasting so sánh từ dimension ngoài cùng bên phải. Bên phải của A là 3, B là 4. Vì $3 \neq 4$ và không có cái nào bằng 1 nên lỗi.
- Sửa B: Reshape B thành `(4, 1)`. Lúc này bên phải của A là 3, B là 1 -> B sẽ tự giãn cột ra thành 3. `B.reshape(-1, 1)`.

**2. Pandas Indexing**

- `df['col_name']`: Trả về một **Series** (1 chiều).
- `df[['col_name']]`: Trả về một **DataFrame** (2 chiều).
- Quan trọng vì các mô hình Scikit-learn (như LinearRegression) yêu cầu input X phải là ma trận 2 chiều, nếu truyền Series sẽ bị báo lỗi.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

**1. Chuẩn hóa hình ảnh**

```python
# Giả sử img là numpy array
img_normalized = img / 255.0

```

**2. RFM Analysis**

```python
# Giả sử df là bảng sales
rfm = df.groupby('customer_id').agg(
    Monetary=('order_value', 'sum'),
    Frequency=('order_value', 'count')
)
# rfm đã tự động có index là customer_id

```

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

**1. Apply vs Vectorization**

- Vectorization `df['A']**2 + df['A']` sẽ gọi thẳng xuống C, chạy nhanh gấp hàng chục đến hàng trăm lần.
- `.apply()` bản chất vẫn là một vòng lặp `for` ngầm bằng Python thuần túy.
- Kết luận: Ưu tiên phép toán NumPy/Pandas theo cột khi code rõ và đã đo là nút thắt. `.apply()` hoặc loop vẫn hợp lý cho logic tuần tự/custom; quyết định bằng tính đúng, khả năng đọc và benchmark thay vì quy tắc tuyệt đối.

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>
