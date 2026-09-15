# Public Test — Pseudo-labeling và Test-Time Augmentation

> **Loại:** Concept Lesson
> **Track:** Foundation 📖 | Contest ⭐
> **Thời gian học ước tính:** 3 giờ (theory: 0.75h, code: 1.25h, exercises: 1h)
> **Profile mặc định:** general · CPU · offline · dữ liệu mô phỏng tự tạo.
> **Trạng thái:** technically_reviewed; chưa có learner testing. Xem [manifest](../../../curriculum.yml).

## Prerequisite Check

1. Unlabeled data khác validation có nhãn ở đâu?
2. Vì sao confidence 0.95 không đảm bảo 95% nhãn đúng?
3. Một phép lật ảnh có luôn giữ nguyên label không?

Nếu chưa trả lời được, quay lại [Validation](../validation/README.md) và [Augmentation](../../03_computer_vision/augmentation/README.md).

## Learning Outcomes

- [ ] LO1: Phân biệt dữ liệu công khai được cấp với việc tìm nhãn test.
- [ ] LO2: Cài pseudo-labeling một vòng có ngưỡng và xử lý trường hợp không chọn mẫu.
- [ ] LO3: So sánh baseline, pseudo-label và TTA trên validation có nhãn được giữ riêng.

## Concept Map

```text
Validation + Augmentation → Public Test → Ensembling
                              └→ baseline chạy lại được trong phòng thi
```

## 1. Intuition — Tại sao cần?

Bạn có ít nhãn nhưng nhiều input không nhãn được cấp trong đề. Pseudo-labeling (gán nhãn giả) dùng dự đoán của model làm mục tiêu huấn luyện bổ sung. TTA (Test-Time Augmentation, biến đổi đầu vào lúc dự đoán) lấy nhiều góc nhìn hợp lệ rồi gộp dự đoán. Cả hai chỉ có ích nếu giả định về dữ liệu đúng; nhãn giả sai có thể củng cố lỗi.

## 2. Math & Derivation

Gọi p_ic là xác suất class c của mẫu i. Chọn mask m_i = 1[max_c p_ic >= tau], gán nhãn yhat_i=argmax_c p_ic. Training bổ sung tối thiểu hóa L = (sum_l CE(y,p) + alpha·sum_u m_i CE(yhat,p))/(n_l + alpha·sum_u m_i), alpha điều chỉnh trọng số nhãn giả. Lab dùng alpha=1 để dễ đọc; khi m toàn 0, giữ baseline. TTA với M phép biến đổi giữ label cho pbar(x)=sum_m p(T_m(x))/M. Trung bình probability trước argmax; với segmentation phải biến đổi ngược tọa độ mask rồi mới gộp.

## 3. Worked Example

Một input có probability `[0.1,0.9]`, tau=0.85: chọn nhãn giả 1. Input `[0.55,0.45]` bị bỏ. Hai góc nhìn cho class 1 lần lượt 0.8 và 0.4: TTA=(0.8+0.4)/2=0.6, nhãn 1 tại threshold=0.5. Trong lab, nhãn do dấu x1 quyết định và x2 là nhiễu đối xứng, nên phản chiếu x2 giữ ý nghĩa nhãn; không suy rộng phép này sang chữ số 6/9.

## 4. Shape Analysis

Labeled X `(n_l,2)`, pool X `(n_u,2)`, mask `(n_u,)`; stack TTA `(M,n,2)` → mean axis 0 → `(n,2)`.

## 5. Complexity

Một vòng pseudo-label cần thêm một lần fit và dự đoán pool. TTA M góc nhìn tăng chi phí inference xấp xỉ M lần; cân nhắc ngân sách trước nộp.

## Phạm vi sử dụng dữ liệu

Lab dùng **pool synthetic do notebook tạo**, cho phép tự huấn luyện để học kỹ thuật. Khi dùng dữ liệu cuộc thi, phải xác nhận quy chế cho phép transductive learning (học có sử dụng input test không nhãn). Nếu không cho phép, chỉ chạy baseline và TTA nếu phép đó được cho phép. Không truy tìm label thật, không dò nhãn qua leaderboard và không dùng validation làm pool. Quyền truy cập input công khai không tự động là quyền dùng nó để train. Network: none; không tải dữ liệu bên ngoài.

## 6. From-Scratch & Framework

Không tạo bộ ba notebook Core vì đây là Concept Lesson. Các phép tính nhỏ trong worked example được đối chiếu bằng code; trọng tâm là dùng và debug pipeline. Thực hành theo [lab.ipynb](lab.ipynb). Notebook tự đủ setup/data, không cần chạy chương khác trước.

Lab có code chạy hoàn chỉnh xen câu hỏi dự đoán; làm bài tập riêng trước khi mở đáp án. Dùng thư viện có sẵn trong [environment](../../../envs/requirements.txt), thuộc nhóm được liệt kê trong rules; quyền dùng trong kỳ thi cụ thể lấy từ [competition profile](../../../docs/COMPETITION_PROFILES.md). Không tự cài package hay tải dữ liệu.

## 7. Experiments — Predict → Run → Explain

Dự đoán số mẫu được chọn khi tau tăng từ 0.70 lên 0.95. Lab so sánh số nhãn giả và Macro F1, thử tau=1.01 để xác nhận nhánh rỗng. TTA dùng identity và phản chiếu x2. Không có assert buộc pseudo-label/TTA thắng baseline.

Ghi theo năm bước: **Hypothesis → Code → Result → Observation → Why**. Result phải là số/plot thực chạy; Observation phân biệt bằng chứng và giả thuyết. Mọi plot cần title, axis labels và legend. Kết quả synthetic chỉ minh họa cơ chế, không dự báo leaderboard.

## 8. Common Mistakes & Misconceptions

> ❌ **Sai:** Public test công khai nên được tìm nhãn thật để train.
> ✅ **Đúng:** Chỉ dùng input được cung cấp theo đúng quy chế; tên chương không có nghĩa đi lấy nhãn test.

> ❌ **Sai:** TTA biến đổi nào cũng được.
> ✅ **Đúng:** Chỉ dùng phép giữ ý nghĩa nhãn; bài localization cần biến đổi ngược output.

> ❌ **Sai:** Confidence cao chứng minh pseudo-label đúng.
> ✅ **Đúng:** Model có thể sai tự tin, đặc biệt khi distribution shift; giữ validation tách biệt.

## 9. Code Notes

Đọc [code_notes.md](code_notes.md), đóng tài liệu rồi làm ít nhất hai bài code tay. Tự kiểm tra bằng assert trước khi so reference.

## 10. Exercises

Làm [exercises.md](exercises.md) theo tầng Understand, Implement, Experiment. Đáp án có thể mở riêng từng bài tại [solutions.md](solutions.md).

## 11. Olympiad Transfer & Connections

Khi đề yêu cầu pipeline có thể chạy lại hoặc cung cấp notebook starter, áp dụng chương này trước khi tăng độ phức tạp model. Baseline tối thiểu là chạy notebook và kiểm tra file nộp; dành khoảng 15–20 phút sau khi đã chuẩn bị môi trường. Nếu pseudo-label score giảm, kiểm tra calibration, class counts và shift trước khi tăng pool. Baseline giữ nguyên là một quyết định hợp lệ.

Sau baseline: (1) xác nhận data/split/metric; (2) thử một giả thuyết có log; (3) đóng băng phương án và chạy lại inference. Profile general dùng khoảng 10% thời gian đọc đề/EDA, 20% baseline, 50% thí nghiệm, 20% kiểm tra và nộp. Đây là gợi ý luyện tập, không phải lịch chính thức 4h/6h của bất kỳ kỳ thi nào.

## 12. References

Nguồn cho API, phương pháp và bài đọc mở rộng nằm trong [references.md](references.md). Quy chế hiện hành luôn ưu tiên thông báo đúng mùa thi.

## 13. Mastery Check

- [ ] Explain: giải thích worked example mà không mở tài liệu.
- [ ] Debug: tạo và phát hiện một lỗi trong phần misconceptions.
- [ ] Apply: hoàn thành lab, lưu kết quả và làm bài I-1 trên notebook trống.

Đạt tối thiểu 2/3 gate; nếu chưa pass Apply thì làm lại lab trước khi chuyển chương.

## 14. Time Estimate

Theory: ~0.75h; Code: ~1.25h; Exercises: ~1h. Runtime notebook: thường dưới 1 phút trên CPU cho fast mode, dự trù dưới 2 phút chế độ đầy đủ trên máy học tập/Colab CPU; đây là ước lượng, không phải benchmark Colab đã đo. Ghi thời gian học thực tế để phản hồi learner testing.

[← Module 06](../MODULE_README.md)
