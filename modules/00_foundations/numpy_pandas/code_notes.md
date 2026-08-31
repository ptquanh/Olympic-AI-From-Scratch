# Code Notes: NumPy & Pandas

## 🔑 Core Patterns (Phải nhớ)

### Pattern 1: Array Creation & Reshape

```python
import numpy as np
a = np.zeros((3, 4)) # Mảng 3x4 toàn số 0
b = np.arange(12)    # [0, 1, ..., 11]
c = b.reshape(3, 4)  # Đổi hình dạng thành 3x4

```

**Ghi nhớ:** Luôn check `shape` của array khi debug lỗi. Dùng `-1` trong reshape để NumPy tự tính (vd: `reshape(-1, 4)`).

### Pattern 2: Broadcasting

```python
matrix = np.ones((4, 3)) # Shape: (4, 3)
vector = np.array([1, 2, 3]) # Shape: (3,)
# Vector sẽ được "kéo giãn" (broadcast) thành (4,3) để cộng vào matrix
result = matrix + vector

```

**Ghi nhớ:** Căn lề phải shape. Trùng nhau hoặc bằng 1 thì broadcast được.

### Pattern 3: Pandas Loading & Filtering

```python
import pandas as pd
df = pd.read_csv('data.csv')
# Lọc khách hàng VIP và tuổi > 30
vip_df = df[(df['is_vip'] == True) & (df['age'] > 30)]

```

**Ghi nhớ:** Dùng dấu `&`, `|` thay cho `and`, `or`. Luôn đóng ngoặc tròn `()` cho từng điều kiện.

### Pattern 4: Groupby & Aggregate

```python
# Tính giá trị hóa đơn trung bình theo từng thành phố
avg_bill = df.groupby('city')['bill_amount'].mean()

```

**Ghi nhớ:** `groupby(cot_nhom)[cot_tinh_toan].ham_tinh_toan()`

## 📋 API Cheat Sheet

| Việc cần làm              | Code                                            | Docs                                                                          |
| ------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------- |
| Khởi tạo array ngẫu nhiên | `np.random.rand(3, 3)`, `np.random.randn(3, 3)` | [link](https://numpy.org/doc/stable/reference/random/index.html)              |
| Ma trận chuyển vị         | `array.T` hoặc `array.transpose()`              | [link](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.T.html) |
| Đọc CSV, xử lý date       | `pd.read_csv('file.csv', parse_dates=['col'])`  | [link](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)     |
| Khảo sát nhanh data       | `df.head()`, `df.info()`, `df.describe()`       |                                                                               |
| Tìm giá trị thiếu (NaN)   | `df.isnull().sum()`                             |                                                                               |

## 🏋️ Bài Luyện Code Tay

**Quy tắc:** Đóng tất cả tài liệu. Mở notebook trống. Hẹn giờ.

| #   | Bài                                                                                    | Thời gian | Hint (chỉ xem khi bí)                                                   |
| --- | -------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------- |
| 1   | Tạo ma trận $3 \times 3$ ngẫu nhiên, chuẩn hóa (đưa mean về 0, std về 1) bằng NumPy    | 5 phút    | `(X - X.mean()) / X.std()`                                              |
| 2   | Đọc file CSV tưởng tượng, lọc ra những người có lương > 1000 và ở cột 'Dept' là 'IT'   | 5 phút    | `df[(df['salary'] > 1000) & (df['Dept'] == 'IT')]`                      |
| 3   | One-hot encoding thủ công: cho array `[0, 1, 2, 1]`, chuyển thành ma trận $4 \times 3$ | 10 phút   | Khởi tạo ma trận zeros, dùng fancy indexing: `M[np.arange(4), arr] = 1` |

## 🧠 Flashcards (Hỏi → Trả lời)

| Hỏi                                                      | Trả lời                                                                                       |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| NumPy: Shape `(5, 4)` và `(4,)` có broadcast được không? | Được. `(4,)` khớp với chiều cuối cùng của `(5,4)`.                                            |
| Pandas: `.loc[]` khác gì `.iloc[]`?                      | `.loc[]` truy cập theo label (tên index/column), `.iloc[]` theo số thứ tự (integer position). |
| Tại sao gọi `.copy()` khi tách DataFrame?                | Tránh sửa view ảnh hưởng đến DataFrame gốc (lỗi SettingWithCopyWarning).                      |
