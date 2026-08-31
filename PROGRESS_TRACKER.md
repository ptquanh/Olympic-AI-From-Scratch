# Progress Tracker — Technical Review Beta

> `curriculum.yml` là nguồn trạng thái duy nhất. File này là hướng dẫn cho người học, không phải tuyên bố chapter đã review.

## Trạng thái repository

| Scope        |     Chapters | Target                      |
| ------------ | -----------: | --------------------------- |
| Module 00–05 |           41 | Technically Reviewed Beta   |
| Module 06–08 | 0 trong repo | Roadmap, ngoài phạm vi Beta |

Trạng thái theo evidence 2026-08-31:

| Status                       | Số chương | Lý do                                                               |
| ---------------------------- | --------: | ------------------------------------------------------------------- |
| `technically_reviewed`       |        31 | Static + CPU x2 + clean Python 3.10 pass                            |
| `drafted`                    |        10 | Local GPU full đã pass; còn thiếu Colab/Kaggle portability evidence |
| `learner_tested`/`published` |         0 | Chưa có learner testing với người thật                              |

Chi tiết 41/41 nằm trong `_dev/review_log.md`. Report JSON không được version-control: PR chạy notebook bị ảnh hưởng, còn full run là gate định kỳ/phát hành và được lưu bằng CI artifact gắn với commit.

## Checklist cá nhân

Với mỗi chapter ID trong `curriculum.yml`, sao chép mẫu sau vào learning log riêng:

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
