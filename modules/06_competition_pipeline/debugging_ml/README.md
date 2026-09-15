# Debugging ML — Tìm lỗi bằng kiểm chứng nhỏ

> **Loại:** Competition Lab
> **Track:** Foundation ⭐ | Contest ⭐
> **Thời gian học ước tính:** 3 giờ (theory: 0.75h, code: 1.25h, exercises: 1h)
> **Profile mặc định:** general · CPU · offline · dữ liệu mô phỏng tự tạo.
> **Trạng thái:** technically_reviewed; chưa có learner testing. Xem [manifest](../../../curriculum.yml).

## Prerequisite Check

1. Gradient descent cập nhật dấu cộng hay trừ?
2. Logits khác probability ở đâu?
3. Broadcast `(n,1)` với `(n,)` tạo ra shape gì?

Nếu chưa trả lời được, quay lại [Validation](../validation/README.md) và [Backprop & Training Loop](../../02_deep_learning/backprop_training_loop/README.md).

## Learning Outcomes

- [ ] LO1: Khoanh vùng lỗi data, shape, loss và update bằng kiểm tra tối thiểu.
- [ ] LO2: So sánh gradient giải tích với finite differences trên batch nhỏ.
- [ ] LO3: Chứng minh training loop học được batch dễ trước khi chạy đầy đủ.

## Concept Map

```text
Backprop & Training Loop + Validation → Debugging ML → Experiment Tracking
                              └→ baseline chạy lại được trong phòng thi
```

## 1. Intuition — Tại sao cần?

Loss không giảm có thể do dữ liệu, dấu gradient hoặc learning rate. Đổi sang model lớn hơn không xác định được nguyên nhân. Debugging là đặt câu hỏi có thể kiểm chứng: loss ban đầu đúng không, gradient đúng không, weight có đổi không, một batch đơn giản có học được không?

## 2. Math & Derivation

Với logit z_i=x_i·w+b, probability p_i=1/(1+exp(-z_i)), binary cross-entropy viết ổn định là logaddexp(0,z_i)-y_i·z_i. Đạo hàm theo z là p_i-y_i vì đạo hàm log(1+exp(z)) bằng sigmoid(z). Do z tuyến tính theo w, g_w=X.T@(p-y)/n và g_b=mean(p-y). Taylor hai phía cho L(w+h e_j)-L(w-h e_j)=2h·g_j+O(h^3); chia 2h được gradient số sai số O(h^2). Đo sai khác tương đối bằng norm(g-g_num)/max(1e-12,norm(g)+norm(g_num)).

## 3. Worked Example

X=[[-1],[1]], y=[0,1], w=b=0. Logit=0, p=[0.5,0.5], loss=log(2)≈0.693147. g_w=((-1)·0.5+1·(-0.5))/2=-0.5, g_b=0. Với lr=0.1, w_new=0.05. Hai probability dịch về đúng phía. Nếu dùng dấu cộng thì w=-0.05, loss tăng.

## 4. Shape Analysis

X `(n,d)`, w `(d,)`, z/y/p `(n,)`, gradient w `(d,)`. Giữ y một chiều: `(n,1)-(n,)` sẽ broadcast thành `(n,n)` và âm thầm đổi objective.

## 5. Complexity

Gradient giải tích O(n·d), finite differences mọi tọa độ khoảng O(n·d²). Chỉ dùng batch nhỏ và vài tọa độ trên mạng lớn; gradcheck không phải vòng train.

## Problem, Data & Submission

Tabular synthetic hai feature, nhãn phân tách tuyến tính kèm noise nhỏ; 160/400 dòng có nhãn và 64 test rows. Batch diagnostic riêng hai điểm đối xứng được tạo để có đáp số tính tay.

**Metric:** Macro F1 để so sánh baseline/reference; thêm BCE loss và relative gradient error để chẩn đoán. Tiny batch đạt accuracy=1 chỉ chứng minh loop học được case dễ, không chứng minh generalization.

**Validation:** Stratified hold-out 25%, scaler chỉ fit train. Batch gradient check và tiny-overfit dùng training hoặc fixture riêng; không fit theo y_validation. Seed 42, float64 cho kiểm tra số.

Pipeline bắt buộc: Data → EDA → Preprocess → Model → Train → Evaluate → Submit. Submission lab là `outputs/submission_starter.csv` hoặc `outputs/submission_solution.csv`, cột `id,label`, một dòng mỗi test ID theo đúng thứ tự đầu vào. Đó là contract mô phỏng; khi thi phải thay bằng schema của đề.

## 6. From-Scratch & Framework

Không tạo bộ ba notebook Core vì đây là Competition Lab. Các phép tính nhỏ trong worked example được đối chiếu bằng code; trọng tâm là dùng và debug pipeline. Thực hành theo [starter.ipynb](starter.ipynb) → [solution.ipynb](solution.ipynb). Notebook tự đủ setup/data, không cần chạy chương khác trước.

Starter có baseline chạy hết, các TODO là phần bạn phải cải thiện. Solution triển khai reference đầy đủ và giải thích lựa chọn. Dùng thư viện có sẵn trong [environment](../../../envs/requirements.txt), thuộc nhóm được liệt kê trong rules; quyền dùng trong kỳ thi cụ thể lấy từ [competition profile](../../../docs/COMPETITION_PROFILES.md). Không tự cài package hay tải dữ liệu.

## 7. Experiments — Predict → Run → Explain

Dự đoán chiều thay đổi loss khi cố ý update dấu cộng. Notebook đo bad-step loss > initial, correct-step loss < initial trên worked fixture; fault được kiểm soát nên Restart & Run All vẫn pass. Sweep learning rate `[0.01,0.1,1.0]` và vẽ loss train; không chọn theo test.

Ghi theo năm bước: **Hypothesis → Code → Result → Observation → Why**. Result phải là số/plot thực chạy; Observation phân biệt bằng chứng và giả thuyết. Mọi plot cần title, axis labels và legend. Kết quả synthetic chỉ minh họa cơ chế, không dự báo leaderboard.

## 8. Common Mistakes & Misconceptions

> ❌ **Sai:** Loss giảm nghĩa là mọi gradient đúng.
> ✅ **Đúng:** Một số lỗi vẫn làm loss giảm; đối chiếu finite difference trên case không suy biến.

> ❌ **Sai:** Gradient càng gần 0 càng tốt.
> ✅ **Đúng:** Có thể bị đứt graph hoặc saturation; kiểm tra parameter update và tiny-overfit.

> ❌ **Sai:** Batch dễ học được thì bài thi sẽ điểm cao.
> ✅ **Đúng:** Đó là sanity check cho loop; validation độc lập mới đo generalization.

## 9. Code Notes

Đọc [code_notes.md](code_notes.md), đóng tài liệu rồi làm ít nhất hai bài code tay. Tự kiểm tra bằng assert trước khi so reference.

## 10. Exercises

Làm [exercises.md](exercises.md) theo tầng Experiment, Transfer, Olympiad; chấm bằng [rubric](rubric.md) và điền [postmortem](postmortem.md). Đáp án có thể mở riêng từng bài tại [solutions.md](solutions.md).

## 11. Olympiad Transfer & Connections

Khi đề yêu cầu pipeline có thể chạy lại hoặc cung cấp notebook starter, áp dụng chương này trước khi tăng độ phức tạp model. Baseline tối thiểu là chạy notebook và kiểm tra file nộp; dành khoảng 15–20 phút sau khi đã chuẩn bị môi trường. Fixture của lab xác định lỗi dấu update. Nếu dữ liệu thật có NaN, sai shape hoặc label mapping, cần sửa những lỗi đó trước; không gán mọi loss tăng cho learning rate.

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
