# Exercises: Experiment Tracking — Ghi lại để tái lập quyết định

Làm sau Worked Example. Mỗi bài ghi giả thuyết trước khi chạy và dẫn artifact làm bằng chứng.

## U-1 — Understand

**Learning outcome:** LO1.

Phân biệt vai trò seed, config hash và data hash.

**Expected output:** Nêu đúng ba vai trò; không tuyên bố hash chứng minh chất lượng hoặc seed đảm bảo mọi hardware.

## I-1 — Implement

**Learning outcome:** LO2.

Ghi 3 run có C khác nhau và kiểm tra JSON round-trip.

**Expected output:** 3 run_id khác nhau; split giữ nguyên; có đủ metric/runtime/versions và pipeline reload.

## E-1 — Experiment

**Learning outcome:** LO3.

Replay best run từ config rồi đổi C.

**Expected output:** Replay probability allclose; C đổi làm config hash đổi; không yêu cầu metric bắt buộc đổi.
