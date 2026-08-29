# Exercises: NumPy & Pandas

## Tầng 1: Understand

**1. Giải thích lỗi Broadcasting**
Cho `A.shape = (4, 3)` và `B.shape = (4,)`. Phép toán `A + B` sẽ báo lỗi `ValueError: operands could not be broadcast together`.
Giải thích tại sao? Làm thế nào để sửa B sao cho phép cộng hợp lệ?

**2. Pandas Indexing**
Phân biệt sự khác nhau về kết quả (kiểu dữ liệu) giữa `df['col_name']` và `df[['col_name']]`. Tại sao điều này quan trọng?

## Tầng 2: Implement

**1. Chuẩn hóa hình ảnh (Min-Max Scaling)**
Cho một ảnh RGB (ảnh màu) được biểu diễn bằng NumPy array có kích thước `(height, width, 3)` với giá trị pixel từ 0 đến 255.
Viết code NumPy (không dùng vòng lặp) để chuẩn hóa ảnh này về khoảng `[0, 1]`.

**2. RFM Analysis (Recency, Frequency, Monetary)**
Cho DataFrame `sales` gồm các cột `['customer_id', 'order_date', 'order_value']`.
Viết pipeline Pandas (càng ít dòng càng tốt) để tính:

- Tổng số tiền mua (Monetary) của mỗi khách hàng.
- Số lần mua (Frequency) của mỗi khách hàng.
- (Khó hơn) Kết quả trả về một DataFrame mới có index là `customer_id` và 2 cột `Monetary`, `Frequency`.

## Tầng 3: Experiment

**1. Tốc độ của `.apply()` so với Vectorization**
Tạo một DataFrame với 1 cột `A` chứa 5 triệu số ngẫu nhiên.

1. Dùng `df['A'].apply(lambda x: x**2 + x)`
2. Dùng phép toán trực tiếp `df['A']**2 + df['A']`
   Đo và so sánh thời gian chạy. Rút ra kết luận khi nào nên/không nên dùng `.apply()`.
