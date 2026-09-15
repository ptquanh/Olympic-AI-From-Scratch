# Ensembling — Averaging, Blending và Stacking

> **Loại:** Competition Lab
> **Track:** Foundation 📖 | Contest ⭐
> **Thời gian học ước tính:** 3 giờ (theory: 0.75h, code: 1.25h, exercises: 1h)
> **Profile mặc định:** general · CPU · offline · dữ liệu mô phỏng tự tạo.
> **Trạng thái:** technically_reviewed; chưa có learner testing. Xem [manifest](../../../curriculum.yml).

## Prerequisite Check

1. Probability hai model có cùng thứ tự class chưa?
2. OOF predictions được tạo như thế nào?
3. Vì sao fit meta-model trên in-sample predictions gây rò rỉ?

Nếu chưa trả lời được, quay lại [Validation](../validation/README.md) và [Tree Ensembles](../../01_machine_learning/tree_ensembles/README.md).

## Learning Outcomes

- [ ] LO1: Gộp probability theo đúng ID và class order.
- [ ] LO2: Xây blending trên hold-out và stacking trên OOF.
- [ ] LO3: So sánh chất lượng, lỗi chung và chi phí trước khi chọn ensemble.

## Concept Map

```text
Validation + Tree Ensembles → Ensembling → Experiment Tracking → Timed Mock
                              └→ baseline chạy lại được trong phòng thi
```

## 1. Intuition — Tại sao cần?

Hai model cùng sai trên mọi mẫu thì gộp chúng ít giúp ích. Ensemble (tổ hợp mô hình) hữu ích khi mỗi model mang thông tin khác nhau. Averaging dùng trọng số cố định; blending học trọng số trên một tập giữ riêng; stacking học meta-model từ dự đoán OOF.

## 2. Math & Derivation

Với M model và a_m>=0, sum a_m=1, pbar_ic=sum_m a_m·p_mic. Tổng probability mỗi dòng vẫn là 1 vì sum_c pbar_ic=sum_m a_m·1=1. Nếu hai sai số có cùng variance sigma² và correlation rho, variance của trung bình là (sigma²+sigma²+2rho sigma²)/4=sigma²(1+rho)/2; đây là trực giác cho averaging, không phải bảo đảm F1 tăng. Stacking binary dùng Z_im=p_m(y=1|x_i) tạo shape (n,M), rồi fit logistic meta-model trên Z_OOF.

## 3. Worked Example

Hai model cho class 1 `[0.8,0.4]`, trọng số `[0.25,0.75]`: p=0.25·0.8+0.75·0.4=0.5. Lab quy ước p>=0.5 là class 1; argmax hai class có thể xử lý hòa khác nên cần khóa quy ước. Nếu model B lưu cột class `[1,0]`, phải reorder trước khi lấy cột class 1.

## 4. Shape Analysis

OOF Z `(n_train,2)`, meta-model predict probability `(n_val,2)`. Không flatten mảng `(model,row,class)` rồi vô tình trộn ID. Lab dùng hai class `[0,1]` và assert classes_ cho mỗi model.

## 5. Complexity

Stacking cần K·M fits tạo OOF rồi M fits full-train. Blending giữ thêm dữ liệu nên base models có ít mẫu học hơn. Chi phí inference ít nhất tổng các base models; lab ghi latency thực đo và không khẳng định ensemble luôn đáng nộp.

## Problem, Data & Submission

400/800 labeled synthetic rows, 8 feature, quan hệ phi tuyến; 80 test rows không nhãn. Base models là scaled logistic regression và random forest, dùng sklearn có sẵn trong environment.

**Metric:** Macro F1 cho metric bài tập; log loss để chọn blending weight trong inner hold-out. Quy ước probability class 1>=0.5. Báo latency inference và tỷ lệ hai model cùng sai trên validation.

**Validation:** Outer hold-out 25% dành so sánh cuối của thí nghiệm. Stacking tạo OOF chỉ trong outer-train. Blending tách riêng blend set từ outer-train; chọn weight bằng log loss trên blend, rồi giữ đúng base models đó để đánh giá. Không fit meta-model hoặc weight bằng outer-validation. Sau khi chọn cách nộp bằng outer-validation, score này là development score, không phải đánh giá cuối độc lập.

Pipeline bắt buộc: Data → EDA → Preprocess → Model → Train → Evaluate → Submit. Submission lab là `outputs/submission_starter.csv` hoặc `outputs/submission_solution.csv`, cột `id,label`, một dòng mỗi test ID theo đúng thứ tự đầu vào. Đó là contract mô phỏng; khi thi phải thay bằng schema của đề.

## 6. From-Scratch & Framework

Không tạo bộ ba notebook Core vì đây là Competition Lab. Các phép tính nhỏ trong worked example được đối chiếu bằng code; trọng tâm là dùng và debug pipeline. Thực hành theo [starter.ipynb](starter.ipynb) → [solution.ipynb](solution.ipynb). Notebook tự đủ setup/data, không cần chạy chương khác trước.

Starter có baseline chạy hết, các TODO là phần bạn phải cải thiện. Solution triển khai reference đầy đủ và giải thích lựa chọn. Dùng thư viện có sẵn trong [environment](../../../envs/requirements.txt), thuộc nhóm được liệt kê trong rules; quyền dùng trong kỳ thi cụ thể lấy từ [competition profile](../../../docs/COMPETITION_PROFILES.md). Không tự cài package hay tải dữ liệu.

## 7. Experiments — Predict → Run → Explain

Dự đoán averaging có thể tốt hơn hoặc kém base tốt nhất. Solution so sánh logistic, forest, mean, blend, stack. Chọn phương án theo validation; nếu hòa chọn phương án ít model hơn. Không khẳng định ensemble phải thắng.

Ghi theo năm bước: **Hypothesis → Code → Result → Observation → Why**. Result phải là số/plot thực chạy; Observation phân biệt bằng chứng và giả thuyết. Mọi plot cần title, axis labels và legend. Kết quả synthetic chỉ minh họa cơ chế, không dự báo leaderboard.

## 8. Common Mistakes & Misconceptions

> ❌ **Sai:** Trung bình nhãn 0/1 là soft voting.
> ✅ **Đúng:** Soft voting gộp probability; nhãn cứng làm mất confidence.

> ❌ **Sai:** Fit meta-model trên output train là stacking hợp lệ.
> ✅ **Đúng:** Dùng OOF để mỗi meta-feature được tạo khi dòng đó không nằm trong base training.

> ❌ **Sai:** Blend weight tốt nhất trên test có thể dùng.
> ✅ **Đúng:** Test không có nhãn; chỉ chọn weight trên inner hold-out được phân bổ trước.

## 9. Code Notes

Đọc [code_notes.md](code_notes.md), đóng tài liệu rồi làm ít nhất hai bài code tay. Tự kiểm tra bằng assert trước khi so reference.

## 10. Exercises

Làm [exercises.md](exercises.md) theo tầng Experiment, Transfer, Olympiad; chấm bằng [rubric](rubric.md) và điền [postmortem](postmortem.md). Đáp án có thể mở riêng từng bài tại [solutions.md](solutions.md).

## 11. Olympiad Transfer & Connections

Khi đề yêu cầu pipeline có thể chạy lại hoặc cung cấp notebook starter, áp dụng chương này trước khi tăng độ phức tạp model. Baseline tối thiểu là chạy notebook và kiểm tra file nộp; dành khoảng 15–20 phút sau khi đã chuẩn bị môi trường. Stacking có thể kém forest trên dataset nhỏ do meta-feature nhiễu và OOF distribution khác full-train prediction. Đó là kết quả hợp lệ; không đổi split để ép ensemble thắng.

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
