# Validation — Đo đúng khả năng tổng quát hóa

> **Loại:** Competition Lab
> **Track:** Foundation ⭐ | Contest ⭐
> **Thời gian học ước tính:** 3 giờ (theory: 0.75h, code: 1.25h, exercises: 1h)
> **Profile mặc định:** general · CPU · offline · dữ liệu mô phỏng tự tạo.
> **Trạng thái:** technically_reviewed; chưa có learner testing. Xem [manifest](../../../curriculum.yml).

## Prerequisite Check

1. Fit scaler trước split có thể làm rò rỉ gì?
2. Stratification giữ đặc điểm nào của label?
3. Khi dự đoán người mới, đơn vị độc lập là dòng hay người?

Nếu chưa trả lời được, quay lại [EDA](../eda/README.md) và [Metrics & Validation](../../01_machine_learning/metrics_and_validation/README.md).

## Learning Outcomes

- [ ] LO1: Chọn K-fold, stratified, group hoặc time split theo đơn vị dự đoán.
- [ ] LO2: Tạo OOF predictions có mỗi dòng đúng một lần và pipeline fit riêng từng fold.
- [ ] LO3: Báo cáo mean/spread và phát hiện split có leakage bằng assert.

## Concept Map

```text
EDA + Metrics & Validation → Validation → Ensembling + Experiment Tracking
                              └→ baseline chạy lại được trong phòng thi
```

## 1. Intuition — Tại sao cần?

Một người có bốn bản ghi gần giống nhau. Nếu ba bản nằm trong train, model có thể nhớ người đó để đoán bản còn lại. Validation (tập kiểm định để lựa chọn phương án) chỉ hữu ích khi mô phỏng đúng dữ liệu bạn sẽ gặp: người mới, dòng độc lập hay thời điểm tương lai.

## 2. Math & Derivation

Với K fold không giao nhau, gọi s_k là điểm fold k. Mean = sum(s_k)/K, spread ở đây là độ lệch chuẩn mẫu sqrt(sum((s_k-mean)^2)/(K-1)). Spread không phải confidence interval vì các tập train của fold giao nhau. OOF (out-of-fold) gán dự đoán cho dòng i bằng model không train trên dòng i; với group data, model cũng không train trên group của i. Macro F1 của toàn bộ OOF không bắt buộc bằng trung bình F1 các fold do F1 là tỷ số phi tuyến.

## 3. Worked Example

Ba bệnh nhân A,B,C có hai dòng/người. Fold 1 giữ A, fold 2 giữ B, fold 3 giữ C. Sáu dòng được nhận một dự đoán OOF. Nếu điểm fold là 0.6, 0.8, 1.0 thì mean=0.8 và sample std=0.2. Với timeline `[1,2,3,4,5,6]`, train `[1,2,3]`, gap `[4]`, validation `[5,6]` phù hợp dự báo tương lai hơn xáo trộn thời gian.

## 4. Shape Analysis

X `(n,d)`; fold_id `(n,)`; OOF probability `(n,2)`; mỗi row có coverage=1. Trong time split, prefix chỉ dùng train có thể không được dự đoán; không áp coverage=1 cho toàn timeline.

## 5. Complexity

K-fold cần K lần fit cho một cấu hình; lưu OOF tốn O(n·C) với C class. GroupKFold giữ người không giao nhau nhưng không đảm bảo class balance; cần xem counts từng fold.

## Problem, Data & Submission

120/240 group, mỗi group 4 dòng. Label cố định theo group, feature nhận diện ngẫu nhiên theo người; dữ liệu được tạo để minh họa ghi nhớ. Public test là 32 người mới (128 dòng). Notebook còn có bảng thời gian nhỏ độc lập để kiểm tra TimeSeriesSplit.

**Metric:** Macro F1 cho từng fold và toàn OOF, labels=[0,1]. Báo mean ± sample std và group overlap. Test synthetic không có nhãn nên không báo điểm test.

**Validation:** So sánh StratifiedKFold với GroupKFold bằng cùng KNN pipeline và cùng dữ liệu. Đó là so sánh hai cách ước lượng, không phải chọn split có điểm cao nhất. KFold dùng khi dòng i.i.d.; StratifiedKFold thêm cân bằng nhãn nhưng không tách group; TimeSeriesSplit cần dữ liệu đã sort và gap phù hợp độ trễ label.

Pipeline bắt buộc: Data → EDA → Preprocess → Model → Train → Evaluate → Submit. Submission lab là `outputs/submission_starter.csv` hoặc `outputs/submission_solution.csv`, cột `id,label`, một dòng mỗi test ID theo đúng thứ tự đầu vào. Đó là contract mô phỏng; khi thi phải thay bằng schema của đề.

## 6. From-Scratch & Framework

Không tạo bộ ba notebook Core vì đây là Competition Lab. Các phép tính nhỏ trong worked example được đối chiếu bằng code; trọng tâm là dùng và debug pipeline. Thực hành theo [starter.ipynb](starter.ipynb) → [solution.ipynb](solution.ipynb). Notebook tự đủ setup/data, không cần chạy chương khác trước.

Starter có baseline chạy hết, các TODO là phần bạn phải cải thiện. Solution triển khai reference đầy đủ và giải thích lựa chọn. Dùng thư viện có sẵn trong [environment](../../../envs/requirements.txt), thuộc nhóm được liệt kê trong rules; quyền dùng trong kỳ thi cụ thể lấy từ [competition profile](../../../docs/COMPETITION_PROFILES.md). Không tự cài package hay tải dữ liệu.

## 7. Experiments — Predict → Run → Explain

Dự đoán: random-row CV sẽ được lợi từ bản ghi gần trùng. Solution ghi cả điểm lẫn số group giao nhau và minh họa split thời gian có gap. Không ép group score phải lớn hơn baseline; ở dữ liệu này khả năng đoán người mới vốn rất thấp.

Ghi theo năm bước: **Hypothesis → Code → Result → Observation → Why**. Result phải là số/plot thực chạy; Observation phân biệt bằng chứng và giả thuyết. Mọi plot cần title, axis labels và legend. Kết quả synthetic chỉ minh họa cơ chế, không dự báo leaderboard.

## 8. Common Mistakes & Misconceptions

> ❌ **Sai:** StratifiedKFold ngăn mọi leakage.
> ✅ **Đúng:** Nó giữ tỷ lệ class, không tách người hoặc thứ tự thời gian.

> ❌ **Sai:** CV std là sai số tin cậy của điểm cuối.
> ✅ **Đúng:** Các lần fit phụ thuộc nhau; ghi spread mô tả, không gọi confidence interval.

> ❌ **Sai:** OOF nghĩa là feature engineering trước CV cũng được.
> ✅ **Đúng:** Mỗi transformer có fit phải nằm trong pipeline riêng mỗi fold.

## 9. Code Notes

Đọc [code_notes.md](code_notes.md), đóng tài liệu rồi làm ít nhất hai bài code tay. Tự kiểm tra bằng assert trước khi so reference.

## 10. Exercises

Làm [exercises.md](exercises.md) theo tầng Experiment, Transfer, Olympiad; chấm bằng [rubric](rubric.md) và điền [postmortem](postmortem.md). Đáp án có thể mở riêng từng bài tại [solutions.md](solutions.md).

## 11. Olympiad Transfer & Connections

Khi đề yêu cầu pipeline có thể chạy lại hoặc cung cấp notebook starter, áp dụng chương này trước khi tăng độ phức tạp model. Baseline tối thiểu là chạy notebook và kiểm tra file nộp; dành khoảng 15–20 phút sau khi đã chuẩn bị môi trường. Nếu row CV cao còn group CV thấp, pipeline có thể đang nhớ group. Group score thấp là thông tin về bài toán; không được đổi về row split để làm báo cáo đẹp.

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
