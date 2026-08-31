# Lời giải: Visualization

<details><summary><b>U-1 — Understand</b></summary>

**1. Matplotlib vs Seaborn**

- Matplotlib giống như thư viện core, kiểm soát linh hoạt từng nét vẽ, trục tọa độ. Dùng khi cần customize rất sâu (vd đồ thị nhiều lớp phức tạp, làm subplots phức tạp).
- Seaborn bọc ngoài Matplotlib, tương thích xuất sắc với Pandas DataFrame. Dùng khi muốn thăm dò dữ liệu (EDA) nhanh, đẹp, và vẽ các đồ thị thống kê (boxplot, violin plot, heatmap).

**2. Outlier**

- Trên Boxplot, outlier là các điểm chấm nhỏ nằm ngoài hai thanh râu (whiskers).

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

**1. Heatmap Ma trận Tương quan**

```python
import seaborn as sns
import matplotlib.pyplot as plt

corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

```

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

**1. Subplots Layout**

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
# axes[0] là biểu đồ bên trái
# axes[1] là biểu đồ bên phải
axes[0].plot([1, 2, 3], [1, 4, 9])
axes[0].set_title("Plot 1")

axes[1].bar(["A", "B"], [5, 10])
axes[1].set_title("Plot 2")

plt.tight_layout()
plt.show()

```

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>
