# Lời giải: NumPy & Pandas

<details><summary><b>Tầng 1: Understand</b></summary>

Khi thực hiện thao tác cộng trên Python List bằng vòng lặp `for`, Python phải kiểm tra kiểu dữ liệu của TỪNG phần tử trước khi cộng (do List có thể chứa số, chuỗi cùng lúc). NumPy thao tác trực tiếp trên C, kiểu dữ liệu cố định, không tốn thời gian kiểm tra, và hỗ trợ tính toán vector hóa (SIMD trên CPU).

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
# NumPy
import numpy as np
A = np.random.randn(10, 10)
B = np.random.randn(10, 10)
C = A @ B

# Pandas
import pandas as pd
data = {
    'Student': ['A', 'A', 'B', 'B'],
    'Subject': ['Math', 'Physics', 'Math', 'Physics'],
    'Score': [8, 9, 7, 6]
}
df = pd.DataFrame(data)
avg_score = df.groupby('Subject')['Score'].mean()
print(avg_score)
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

Dùng hàm `df.fillna(df.mean(), inplace=True)`.

</details>
