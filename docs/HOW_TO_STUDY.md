# Hướng dẫn học Olympic AI From Scratch

## 1. Chọn track

- **Foundation Track:** đi theo thứ tự 00 → 05. Có thể bỏ qua mục `advanced` nhưng không bỏ prerequisite bắt buộc.
- **Contest Track:** làm diagnostic, ưu tiên Metrics & Validation, Feature Engineering, PyTorch Training Loop, CV/NLP competition labs và các mục được đánh dấu `contest: required` trong `curriculum.yml`.

Track chỉ thay đổi độ sâu và thứ tự, không thay đổi chuẩn đúng của kiến thức.

## 2. Đọc trạng thái trước khi học

- `drafted`: có thể học thử nhưng còn điểm cần review.
- `technically_reviewed`: toán, code, đáp án và notebook đã vượt quality gate kỹ thuật.
- `learner_tested`: đã có ít nhất một người thuộc target audience học thử.
- `published`: đã sửa theo learner feedback và sẵn sàng phát hành ổn định.

Không suy ra chất lượng từ việc “có đủ file”. Nguồn trạng thái duy nhất là `curriculum.yml`.

## 3. Quy trình cho một chương

1. **Prerequisite check:** trả lời 3–5 câu mà không tra tài liệu. Nếu chưa đạt, theo link về chương trước.
2. **Theory:** đọc problem/intuition, notation, derivation và worked example. Tự tính lại số nhỏ trên giấy.
3. **Notebook:** dự đoán output trước khi chạy. Với Core, chạy from-scratch trước framework và experiments.
4. **Recall:** đóng notebook, dùng `code_notes.md` để code lại pattern trong thời gian quy định.
5. **Exercises:** làm theo ID U → I → E → T → O. Chỉ mở `<details>` tương ứng trong solutions sau khi đã ghi lời giải của mình.
6. **Mastery check:** giải thích, derive, re-implement, predict, diagnose và apply. Core cần đạt ít nhất 4/6; Concept cần 2/3 Explain–Debug–Apply.

## 4. Ý nghĩa ID bài tập

| Prefix | Năng lực   | Expected output bắt buộc              |
| ------ | ---------- | ------------------------------------- |
| `U`    | Understand | Lập luận, công thức hoặc đáp số       |
| `I`    | Implement  | Hàm/API, shape, test case             |
| `E`    | Experiment | Hypothesis, metric, observation       |
| `T`    | Transfer   | Pipeline trên dữ liệu/bài toán mới    |
| `O`    | Olympiad   | Bài có timebox, metric và deliverable |

## 5. Runtime profiles

- **CPU smoke:** đặt `OAI_FAST_MODE=1`; dùng dữ liệu nhỏ và ít epoch để kiểm tra toàn bộ luồng.
- **GPU full:** dùng cấu hình đầy đủ được ghi trong notebook; chỉ bắt buộc cho các chương có `gpu_full: true`.
- **Competition-safe:** không tự cài package, không tải ngầm, dùng đúng cache và thư viện của profile kỳ thi.
- **Online learning:** phần cần tải dataset/model phải ghi `Network: required_first_run` hoặc `optional`, nguồn và cache location.

Notebook không có metadata hoặc không chạy `Restart & Run All` chưa được xem là hoàn thành.

## 6. Học để thi mà không học thuộc luật sai

Kiến thức mô hình và pipeline thường dùng chung; luật thi thì không. Bắt đầu từ [COMPETITION_PROFILES.md](COMPETITION_PROFILES.md). Khi gặp bảng phân bổ thời gian, danh sách thư viện hoặc chính sách LLM, kiểm tra đủ bốn trường: **kỳ thi – năm – nguồn – ngày xác minh**. Quy chế chính thức mới nhất luôn cao hơn mẹo hoặc tài liệu tham khảo cũ.

## 7. Ghi lại bằng chứng học

Với mỗi chương, lưu:

- đáp án prerequisite trước và sau khi học;
- notebook hoặc code viết lại không nhìn tài liệu;
- metric/plot của experiment;
- lỗi đã gặp và cách chẩn đoán;
- thời gian thực tế cho theory, code và exercises.

Những dữ liệu này giúp maintainer hiệu chỉnh time estimate và là đầu vào cần thiết trước khi chuyển chương từ `technically_reviewed` sang `learner_tested`.
