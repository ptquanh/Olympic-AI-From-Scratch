# Lời giải: Feature Engineering

<details><summary><b>U-1 — Understand</b></summary>
Target Encoding rất nhạy cảm với các Category hiếm. Cách xử lý:
1. Dùng kỹ thuật Smoothing (kéo giá trị target encoding của các mẫu hiếm về gần với giá trị trung bình toàn cục của nhãn).
2. Dùng Leave-One-Out Encoding hoặc K-Fold Target Encoding.
3. Gom các Category hiếm thành một nhóm chung "Other" trước khi Encoding.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

```python
import pandas as pd
df = pd.DataFrame({'Date': ['2024-05-12', '2024-06-15']})

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.dayofweek

```

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

```python
import numpy as np
X = np.random.randn(100)
X[0] = 1000 # Outlier

p1 = np.percentile(X, 1)
p99 = np.percentile(X, 99)

X_clipped = np.clip(X, p1, p99)
print("New Max:", X_clipped.max())

```

Giá trị 1000 đã bị gọt xuống bằng đúng giá trị ở bách phân vị thứ 99 (thường loanh quanh 2-3 đối với phân phối chuẩn).

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>
