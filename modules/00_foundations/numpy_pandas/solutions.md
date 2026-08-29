# Lời giải: NumPy & Pandas

<details><summary><b>Tầng 1: Understand</b></summary>

**1. Lỗi Broadcasting**

- A có shape `(4, 3)`, B có shape `(4,)`. Broadcasting so sánh từ dimension ngoài cùng bên phải. Bên phải của A là 3, B là 4. Vì $3 \neq 4$ và không có cái nào bằng 1 nên lỗi.
- Sửa B: Reshape B thành `(4, 1)`. Lúc này bên phải của A là 3, B là 1 -> B sẽ tự giãn cột ra thành 3. `B.reshape(-1, 1)`.

**2. Pandas Indexing**

- `df['col_name']`: Trả về một **Series** (1 chiều).
- `df[['col_name']]`: Trả về một **DataFrame** (2 chiều).
- Quan trọng vì các mô hình Scikit-learn (như LinearRegression) yêu cầu input X phải là ma trận 2 chiều, nếu truyền Series sẽ bị báo lỗi.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

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

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

**1. Apply vs Vectorization**

- Vectorization `df['A']**2 + df['A']` sẽ gọi thẳng xuống C, chạy nhanh gấp hàng chục đến hàng trăm lần.
- `.apply()` bản chất vẫn là một vòng lặp `for` ngầm bằng Python thuần túy.
- Kết luận: Luôn ưu tiên dùng các phép toán có sẵn của Pandas/NumPy. Chỉ dùng `.apply()` khi hàm quá phức tạp không thể viết dưới dạng vector (ví dụ gọi API ngoài, xử lý text regex phức tạp, hàm custom có lệnh if-else).
</details>
