# Exercises: Debugging ML — Tìm lỗi bằng kiểm chứng nhỏ

Làm sau Worked Example. Mỗi bài ghi giả thuyết trước khi chạy và dẫn artifact làm bằng chứng.

## E-1 — Experiment

**Learning outcome:** LO1.

So sánh dấu cộng/trừ và ba learning rate.

**Expected output:** Bad step tăng loss trên fixture; correct step giảm; có bảng hoặc plot được gắn nhãn đầy đủ.

## T-1 — Transfer

**Learning outcome:** LO2.

Chuyển checklist sang PyTorch classification.

**Expected output:** Liệt kê logits/target shape, loss phù hợp, zero_grad→forward→loss→backward→step, train/eval và tiny-overfit.

## O-1 — Olympiad

**Learning outcome:** LO3.

Trong 60 phút, sửa loop, lưu diagnostic và xuất submission.

**Expected output:** Gradient relative error <1e-6 trên fixture; tiny accuracy=1; 64 dòng id/label; postmortem nêu root cause.
