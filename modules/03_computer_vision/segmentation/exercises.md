# Bài tập: Image Segmentation

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Câu hỏi lý thuyết**
Kỹ thuật Skip-connection ngang trong U-Net có tác dụng gì?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Thực hành code**
Viết hàm `dice_coeff` (dùng thư viện torch) cho 2 mask A và B chứa 0 và 1.

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Tác động của Threshold lên Dice Coefficient**
Trong segmentation, output của model thường là xác suất [0, 1]. Ta phải chọn một ngưỡng (Threshold) để ép về 0 hoặc 1 (Ví dụ: `pred > 0.5`).
Thử tự tạo một `pred` bằng `torch.rand()` và một nhãn `mask`. Tính Dice Coeff với Threshold 0.3 và Threshold 0.7 xem kết quả thay đổi ra sao.

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
