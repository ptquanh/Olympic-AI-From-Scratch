# Team Roles — đội 2–3 người

Vai trò là ownership, không phải silo. Mọi thành viên phải hiểu metric, submission schema và best run hiện tại.

## Đội 3 người

| Vai                        | Trách nhiệm chính                               | Không được quên                                     |
| -------------------------- | ----------------------------------------------- | --------------------------------------------------- |
| A — Data/Validation        | EDA, split, leakage, metric, baseline tabular   | giữ một validation duy nhất làm chuẩn so sánh       |
| B — Modeling               | train/inference, architecture, tuning, ensemble | mỗi experiment phải có hypothesis và rollback point |
| C — Integration/Submission | notebook sạch, artifact, schema, experiment log | chạy end-to-end sớm và giữ bản submission hợp lệ    |

Sau khi baseline ổn, A/B có thể chia task theo expected value; C chuyển sang ensemble, sanity check và FINAL packaging.

## Đội 2 người

- **A:** Data + Validation + task ưu tiên 1.
- **B:** Modeling + Integration + task ưu tiên 2.
- Cả hai cùng review submission ở các checkpoint cố định.

## Checkpoint giao tiếp

Mỗi 30–45 phút, mỗi người chỉ báo bốn dòng:

1. Score/metric hiện tại.
2. Thay đổi vừa thử.
3. Kết luận giữ/bỏ.
4. Việc tiếp theo và thời gian dự kiến hoàn thành.

Không truyền notebook bằng cách copy thủ công qua nhiều phiên nếu có thể tránh. Một người giữ bản tích hợp chính; thay đổi cần được ghi trong experiment log trước khi merge vào final notebook.

## Quy tắc khi tranh luận

Ưu tiên evidence theo thứ tự: validation đáng tin → runtime thực tế → độ phức tạp tích hợp → trực giác. Khi hai hướng ngang nhau, chọn hướng cho kết quả kiểm chứng sớm hơn.
