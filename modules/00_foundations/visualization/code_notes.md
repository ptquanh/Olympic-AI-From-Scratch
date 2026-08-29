# Code Notes: Visualization

## 🔑 Core Patterns (Phải nhớ)

### Pattern 1: Matplotlib Object-Oriented (Chuẩn mực)

```python
import matplotlib.pyplot as plt

# Tạo 1 Figure chứa 1 hệ tọa độ (Axes)
fig, ax = plt.subplots(figsize=(8, 5))

# Vẽ lên Axes
ax.plot([1, 2, 3], [10, 20, 15], marker='o', label='Doanh thu')

# THÊM ĐẦY ĐỦ THÔNG TIN BẮT BUỘC
ax.set_title("Biểu đồ Doanh Thu")
ax.set_xlabel("Tháng")
ax.set_ylabel("Triệu VND")
ax.legend() # Hiện chú thích

plt.show()
```

**Ghi nhớ:** Luôn dùng `fig, ax = plt.subplots()`. Luôn set title, xlabel, ylabel.

### Pattern 2: Vẽ Nhiều Subplots

```python
# Tạo Figure 1 hàng, 2 cột (2 biểu đồ cạnh nhau)
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))

ax1.plot(x, y1)
ax1.set_title("Biểu đồ 1")

ax2.scatter(x, y2)
ax2.set_title("Biểu đồ 2")

plt.tight_layout() # Tránh các chữ đè lên nhau
plt.show()
```

**Ghi nhớ:** Dùng `plt.tight_layout()` trước khi `show()`.

### Pattern 3: Seaborn cho Pandas DataFrame

```python
import seaborn as sns

# Vẽ Histogram xem phân phối tuổi
sns.histplot(data=df, x='age', bins=20, kde=True)

# Vẽ Scatter có tô màu theo cột nhóm (Hue)
sns.scatterplot(data=df, x='height', y='weight', hue='gender')
```

**Ghi nhớ:** Seaborn nhận trực tiếp tham số `data=DataFrame`, `x` và `y` là tên cột. Rất nhàn!

## 📋 API Cheat Sheet

| Việc cần làm       | Code                                                  | Docs                   |
| ------------------ | ----------------------------------------------------- | ---------------------- |
| Vẽ đường kẻ lưới   | `ax.grid(True, linestyle='--')`                       |                        |
| Lưu ảnh ra file    | `fig.savefig('plot.png', dpi=300)`                    | Đặt TRƯỚC `plt.show()` |
| Chỉnh cỡ chữ Title | `ax.set_title("Title", fontsize=16)`                  |                        |
| Heatmap tương quan | `sns.heatmap(df.corr(), annot=True, cmap='coolwarm')` | Tuyệt chiêu EDA        |

## 🏋️ Bài Luyện Code Tay

**Quy tắc:** Đóng tất cả tài liệu. Mở notebook trống. Hẹn giờ.

| #   | Bài                                                                                                               | Thời gian | Hint (chỉ xem khi bí)                                                       |
| --- | ----------------------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------- |
| 1   | Dùng `numpy` sinh 100 điểm `x` (từ -5 đến 5), `y = x^2`. Vẽ Line plot với màu đỏ, nét đứt. Nhớ set Title và trục. | 5 phút    | `x = np.linspace(-5, 5, 100)`, `ax.plot(x, y, color='red', linestyle='--')` |
| 2   | Cho dict `sales = {'Hanoi': 50, 'HCM': 80, 'Da Nang': 45}`. Vẽ Bar chart thể hiện.                                | 5 phút    | `ax.bar(sales.keys(), sales.values())`                                      |

## 🧠 Flashcards (Hỏi → Trả lời)

| Hỏi                                                                     | Trả lời                                  |
| ----------------------------------------------------------------------- | ---------------------------------------- |
| Lệnh nào để vẽ phân phối của MỘT biến số lượng liên tục?                | Histogram (`plt.hist` / `sns.histplot`). |
| Hàm nào để ngăn chặn các subplot đè chữ/số lên nhau?                    | `plt.tight_layout()`.                    |
| Trong Machine Learning, vẽ đồ thị Loss vs Epoch thì dùng loại plot nào? | Line plot (`plt.plot`).                  |
