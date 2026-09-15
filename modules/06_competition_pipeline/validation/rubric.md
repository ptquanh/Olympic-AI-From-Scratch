# Rubric: Validation — Đo đúng khả năng tổng quát hóa

Chấm evidence từ [exercises](exercises.md), notebook và file outputs. Tổng 100 điểm; mỗi mục cho 0 nếu thiếu evidence, một nửa nếu chỉ hoàn thành một phần, đủ điểm khi đáp ứng toàn bộ điều kiện.

| Tiêu chí             | Điểm | Điều kiện lấy đủ điểm                                                                                       |
| -------------------- | ---: | ----------------------------------------------------------------------------------------------------------- |
| Data/EDA và split    |   25 | Schema, counts, nguồn feature rõ; validation đúng đơn vị; không leakage                                     |
| Baseline và contract |   20 | Restart & Run All chạy hết; CSV được đọc lại, đúng ID/thứ tự/class                                          |
| E-1: Experiment      |   25 | Bảng mean, sample std, OOF F1 và overlap; group overlap=0, coverage mọi dòng=1.                             |
| T-1: Transfer        |   15 | Vẽ ít nhất 3 cửa sổ train/gap/validation; chứng minh mọi feature và label train đã có trước mốc validation. |
| O-1: Olympiad        |   15 | Có fold assignment, coverage assertions, 128 dòng CSV đúng ID; nêu giới hạn score cho người mới.            |

- **Baseline (50–69):** pipeline chạy, metric đúng, artifact hợp lệ; cần bổ sung phân tích hoặc chuyển giao.
- **Good (70–89):** đủ baseline, thí nghiệm có kiểm soát và giải thích lựa chọn.
- **Excellent (90–100):** thêm chuyển giao đúng assumptions, chạy trong timebox và postmortem có bằng chứng.
- **Gate bắt buộc:** leakage, sử dụng label test, CSV sai schema/ID hoặc không replay được ⇒ chưa đạt bất kể tổng điểm.

Không chấm theo ngưỡng leaderboard cố định. Với dữ liệu synthetic, phát hiện một phương án không giúp tăng điểm vẫn là kết quả tốt nếu phép kiểm đúng.
