# Rubric: Debugging ML — Tìm lỗi bằng kiểm chứng nhỏ

Chấm evidence từ [exercises](exercises.md), notebook và file outputs. Tổng 100 điểm; mỗi mục cho 0 nếu thiếu evidence, một nửa nếu chỉ hoàn thành một phần, đủ điểm khi đáp ứng toàn bộ điều kiện.

| Tiêu chí             | Điểm | Điều kiện lấy đủ điểm                                                                                        |
| -------------------- | ---: | ------------------------------------------------------------------------------------------------------------ |
| Data/EDA và split    |   25 | Schema, counts, nguồn feature rõ; validation đúng đơn vị; không leakage                                      |
| Baseline và contract |   20 | Restart & Run All chạy hết; CSV được đọc lại, đúng ID/thứ tự/class                                           |
| E-1: Experiment      |   25 | Bad step tăng loss trên fixture; correct step giảm; có bảng hoặc plot được gắn nhãn đầy đủ.                  |
| T-1: Transfer        |   15 | Liệt kê logits/target shape, loss phù hợp, zero_grad→forward→loss→backward→step, train/eval và tiny-overfit. |
| O-1: Olympiad        |   15 | Gradient relative error <1e-6 trên fixture; tiny accuracy=1; 64 dòng id/label; postmortem nêu root cause.    |

- **Baseline (50–69):** pipeline chạy, metric đúng, artifact hợp lệ; cần bổ sung phân tích hoặc chuyển giao.
- **Good (70–89):** đủ baseline, thí nghiệm có kiểm soát và giải thích lựa chọn.
- **Excellent (90–100):** thêm chuyển giao đúng assumptions, chạy trong timebox và postmortem có bằng chứng.
- **Gate bắt buộc:** leakage, sử dụng label test, CSV sai schema/ID hoặc không replay được ⇒ chưa đạt bất kể tổng điểm.

Không chấm theo ngưỡng leaderboard cố định. Với dữ liệu synthetic, phát hiện một phương án không giúp tăng điểm vẫn là kết quả tốt nếu phép kiểm đúng.
