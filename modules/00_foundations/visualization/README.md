# Visualization (Trực Quan Hóa Dữ Liệu)

> **Thời gian học ước tính:** 2 giờ (theory: 0.5h, code: 1h, exercises: 0.5h)
> **Loại:** Concept Lesson
> **Track:** Foundation ⭐ | Contest ⏭️

## Prerequisite Check

Chương này sử dụng kết quả xử lý dữ liệu từ NumPy và Pandas.
Bạn có thể bỏ qua chương này nếu trả lời được:

1. Vẽ Scatter plot khác gì với Line plot?
2. Trong Matplotlib, `Figure` và `Axes` khác nhau như thế nào?

Nếu chưa trả lời được → tiếp tục học chương này.

## Learning Outcomes

Sau chương này, bạn sẽ có thể:

- [ ] Tạo `Figure` và `Axes` (subplots) bằng Matplotlib
- [ ] Vẽ Line, Scatter, Bar, Histogram chuẩn chỉ (có title, label, legend)
- [ ] Dùng Seaborn để vẽ các biểu đồ thống kê phức tạp chỉ với 1 dòng code
- [ ] Chọn đúng loại biểu đồ cho từng mục đích phân tích (EDA)

## Concept Map

```text
[NumPy & Pandas] ──→ [CHƯƠNG NÀY] ──→ [Exploratory Data Analysis (EDA)]
                             │
                             └── dùng trong [Theo dõi Loss curve khi Train]
```

## 1. Intuition — Tại Sao Phải Vẽ?

Trong AI/Machine Learning, bạn sẽ liên tục đối mặt với 2 tình huống:

1. **Trước khi train (EDA):** Nhìn vào bảng số liệu hàng triệu dòng, bạn không thể biết dữ liệu có bị lệch, có điểm dị biệt (outlier) hay không. Một biểu đồ Histogram hoặc Scatter plot sẽ phơi bày điều đó ngay lập tức.
2. **Trong/Sau khi train:** Bạn cần vẽ biểu đồ Loss/Accuracy thay đổi theo thời gian (Epoch) để biết mô hình đang học tốt hay bị Overfitting.

**Quy tắc tối thượng (R3 trong Rules):** Một biểu đồ không có Title, không có nhãn trục X (X-label), không có nhãn trục Y (Y-label) là một biểu đồ **vô giá trị**.

## 2. Matplotlib: Nền Móng

Matplotlib (đặc biệt là module `pyplot`) là thư viện cơ bản nhất.
Khái niệm quan trọng nhất:

- **Figure:** Cửa sổ chứa toàn bộ hình vẽ.
- **Axes:** Hệ tọa độ thực tế nơi dữ liệu được vẽ lên (Đừng nhầm với _Axis_ là cái trục). Một Figure có thể chứa nhiều Axes (Subplots).

## 3. Seaborn: Đẹp và Nhanh (Dành cho Thống Kê)

Seaborn được xây dựng TRÊN nền Matplotlib. Nó được thiết kế đặc biệt để hoạt động mượt mà với Pandas DataFrame và tự động làm cho biểu đồ trông đẹp hơn.
Nếu vẽ các biểu đồ phân phối, tương quan giữa các cột trong DataFrame → Dùng Seaborn.
Nếu cần tinh chỉnh từng pixel, vẽ biểu đồ cơ bản từ list/array → Dùng Matplotlib.

## 4. Các Loại Biểu Đồ Thường Dùng

1. **Line Plot (`plt.plot`):** Quan sát xu hướng theo thời gian (vd: Loss/Epoch).
2. **Scatter Plot (`plt.scatter`):** Quan sát mối quan hệ giữa 2 biến liên tục (vd: Cân nặng và Chiều cao).
3. **Histogram (`plt.hist` hoặc `sns.histplot`):** Xem phân phối của 1 biến (vd: Có bao nhiêu người trong từng độ tuổi).
4. **Bar Chart (`plt.bar` hoặc `sns.barplot`):** So sánh giá trị giữa các nhóm phân loại (vd: Doanh thu theo Thành phố).
5. **Heatmap (`sns.heatmap`):** Xem ma trận tương quan (Correlation) giữa tất cả các đặc trưng.

## 5. Common Mistakes & Misconceptions

> ❌ **Sai:** Cố gắng vẽ tất cả dữ liệu (hàng triệu điểm) lên một Scatter Plot.
> ✅ **Đúng:** Nó sẽ biến thành 1 cục mực đen thui. Hãy dùng lấy mẫu (sampling) hoặc vẽ theo mật độ (hexbin, KDE) nếu dữ liệu quá lớn.

> ❌ **Sai:** Chỉ dùng `plt.plot()` mà không có Figure/Axes rõ ràng (State-based interface).
> ✅ **Đúng:** Nên dùng Object-oriented interface (`fig, ax = plt.subplots()`) để dễ dàng quản lý nhiều biểu đồ con và tránh vẽ nhầm sang biểu đồ khác.
