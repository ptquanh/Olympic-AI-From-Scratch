# Bài tập: Image Segmentation

## Tầng 1: Understand

**1. Câu hỏi lý thuyết**
Kỹ thuật Skip-connection ngang trong U-Net có tác dụng gì?

## Tầng 2: Implement

**1. Thực hành code**
Viết hàm `dice_coeff` (dùng thư viện torch) cho 2 mask A và B chứa 0 và 1.

## Tầng 3: Experiment

**1. Tác động của Threshold lên Dice Coefficient**
Trong segmentation, output của model thường là xác suất [0, 1]. Ta phải chọn một ngưỡng (Threshold) để ép về 0 hoặc 1 (Ví dụ: `pred > 0.5`).
Thử tự tạo một `pred` bằng `torch.rand()` và một nhãn `mask`. Tính Dice Coeff với Threshold 0.3 và Threshold 0.7 xem kết quả thay đổi ra sao.
