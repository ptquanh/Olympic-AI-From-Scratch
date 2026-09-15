# Module 06 — Competition Pipeline

> **Track:** Foundation ⭐ | Contest ⭐
> **Trạng thái:** 7 chương technically_reviewed; cần learner testing trước khi Published.
> **Profile mặc định:** general; CPU, offline, seed 42, dữ liệu synthetic tự tạo.

## Mục tiêu

Từ dữ liệu mới đến baseline có validation đúng, thí nghiệm có bằng chứng và bài nộp chạy lại được. Module hoạt động từ tuần 1 theo plan; bạn không cần học xong LLM mới bắt đầu EDA và validation.

## Lộ trình

| Thứ tự plan | Chương                                                                                     | Loại            | Foundation | Contest |
| ----------- | ------------------------------------------------------------------------------------------ | --------------- | ---------- | ------- |
| 1           | [EDA — Khám phá dữ liệu trước baseline](eda/README.md)                                     | Competition Lab | ⭐         | ⭐      |
| 2           | [Validation — Đo đúng khả năng tổng quát hóa](validation/README.md)                        | Competition Lab | ⭐         | ⭐      |
| 3           | [Public Test — Pseudo-labeling và Test-Time Augmentation](data_from_public_test/README.md) | Concept Lesson  | 📖         | ⭐      |
| 4           | [Debugging ML — Tìm lỗi bằng kiểm chứng nhỏ](debugging_ml/README.md)                       | Competition Lab | ⭐         | ⭐      |
| 5           | [Ensembling — Averaging, Blending và Stacking](ensembling/README.md)                       | Competition Lab | 📖         | ⭐      |
| 6           | [JupyterLab Workflow — Kernel sạch và bài nộp tái lập](jupyterlab_workflow/README.md)      | Concept Lesson  | ⭐         | ⭐      |
| 7           | [Experiment Tracking — Ghi lại để tái lập quyết định](experiment_tracking/README.md)       | Concept Lesson  | 📖         | ⭐      |

Học JupyterLab Workflow trước nếu chưa thao tác được notebook. Sau đó EDA → Validation → Debugging → Experiment Tracking. Khi baseline ổn, học Public Test và Ensembling. Mỗi chương khoảng 3 giờ; toàn module khoảng 21 giờ gồm bài tập. Runtime code ngắn hơn thời gian học vì phần chính là dự đoán, giải thích và luyện code tay.

## Đầu vào và đầu ra

- Entry prerequisites: [NumPy/Pandas](../00_foundations/numpy_pandas/README.md) và [Metrics & Validation](../01_machine_learning/metrics_and_validation/README.md). Public Test dùng thêm [Augmentation](../03_computer_vision/augmentation/README.md); Debugging dùng [Backprop & Training Loop](../02_deep_learning/backprop_training_loop/README.md); Ensembling dùng [Tree Ensembles](../01_machine_learning/tree_ensembles/README.md).
- Competition Lab: README → starter → bài E/T/O → solution → rubric → postmortem. Có exercises/solutions bổ sung để giữ ID và đáp án từng bài theo R6/R11.
- Concept Lesson: README → lab → code notes → bài U/I/E → solutions.
- Tất cả 11 notebook tự đủ dữ liệu/setup. Public test chỉ là input không nhãn được mô phỏng; không dùng nhãn test hay tải dữ liệu bên ngoài.
- Artifact tạo tại `outputs/` bên trong chương. Starter và solution dùng tên riêng; thư mục outputs được git-ignore. CSV có `id,label` là contract bài tập, phải đổi theo đề thực tế.

## Chạy và kiểm tra

Chuẩn bị [môi trường](../../docs/SETUP.md), mở notebook tại thư mục chương, Restart & Run All. `OAI_FAST_MODE=1` giảm số mẫu/vòng lặp nhưng giữ đầy đủ logic. Không tự cài thư viện và không cần GPU.

Từ repository root, contributor kiểm tra riêng module:

```bash
python tools/audit_curriculum.py
python tools/run_notebooks.py --fast --profile cpu --offline --match 06_competition_pipeline --repeats 2 --report _dev/module06_report.json
python tools/verify_notebook_report.py _dev/module06_report.json --profile cpu --min-repeats 2 --allow-partial
```

`technically_reviewed` phản ánh tài liệu, đáp án, notebook và audit kỹ thuật đã vượt gate của repo; trạng thái này chưa thay cho learner testing. Kiểm tra đúng [competition profile](../../docs/COMPETITION_PROFILES.md) khi áp dụng vào đề. Dữ liệu synthetic và các timebox của bài tập không phải luật của kỳ thi.

[← Giáo trình](../../README.md) · [Progress Tracker](../../docs/PROGRESS_TRACKER.md)
