# EDA — Khám phá dữ liệu trước baseline

> **Loại:** Competition Lab
> **Track:** Foundation ⭐ | Contest ⭐
> **Thời gian học ước tính:** 3 giờ (theory: 0.75h, code: 1.25h, exercises: 1h)
> **Profile mặc định:** general · CPU · offline · dữ liệu mô phỏng tự tạo.
> **Trạng thái:** technically_reviewed; chưa có learner testing. Xem [manifest](../../../curriculum.yml).

## Prerequisite Check

1. `isna().mean()` đo tỷ lệ gì và xử lý mẫu số như thế nào?
2. Vì sao ID bệnh nhân không nên tự động được coi là feature?
3. Macro F1 khác accuracy khi class mất cân bằng ở đâu?

Nếu chưa trả lời được, quay lại [NumPy & Pandas](../../00_foundations/numpy_pandas/README.md) và [Metrics & Validation](../../01_machine_learning/metrics_and_validation/README.md).

## Learning Outcomes

- [ ] LO1: Lập báo cáo schema, missing, duplicate và class balance có số liệu.
- [ ] LO2: Phát hiện feature xuất hiện sau thời điểm dự đoán và kiểm tra group overlap.
- [ ] LO3: Xuất baseline cùng bảng giả thuyết có phép kiểm chứng.

## Concept Map

```text
NumPy/Pandas + Metrics & Validation → EDA → Validation → Debugging ML
                              └→ baseline chạy lại được trong phòng thi
```

## 1. Intuition — Tại sao cần?

Bạn nhận bảng khám bệnh có nhiều lần đo trên cùng người. Một cột kết quả xét nghiệm sau chẩn đoán gần như trùng label. Điểm cao từ cột này không giúp dự đoán ở thời điểm tiếp nhận. EDA (Exploratory Data Analysis, khám phá dữ liệu) phải kết hợp thống kê với ý nghĩa và thời điểm thu thập từng cột.

## 2. Math & Derivation

Với cột j có n dòng, đặt m_ij = 1 nếu ô i thiếu và 0 nếu có giá trị. Tổng các chỉ báo đếm ô thiếu, nên tỷ lệ r_j = sum_i(m_ij)/n. Với class c, p_c = n_c/n. Đếm duplicate cần xác định khóa: trùng toàn bộ dòng khác với cùng bệnh nhân ở hai lần khám. Correlation (tương quan) chỉ đo liên hệ; cột tương quan cao vẫn cần kiểm tra có sẵn lúc inference (dự đoán) hay không.

## 3. Worked Example

Bốn dòng có patient_id `[A,A,B,C]`, tuổi `[20,20,40,NaN]`, nhãn `[0,0,1,0]`. Missing tuổi = 1/4 = 25%; tỷ lệ class 1 = 1/4. Nếu hai dòng A là cùng bản ghi bị nhân đôi thì có 1 duplicate vượt bản gốc. Nếu là hai lần khám khác nhau, giữ cả hai nhưng không để A xuất hiện ở cả train và validation. Cột `after_event = label` có độ khớp 100% nhưng bị loại vì được tạo sau sự kiện.

## 4. Shape Analysis

Bảng raw có n dòng; feature số sau chọn cột có shape `(n, 2)`, label `(n,)`, xác suất hai class `(n, 2)`. ID chỉ dùng để join và kiểm tra submission.

## 5. Complexity

Profiling các ô mất O(n·d). Histogram dùng số bins cố định. Với dữ liệu lớn, tổng hợp missing trên toàn dữ liệu theo chunk rồi xem mẫu phân tầng; một mẫu nhỏ không chứng minh toàn bộ dữ liệu sạch.

## Problem, Data & Submission

Dữ liệu synthetic (mô phỏng) trong notebook: 120/240 bệnh nhân, mỗi người 3 lần đo, hai feature, cột sau sự kiện và 3 dòng bị nhân đôi. Public test có 24 người mới, 72 dòng và không có label. Dữ liệu do code tạo, không cần download hay tài sản bên thứ ba.

**Metric:** Macro F1: tính F1 riêng từng class rồi trung bình để mỗi class có trọng số bằng nhau. Dùng labels=[0,1], zero_division=0. Đây là metric của lab mô phỏng, không phải luật chung mọi đề.

**Validation:** Dedupe đúng các bản ghi nhân đôi trước khi chia. Dùng GroupShuffleSplit theo patient_id; assert tập người không giao nhau. Fit imputer/scaler chỉ trên train. Label validation chỉ dùng evaluate. Không dùng `after_event`, patient_id hoặc row ID làm feature.

Pipeline bắt buộc: Data → EDA → Preprocess → Model → Train → Evaluate → Submit. Submission lab là `outputs/submission_starter.csv` hoặc `outputs/submission_solution.csv`, cột `id,label`, một dòng mỗi test ID theo đúng thứ tự đầu vào. Đó là contract mô phỏng; khi thi phải thay bằng schema của đề.

## 6. From-Scratch & Framework

Không tạo bộ ba notebook Core vì đây là Competition Lab. Các phép tính nhỏ trong worked example được đối chiếu bằng code; trọng tâm là dùng và debug pipeline. Thực hành theo [starter.ipynb](starter.ipynb) → [solution.ipynb](solution.ipynb). Notebook tự đủ setup/data, không cần chạy chương khác trước.

Starter có baseline chạy hết, các TODO là phần bạn phải cải thiện. Solution triển khai reference đầy đủ và giải thích lựa chọn. Dùng thư viện có sẵn trong [environment](../../../envs/requirements.txt), thuộc nhóm được liệt kê trong rules; quyền dùng trong kỳ thi cụ thể lấy từ [competition profile](../../../docs/COMPETITION_PROFILES.md). Không tự cài package hay tải dữ liệu.

## 7. Experiments — Predict → Run → Explain

Dự đoán: thêm `after_event` sẽ làm điểm validation tăng giả tạo. Solution đo baseline sạch và nhánh cố ý có leakage trên cùng split; chỉ baseline sạch được refit để nộp. Lập ba giả thuyết từ missing, class balance và shift; mỗi giả thuyết phải có một phép kiểm chứng.

Ghi theo năm bước: **Hypothesis → Code → Result → Observation → Why**. Result phải là số/plot thực chạy; Observation phân biệt bằng chứng và giả thuyết. Mọi plot cần title, axis labels và legend. Kết quả synthetic chỉ minh họa cơ chế, không dự báo leaderboard.

## 8. Common Mistakes & Misconceptions

> ❌ **Sai:** Correlation cao nghĩa là feature tốt.
> ✅ **Đúng:** Kiểm tra nguồn gốc và thời điểm; cột sau sự kiện bị loại dù điểm cao.

> ❌ **Sai:** Trùng bệnh nhân nghĩa là xóa dòng.
> ✅ **Đúng:** Chỉ xóa bản ghi bị lặp thật; các lần đo khác nhau cần group split.

> ❌ **Sai:** EDA trên toàn bảng rồi tune theo mọi label là an toàn.
> ✅ **Đúng:** Schema có thể xem toàn bảng; phân tích liên hệ target phục vụ lựa chọn model phải nằm trong train.

## 9. Code Notes

Đọc [code_notes.md](code_notes.md), đóng tài liệu rồi làm ít nhất hai bài code tay. Tự kiểm tra bằng assert trước khi so reference.

## 10. Exercises

Làm [exercises.md](exercises.md) theo tầng Experiment, Transfer, Olympiad; chấm bằng [rubric](rubric.md) và điền [postmortem](postmortem.md). Đáp án có thể mở riêng từng bài tại [solutions.md](solutions.md).

## 11. Olympiad Transfer & Connections

Khi đề yêu cầu pipeline có thể chạy lại hoặc cung cấp notebook starter, áp dụng chương này trước khi tăng độ phức tạp model. Baseline tối thiểu là chạy notebook và kiểm tra file nộp; dành khoảng 15–20 phút sau khi đã chuẩn bị môi trường. Điểm tăng mạnh khi thêm after_event là phản ví dụ có chủ đích; quyết định đúng là bỏ cột. Nếu group overlap khác 0, quay về split trước khi chỉnh model.

Sau baseline: (1) xác nhận data/split/metric; (2) thử một giả thuyết có log; (3) đóng băng phương án và chạy lại inference. Profile general dùng khoảng 10% thời gian đọc đề/EDA, 20% baseline, 50% thí nghiệm, 20% kiểm tra và nộp. Đây là gợi ý luyện tập, không phải lịch chính thức 4h/6h của bất kỳ kỳ thi nào.

## 12. References

Nguồn cho API, phương pháp và bài đọc mở rộng nằm trong [references.md](references.md). Quy chế hiện hành luôn ưu tiên thông báo đúng mùa thi.

## 13. Mastery Check

- [ ] Explain: giải thích worked example mà không mở tài liệu.
- [ ] Debug: tạo và phát hiện một lỗi trong phần misconceptions.
- [ ] Apply: hoàn thành bài O-1 trong timebox, đúng submission contract và có postmortem.

Đạt khi artifact chạy lại được, đúng split/metric và rubric ≥70/100; score cao không bù được leakage.

## 14. Time Estimate

Theory: ~0.75h; Code: ~1.25h; Exercises: ~1h. Runtime notebook: thường dưới 1 phút trên CPU cho fast mode, dự trù dưới 2 phút chế độ đầy đủ trên máy học tập/Colab CPU; đây là ước lượng, không phải benchmark Colab đã đo. Ghi thời gian học thực tế để phản hồi learner testing.

[← Module 06](../MODULE_README.md)
