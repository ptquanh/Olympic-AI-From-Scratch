# Exercises: Ensembling — Averaging, Blending và Stacking

Làm sau Worked Example. Mỗi bài ghi giả thuyết trước khi chạy và dẫn artifact làm bằng chứng.

## E-1 — Experiment

**Learning outcome:** LO1.

So sánh single/mean/blend/stack trên outer-validation cố định.

**Expected output:** 5 dòng score và latency; OOF coverage=1; nêu lựa chọn dù ensemble không thắng.

## T-1 — Transfer

**Learning outcome:** LO2.

Áp dụng với validation có nhiều ảnh một người.

**Expected output:** Base OOF và inner blend đều tách người; ID/class order được căn trước gộp.

## O-1 — Olympiad

**Learning outcome:** LO3.

Trong 75 phút, tạo ensemble có thể chạy lại.

**Expected output:** CSV 80 dòng, lựa chọn model có bằng chứng metric và ngân sách; lưu weight và split/config.
