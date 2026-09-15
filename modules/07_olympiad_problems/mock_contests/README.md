# Mock Contests

Mock contest là **playlist link**, không chứa lại đề hoặc dataset. Tải tài liệu từ nguồn chính thức trước giờ mock theo đúng điều khoản của nguồn.

## Playlist có sẵn

- [Mock 01 — Foundation 4h](mock_01_foundation_4h.md)
- [Mock 02 — Mixed 4h](mock_02_mixed_4h.md)
- [Mock 03 — Final Simulation 6h](mock_03_final_6h.md)

## Mock 4 giờ — baseline discipline

- 0:00–0:20: đọc toàn bộ task, metric, submission schema.
- 0:20–1:10: EDA + validation + baseline task A.
- 1:10–2:00: baseline task B.
- 2:00–3:00: error analysis, chọn đúng **một** hướng cải thiện/task.
- 3:00–3:35: ensemble hoặc tuning chỉ khi validation ổn định.
- 3:35–4:00: Restart & Run All, kiểm tra file nộp, chốt report.

## Mock 6 giờ — final simulation

- 0:00–0:30: triage 3 task, chia thứ tự ưu tiên.
- 0:30–2:30: tạo baseline hợp lệ cho cả ba.
- 2:30–4:30: tập trung 1–2 task có expected value cao nhất.
- 4:30–5:20: ensemble/robustness/error analysis.
- 5:20–6:00: freeze code, rerun sạch, đóng gói FINAL.

## Scoring sau mock

Chấm cả score lẫn quy trình: có baseline sớm không, split đúng không, log có tái lập không, notebook có chạy sạch không, và có nộp đúng schema không.

Sau mock, điền `../postmortem_template.md` và cập nhật `_dev/real_problem_log.md`.
