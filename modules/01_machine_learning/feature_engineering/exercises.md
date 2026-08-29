# Bài tập: Feature Engineering

## Tầng 1: Understand

**1. Tại sao dùng Target Encoding dễ bị Leakage?**
Nếu một Category chỉ có đúng 1 mẫu trong tập Train (và nhãn của nó là 1). Khi target encoding, cột mới sẽ mang giá trị 1. Mô hình sẽ học thuộc lòng điều này. Ta xử lý sao?

## Tầng 2: Implement

**1. Ngày tháng**
Cho cột `Date` dạng chuỗi `2024-05-12`. Dùng pandas chuyển về kiểu datetime và tạo ra 3 cột mới: `Year`, `Month`, `DayOfWeek`.

## Tầng 3: Experiment

**1. Outlier Clipping**
Tạo ra mảng `X = np.random.randn(100)` (phân phối chuẩn). Thêm một Outlier `X[0] = 1000`.
Dùng `np.clip()` để cắt (clip) mảng này ở ngưỡng phần vị thứ 1 (1st percentile) và 99 (99th percentile). In ra giá trị Max mới của mảng.
