# Experiment Tracking — Ghi lại để tái lập quyết định

> **Loại:** Concept Lesson
> **Track:** Foundation 📖 | Contest ⭐
> **Thời gian học ước tính:** 3 giờ (theory: 0.75h, code: 1.25h, exercises: 1h)
> **Profile mặc định:** general · CPU · offline · dữ liệu mô phỏng tự tạo.
> **Trạng thái:** technically_reviewed; chưa có learner testing. Xem [manifest](../../../curriculum.yml).

## Prerequisite Check

1. Cố định seed có lưu được train/validation split không?
2. Hai cấu hình khác nhau nhưng cùng tên file có vấn đề gì?
3. Vì sao phải lưu preprocessing cùng model?

Nếu chưa trả lời được, quay lại [Validation](../validation/README.md) và [JupyterLab Workflow](../jupyterlab_workflow/README.md).

## Learning Outcomes

- [ ] LO1: Ghi config, split, metric, runtime và data hash cho mỗi run.
- [ ] LO2: Replay một run từ artifact và kiểm tra predictions.
- [ ] LO3: Chọn cấu hình theo validation, ghi cả thí nghiệm thất bại và giới hạn reproducibility.

## Concept Map

```text
Validation + JupyterLab Workflow → Experiment Tracking → Competition Pipeline hoàn chỉnh
                              └→ baseline chạy lại được trong phòng thi
```

## 1. Intuition — Tại sao cần?

Ba ngày sau, bạn không nhớ score tốt nhất dùng C=0.1 hay C=1, split nào, đã scale chưa. Experiment tracking (ghi dấu thí nghiệm) gắn kết quả với đúng input, code, config và môi trường. Một bảng điểm không có provenance (nguồn gốc) không đủ để tái lập.

## 2. Math & Derivation

Đặt run_key = SHA256(canonical_json(config)). Canonical ở đây nghĩa là sort key và dùng separators cố định, giúp cùng config cho cùng chuỗi byte. Hash không chứng minh run đúng; nó giúp phát hiện config/data khác nhau. Reproducibility kiểm tra max_i |p_i-p_replay_i| <= atol + rtol·|p_i|. Seed kiểm soát nguồn ngẫu nhiên nhưng không đảm bảo bitwise equality giữa hardware, phiên bản thư viện hoặc thuật toán không deterministic.

## 3. Worked Example

Config `{seed:42,C:1.0}` và `{C:1.0,seed:42}` phải cho cùng canonical JSON và hash. Nếu đổi C=0.1 thì hash đổi. Run A có F1=0.80 trong 2 giây, run B=0.80 trong 20 giây: theo tie-break ưu tiên chi phí đã khai báo, A là lựa chọn hợp lý. Score chênh rất nhỏ cần xét độ ổn định, không chỉ xếp hạng một lần.

## 4. Shape Analysis

Split train/val là index array; probability validation `(n_val,2)`; log là danh sách record có schema_version, run_id, config, metric, elapsed_seconds, data_hash và versions.

## 5. Complexity

Hash dữ liệu đọc O(số byte). Lưu model tăng disk theo số run; lab lưu best model và log cho mọi run. Không dùng dịch vụ cloud hay API key; JSON, NumPy và joblib đều chạy offline.

## 6. From-Scratch & Framework

Không tạo bộ ba notebook Core vì đây là Concept Lesson. Các phép tính nhỏ trong worked example được đối chiếu bằng code; trọng tâm là dùng và debug pipeline. Thực hành theo [lab.ipynb](lab.ipynb). Notebook tự đủ setup/data, không cần chạy chương khác trước.

Lab có code chạy hoàn chỉnh xen câu hỏi dự đoán; làm bài tập riêng trước khi mở đáp án. Dùng thư viện có sẵn trong [environment](../../../envs/requirements.txt), thuộc nhóm được liệt kê trong rules; quyền dùng trong kỳ thi cụ thể lấy từ [competition profile](../../../docs/COMPETITION_PROFILES.md). Không tự cài package hay tải dữ liệu.

## 7. Experiments — Predict → Run → Explain

Dự đoán run_id có đổi khi đảo thứ tự key hay khi thay C. Lab thử C=[0.1,1,10] với split cố định, ghi log rồi reload best pipeline. Đồng thời chạy lại từ config và so sánh probability trong cùng môi trường. Ghi runtime nhưng không kỳ vọng thời gian bằng nhau qua hai lần.

Ghi theo năm bước: **Hypothesis → Code → Result → Observation → Why**. Result phải là số/plot thực chạy; Observation phân biệt bằng chứng và giả thuyết. Mọi plot cần title, axis labels và legend. Kết quả synthetic chỉ minh họa cơ chế, không dự báo leaderboard.

## 8. Common Mistakes & Misconceptions

> ❌ **Sai:** Seed=42 bảo đảm mọi máy ra cùng bit.
> ✅ **Đúng:** Còn phụ thuộc environment/hardware; lưu versions và tolerance.

> ❌ **Sai:** Chỉ cần lưu best score.
> ✅ **Đúng:** Cần cả config, split, dữ liệu, code version và preprocessing để giải thích/replay.

> ❌ **Sai:** Hash giống nhau nghĩa là model tốt.
> ✅ **Đúng:** Hash xác định nội dung; chất lượng vẫn cần validation đúng.

## 9. Code Notes

Đọc [code_notes.md](code_notes.md), đóng tài liệu rồi làm ít nhất hai bài code tay. Tự kiểm tra bằng assert trước khi so reference.

## 10. Exercises

Làm [exercises.md](exercises.md) theo tầng Understand, Implement, Experiment. Đáp án có thể mở riêng từng bài tại [solutions.md](solutions.md).

## 11. Olympiad Transfer & Connections

Khi đề yêu cầu pipeline có thể chạy lại hoặc cung cấp notebook starter, áp dụng chương này trước khi tăng độ phức tạp model. Baseline tối thiểu là chạy notebook và kiểm tra file nộp; dành khoảng 15–20 phút sau khi đã chuẩn bị môi trường. Nếu replay khác, so data hash và split trước, rồi config, code version và package versions. Không đổi tolerance lớn để che sai khác chưa giải thích.

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
