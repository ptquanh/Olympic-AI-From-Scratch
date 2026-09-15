# Exercises: Public Test — Pseudo-labeling và Test-Time Augmentation

Làm sau Worked Example. Mỗi bài ghi giả thuyết trước khi chạy và dẫn artifact làm bằng chứng.

## U-1 — Understand

**Learning outcome:** LO1.

Tính mask ở tau=0.85 cho `[0.1,0.9]`, `[0.55,0.45]`; tính TTA example.

**Expected output:** Mask [True,False], nhãn được chọn [1], TTA class 1=0.6.

## I-1 — Implement

**Learning outcome:** LO2.

Cài chọn mẫu và kiểm thử threshold 1.01.

**Expected output:** Không có mẫu được chọn; model giữ baseline, không gọi fit trên mảng rỗng.

## E-1 — Experiment

**Learning outcome:** LO3.

Chạy tau 0.70/0.85/0.95 và identity/reflection TTA.

**Expected output:** Bảng threshold/count/Macro F1; count không tăng khi tau tăng với cùng baseline. Nêu một giới hạn chuyển sang ảnh.
