# Bài tập: Feature Engineering

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Tại sao dùng Target Encoding dễ bị Leakage?**
Nếu một Category chỉ có đúng 1 mẫu trong tập Train (và nhãn của nó là 1). Khi target encoding, cột mới sẽ mang giá trị 1. Mô hình sẽ học thuộc lòng điều này. Ta xử lý sao?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Ngày tháng**
Cho cột `Date` dạng chuỗi `2024-05-12`. Dùng pandas chuyển về kiểu datetime và tạo ra 3 cột mới: `Year`, `Month`, `DayOfWeek`.

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Outlier Clipping**
Tạo ra mảng `X = np.random.randn(100)` (phân phối chuẩn). Thêm một Outlier `X[0] = 1000`.
Dùng `np.clip()` để cắt (clip) mảng này ở ngưỡng phần vị thứ 1 (1st percentile) và 99 (99th percentile). In ra giá trị Max mới của mảng.

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
