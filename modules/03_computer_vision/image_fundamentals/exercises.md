# Bài tập: Image Fundamentals

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Câu hỏi lý thuyết**
Tại sao cần chuẩn hóa ảnh (chia 255)?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Thực hành code**
Tự code hàm đổi từ BGR sang RGB bằng numpy slicing (không dùng `cv2.cvtColor`).

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Khám phá không gian màu HSV**
Dùng `cv2.cvtColor` để đổi một bức ảnh RGB sang hệ màu HSV (Hue, Saturation, Value).
Hiển thị thử kênh `H` (kênh số 0) ra màn hình bằng `matplotlib`. Màu sắc có vẻ thế nào?

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
