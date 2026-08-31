# Bài tập: Data Augmentation

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Câu hỏi lý thuyết**
Bài toán nhận diện chữ số viết tay (MNIST). Có nên dùng RandomHorizontalFlip không? Tại sao?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Thực hành code**
Viết Compose kết hợp 3 transform: Resize(256), RandomCrop(224), ToTensor().

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Tác động của Normalize**
Thử Normalize một ảnh bằng `transforms.Normalize((0.5,), (0.5,))`.
In ra giá trị lớn nhất và nhỏ nhất của tensor ảnh sau khi chuẩn hóa. Giá trị giờ nằm trong khoảng nào?

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
