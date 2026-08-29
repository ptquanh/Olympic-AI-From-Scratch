# Lời giải: Visualization

<details><summary><b>Tầng 1: Understand</b></summary>

Matplotlib như một thư viện vẽ đồ thị ở mức độ gốc, kiểm soát đến từng pixel, trục tọa độ, label.
Seaborn là lớp bọc bên ngoài Matplotlib, được thiết kế ĐẶC BIỆT cho việc vẽ đồ thị dựa trên Pandas DataFrame một cách đẹp mắt và nhanh gọn nhất.
Khi cần đồ thị đẹp + nhanh -> Dùng Seaborn. Khi cần custom các chi tiết cực khó -> Matplotlib.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({
    'Income': np.random.normal(50000, 10000, 100),
    'Age': np.random.randint(20, 60, 100)
})

# Scatter Plot
sns.scatterplot(data=df, x='Age', y='Income')
plt.title('Relationship between Age and Income')
plt.show()

# Histogram
sns.histplot(data=df, x='Income', bins=20)
plt.title('Income Distribution')
plt.show()
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

Trong Boxplot, điểm Outlier được vẽ thành các dấu chấm nhỏ nằm bên ngoài hai thanh râu (whiskers). Công thức mặc định thường là $Q1 - 1.5 \times IQR$ và $Q3 + 1.5 \times IQR$.

</details>
