# Exercises: Validation — Đo đúng khả năng tổng quát hóa

Làm sau Worked Example. Mỗi bài ghi giả thuyết trước khi chạy và dẫn artifact làm bằng chứng.

## E-1 — Experiment

**Learning outcome:** LO1.

So sánh row CV và group CV, giữ nguyên model.

**Expected output:** Bảng mean, sample std, OOF F1 và overlap; group overlap=0, coverage mọi dòng=1.

## T-1 — Transfer

**Learning outcome:** LO2.

Thiết kế validation dự báo doanh số ngày kế tiếp, feature dùng 7 ngày quá khứ.

**Expected output:** Vẽ ít nhất 3 cửa sổ train/gap/validation; chứng minh mọi feature và label train đã có trước mốc validation.

## O-1 — Olympiad

**Learning outcome:** LO3.

Trong 60 phút, tạo CV report và submission tái lập.

**Expected output:** Có fold assignment, coverage assertions, 128 dòng CSV đúng ID; nêu giới hạn score cho người mới.
