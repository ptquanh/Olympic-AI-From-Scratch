# Workflow 4h / 6h

`docs/COMPETITION_PROFILES.md` ghi Olympic AI PTIT 2026 có vòng sơ loại 4 giờ và vòng chung kết 6 giờ. Các mốc dưới đây là playbook cho profile đó; với kỳ thi khác, giữ **tỷ lệ thời gian** và thay luật cụ thể.

## 4 giờ — sơ loại

| Mốc       | Mục tiêu                             | Output bắt buộc                        |
| --------- | ------------------------------------ | -------------------------------------- |
| 0:00–0:20 | đọc đề, metric, file, constraints    | task board + owner + submission schema |
| 0:20–0:50 | EDA/split/baseline tối thiểu         | validation chạy được                   |
| 0:50–1:30 | submission đầu tiên                  | một file nộp hợp lệ                    |
| 1:30–2:40 | 2–3 experiment có hypothesis         | bảng score + quyết định keep/drop      |
| 2:40–3:20 | cải thiện có expected value cao nhất | best reproducible run                  |
| 3:20–3:40 | ensemble/tuning nhẹ nếu justified    | candidate cuối                         |
| 3:40–4:00 | freeze, rerun, đóng gói              | final notebook + submission + report   |

Nếu chưa có submission hợp lệ ở mốc 1:30, dừng tuning và sửa pipeline.

## 6 giờ — chung kết

| Mốc       | Mục tiêu                             | Output bắt buộc                     |
| --------- | ------------------------------------ | ----------------------------------- |
| 0:00–0:30 | triage toàn bộ task                  | priority + owner + risk             |
| 0:30–1:30 | baseline mọi task khả thi            | ít nhất một end-to-end path/task    |
| 1:30–3:30 | song song hóa experiment             | experiment log + score              |
| 3:30–4:45 | tập trung task có expected value cao | best candidate ổn định              |
| 4:45–5:20 | ensemble/error analysis cuối         | quyết định cuối dựa trên validation |
| 5:20–6:00 | freeze + rerun + FINAL               | artifact sạch và có thể tái lập     |

## Hai checkpoint không được bỏ

### Checkpoint 1 — sau baseline

- Submission có đúng số dòng/cột/tên file không?
- Validation có leakage không?
- Runtime full inference có nằm trong giới hạn không?
- Có lưu seed/config/version của best run không?

### Checkpoint 2 — trước freeze

- Best score có tái lập từ notebook sạch không?
- Model/artifact final có đúng file mà notebook đang dùng không?
- Không còn path tuyệt đối, state ẩn hoặc cell phải chạy thủ công ngoài thứ tự.
- Một thành viên khác đã review output cuối.
