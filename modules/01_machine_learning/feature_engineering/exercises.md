# Bài tập: Feature Engineering

## Tầng 1: Understand

**1. Tại sao dùng Target Encoding dễ bị Leakage?**
Nếu một Category chỉ có đúng 1 mẫu trong tập Train (và nhãn của nó là 1). Khi target encoding, cột mới sẽ mang giá trị 1. Mô hình sẽ học thuộc lòng điều này. Ta xử lý sao?

## Tầng 2: Implement

**1. Ngày tháng**
Cho cột `Date` dạng chuỗi `2024-05-12`. Dùng pandas chuyển về kiểu datetime và tạo ra 3 cột mới: `Year`, `Month`, `DayOfWeek`.

## Tầng 3: Experiment

**1. Label vs One-Hot Encoding**
Thử nghiệm trên bộ dữ liệu Titanic. Sử dụng Label Encoding cho cột 'Embarked' và đo điểm. Sau đó chuyển sang One-Hot Encoding và đo lại điểm. Xem độ chính xác thay đổi như thế nào trên mô hình Logistic Regression.
