# Bài tập: CNN Architectures

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Câu hỏi lý thuyết**
Skip Connection (Residual Connection) của ResNet giúp giải quyết hiện tượng gì?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Thực hành code**
Tải ResNet18 từ `torchvision`, đóng băng toàn bộ trọng số, và thay lớp `.fc` cuối cùng thành 5 classes.

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Khảo sát kiến trúc MobileNet**
MobileNet là một họ mạng CNN chuyên dùng cho điện thoại di động vì tốc độ rất nhanh.
Hãy dùng `torchvision.models.mobilenet_v2()` để tạo model. In ra tổng số lượng tham số (parameters) của model này và so sánh với ResNet18 (ResNet18 có khoảng 11 triệu tham số).

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
