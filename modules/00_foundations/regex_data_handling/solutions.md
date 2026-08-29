# Lời giải: Regex & Data Handling

<details><summary><b>Tầng 1: Understand</b></summary>

**1. Greedy vs Non-Greedy**

- Dùng `.*` (Greedy): Sẽ bắt `<div>Xin chào</div>`. Nó tham lam ăn từ dấu `<` đầu tiên đến dấu `>` cuối cùng.
- Dùng `.*?` (Non-Greedy): Chỉ bắt `<div>`. Nó dừng lại ở dấu `>` đầu tiên tìm thấy.

**2. Data Pipeline**

- Nếu dữ liệu lớn hơn RAM, `df.dropna()` sẽ load toàn bộ vào RAM và chết.
- Giải pháp: Đọc file theo chunk (`pd.read_csv(chunksize=...)`), hoặc dùng các thư viện tối ưu out-of-core như Polars, Dask.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

**1. Bóc tách thông tin (Regex)**

```python
import re
text = "Hóa đơn HĐ-2023 có giá 2,000,000 VND"

# Tìm Hóa đơn
match_hd = re.search(r'HĐ-\d{4}', text)
invoice = match_hd.group() if match_hd else None

# Tìm Số tiền
match_price = re.search(r'[\d,]+', text)
price_str = match_price.group() if match_price else None
# Lọc dấu phẩy và chuyển int
price = int(price_str.replace(',', '')) if price_str else None
```

**2. Data Cleaning**

```python
# Điền tuổi bằng Median
df['Tuổi'].fillna(df['Tuổi'].median(), inplace=True)
# Hoặc df['Tuổi'] = df['Tuổi'].fillna(df['Tuổi'].median())
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

**1. Đoạn code chết chóc**

```python
import re

text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaa!"
# Mẫu có khả năng gây catastrophic backtracking
# Vì (a+)+ có rất rất nhiều cách khớp các ký tự a
re.match(r'(a+)+b', text)
```

Regex này mất cực nhiều thời gian mới nhận ra không có chữ 'b' ở cuối vì nó thử mọi tổ hợp chập của (a+).

</details>
