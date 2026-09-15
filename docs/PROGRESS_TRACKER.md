# Progress Tracker — Technical Review Beta

> `curriculum.yml` là nguồn trạng thái duy nhất. File này là hướng dẫn cho người học, không phải tuyên bố chapter đã review.

## Trạng thái repository

| Scope        |       Chapters | Target                                  |
| ------------ | -------------: | --------------------------------------- |
| Module 00–05 |             41 | Technically Reviewed Beta               |
| Module 06    |              7 | Drafted; 11 notebook CPU offline        |
| Module 07–08 | Resource layer | Đã triển khai, ngoài manifest 48 chương |

Trạng thái: baseline 00–05 ngày 2026-08-31, bổ sung Module 06 ngày 2026-09-15:

| Status                       | Số chương | Lý do                                                            |
| ---------------------------- | --------: | ---------------------------------------------------------------- |
| `technically_reviewed`       |        31 | Static + CPU x2 + clean Python 3.10 pass                         |
| `drafted`                    |        17 | 10 chương GPU chờ portability; 7 chương Module 06 mới triển khai |
| `learner_tested`/`published` |         0 | Chưa có learner testing với người thật                           |

Manifest hiện có 48 chương. Chi tiết nằm trong `_dev/review_log.md`. Report JSON không được version-control: PR chạy notebook bị ảnh hưởng, còn full run là gate định kỳ/phát hành và được lưu bằng CI artifact gắn với commit.

## Module 06 — Competition Pipeline

| Chương                                                                                  | Archetype   | Status  |
| --------------------------------------------------------------------------------------- | ----------- | ------- |
| [EDA](../modules/06_competition_pipeline/eda/README.md)                                 | Competition | drafted |
| [Validation](../modules/06_competition_pipeline/validation/README.md)                   | Competition | drafted |
| [Public Test](../modules/06_competition_pipeline/data_from_public_test/README.md)       | Concept     | drafted |
| [Debugging ML](../modules/06_competition_pipeline/debugging_ml/README.md)               | Competition | drafted |
| [Ensembling](../modules/06_competition_pipeline/ensembling/README.md)                   | Competition | drafted |
| [JupyterLab Workflow](../modules/06_competition_pipeline/jupyterlab_workflow/README.md) | Concept     | drafted |
| [Experiment Tracking](../modules/06_competition_pipeline/experiment_tracking/README.md) | Concept     | drafted |

Bài mô phỏng chạy CPU offline; chất lượng trên đề thật, thao tác UI JupyterLab và thời gian học thực tế cần người học kiểm chứng. Không gọi các chương này Published từ kết quả kiểm tra tự động.

## Module 07–08 — Practice & Team Operations

- [Module 07 — Olympiad Problems](../modules/07_olympiad_problems/MODULE_README.md): curated links, practice protocol, diagnostic, IOAI/Polish OAI/PTIT registry, mock playlists và postmortem template.
- [Module 08 — Team Competition](../modules/08_team_competition/MODULE_README.md): team roles, workflow 4h/6h, contest toolkit, notebook checklist, FINAL folder và technical report template.

Kiểm chứng thực tế được ghi tại `_dev/real_problem_log.md`; gap lặp lại qua nhiều đề được tổng hợp tại `_dev/curriculum_gap_log.md`.

Hai module này chưa có chapter status trong `curriculum.yml`; chúng được review như tài liệu hỗ trợ và phải tiếp tục cập nhật nguồn theo từng mùa thi.

## Checklist theo dõi học tập

Với mỗi chapter ID trong `curriculum.yml`, sao chép mẫu sau để theo dõi tiến độ:

```markdown
- [ ] Prerequisite check
- [ ] Theory + worked example
- [ ] Notebook CPU smoke / GPU full nếu cần
- [ ] Code recall không nhìn tài liệu
- [ ] Exercises theo track
- [ ] Mastery check
- Actual time: theory ** / code ** / exercises \_\_
- Biggest misconception: \_\_
```

## Milestones khuyến nghị

- **Foundation 1:** hoàn tất module 00 và tự viết lại các thao tác NumPy/Pandas cốt lõi.
- **ML baseline:** hoàn tất Linear/Logistic Regression, Metrics & Validation, Tree Ensembles và Feature Engineering.
- **DL training:** tự debug được một training loop PyTorch và giải thích gradient flow.
- **CV pipeline:** hoàn tất Image Classification competition lab, sau đó Detection/Segmentation.
- **NLP pipeline:** hoàn tất Text Classification competition lab, sau đó Document AI/Audio theo nhu cầu.
- **Advanced:** Transformer, Fine-tuning và Multimodal.

`Published` không phải milestone tự học và không được đánh dấu chỉ vì automation pass; nó cần learner testing và revision.
