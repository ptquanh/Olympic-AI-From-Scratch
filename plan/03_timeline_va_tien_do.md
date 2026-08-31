# ⏱️ Timeline, Tiến Độ & Quality Gates

> **Tài liệu lịch sử:** Timeline 10 tuần bên dưới là kế hoạch soạn ban đầu, không phải trạng thái release hiện tại và không phải lịch thi chính thức. Dùng `../curriculum.yml` cho trạng thái chương; kiểm tra website ban tổ chức cho lịch thi.

> [← Quay lại Tổng Quan](00_tong_quan.md)

---

## Phiên Bản Phát Hành

| Version                      | Thời điểm     | Nội dung                                                                                  |
| ---------------------------- | ------------- | ----------------------------------------------------------------------------------------- |
| **v0.1 — OlpAI Core**        | Trước 01/11   | Curriculum map, Contest Track, ~10 Core chapters drafted, competition pipeline, templates |
| **v0.2 — Post-Regional**     | 02/11 → 30/11 | Foundation Track, from-scratch sâu hơn, postmortems từ vòng khu vực                       |
| **v0.5 — Pre-Finals**        | 01/12 → 07/12 | Solutions, hình minh họa, learner testing batch 1, audio/document AI                      |
| **v1.0 — Community Release** | 01/2027+      | Tất cả chương Published, MkDocs site, CONTRIBUTING.md active                              |

---

## Timeline v0.1 — 10 Tuần Trước Thi

> **Nguyên tắc:** Mỗi tuần ≥1 timed task. Competition pipeline active từ tuần 1.

### Tuần 0 — Setup + Diagnostic (24-25/08)

| Việc                                           | Output                              |
| ---------------------------------------------- | ----------------------------------- |
| Scaffold repo + curriculum map                 | Repo structure, `CURRICULUM_MAP.md` |
| Setup environment: Python, PyTorch, JupyterLab | Working dev environment             |
| Diagnostic test: 2 bài dễ nhất baseline (3h)   | `07_olympiad_problems/diagnostic/`  |
| Gap analysis → quyết định priority             | Adjusted roadmap                    |

### Tuần 1 — Python + ML Core (25/08 → 31/08)

| Focus       | Chapters                     | Target     |
| ----------- | ---------------------------- | ---------- |
| Concept     | `00/regex_data_handling/`    | Drafted    |
| Core        | `01/linear_regression/`      | Drafted    |
| Core        | `01/logistic_regression/`    | Drafted    |
| Core        | `01/metrics_and_validation/` | Outlined   |
| Competition | `06/eda/` + `06/validation/` | Drafted    |
| Timed task  | 1 tabular problem (2-3h)     | Postmortem |

### Tuần 2 — Classical ML Applied (01/09 → 07/09)

| Focus      | Chapters                                           | Target     |
| ---------- | -------------------------------------------------- | ---------- |
| Concept    | `01/tree_ensembles/` (XGBoost, LightGBM, CatBoost) | Drafted    |
| Concept    | `01/feature_engineering/`                          | Drafted    |
| Concept    | `01/hyperparameter_tuning/`                        | Outlined   |
| Concept    | `01/unsupervised/`                                 | Outlined   |
| Template   | `templates/tabular_classification.ipynb` v1        | Working    |
| Timed task | 1 tabular competition (3h)                         | Postmortem |

### Tuần 3 — Deep Learning Core (08/09 → 14/09)

| Focus      | Chapters                     | Target     |
| ---------- | ---------------------------- | ---------- |
| Core       | `02/pytorch_fundamentals/`   | Drafted    |
| Core       | `02/autograd_micrograd/`     | Drafted    |
| Core       | `02/backprop_training_loop/` | Drafted    |
| Concept    | `02/optimization/`           | Outlined   |
| Concept    | `02/regularization/`         | Outlined   |
| Milestone  | Overfit MNIST subset         | ✅         |
| Timed task | 1 basic image problem (3h)   | Postmortem |

### Tuần 4 — CNN + Image Classification (15/09 → 21/09)

| Focus       | Chapters                                  | Target     |
| ----------- | ----------------------------------------- | ---------- |
| Core        | `03/convolution/`                         | Drafted    |
| Concept     | `03/cnn_architectures/`                   | Drafted    |
| Concept     | `03/augmentation/`                        | Outlined   |
| Competition | `03/image_classification/`                | Drafted    |
| Template    | `templates/image_classification.ipynb` v1 | Working    |
| Timed task  | 1 CV competition (3h)                     | Postmortem |

### Tuần 5 — Detection + Segmentation (22/09 → 28/09)

| Focus      | Chapters                                   | Target     |
| ---------- | ------------------------------------------ | ---------- |
| Core       | `03/detection/` (IoU, NMS, AP + YOLO/DETR) | Drafted    |
| Concept    | `03/segmentation/`                         | Drafted    |
| Templates  | Detection + Segmentation                   | Working    |
| Timed task | 1 IOAI CV problem (3h)                     | Postmortem |
| Timed task | 1 IOAI problem (khác domain)               | Postmortem |

### Tuần 6 — NLP + Team (29/09 → 05/10)

| Focus       | Chapters                         | Target     |
| ----------- | -------------------------------- | ---------- |
| Concept     | `04/text_preprocessing/`         | Drafted    |
| Concept     | `04/embeddings/`                 | Drafted    |
| Competition | `04/text_classification/`        | Drafted    |
| Team        | `08_team_competition/` materials | Drafted    |
| Templates   | Text classification + Retrieval  | Working    |
| Timed task  | 1 NLP problem (3h)               | Postmortem |

### Tuần 7 — Transformer + Fine-tuning (06/10 → 12/10)

| Focus        | Chapters                              | Target     |
| ------------ | ------------------------------------- | ---------- |
| Core         | `04/attention/`                       | Drafted    |
| Core         | `04/transformer/`                     | Drafted    |
| Concept      | `04/pretrained_encoders/`             | Outlined   |
| Core         | `05/finetuning_patterns/`             | Outlined   |
| Mini project | Tiny text classifier with Transformer | Working    |
| Timed task   | 1 NLP/multimodal problem (3h)         | Postmortem |

### Tuần 8 — Gap-Fill + Mock #1 (13/10 → 19/10)

| Focus       | Việc                                                 | Target     |
| ----------- | ---------------------------------------------------- | ---------- |
| Concept     | `05/prompt_engineering/` (chiến thuật LLM trong thi) | Drafted    |
| Concept     | `06/data_from_public_test/`                          | Drafted    |
| Gap-fill    | Topic yếu từ timed tasks                             | Depends    |
| **Mock #1** | 4-6 giờ sát format OlpAI (với đội)                   | Postmortem |

### Tuần 9 — Problem Grinding (20/10 → 26/10)

| Ngày  | Việc                                            |
| ----- | ----------------------------------------------- |
| T1-T2 | Giải 2 bài IOAI (2024/2025) + postmortems       |
| T3    | Giải 1 bài aichallenge.ptit.edu.vn + postmortem |
| T4    | **Mock #2** (4-6 giờ)                           |
| T5    | Postmortem + fix pipelines                      |
| T6-CN | 1 bài Poland OAI + failure pattern analysis     |

### Tuần 10 — Contest Mode (27/10 → 01/11)

| Ngày      | Việc                                                 |
| --------- | ---------------------------------------------------- |
| T1        | **Mock #3** (sát format, với đội, có cấu trúc FINAL) |
| T2        | Postmortem + final template fixes                    |
| T3        | Review top 5 failure patterns                        |
| T4        | Light review mastery gates                           |
| T5        | Tapering — không học mới                             |
| **01/11** | 🏆 **OlpAI Vòng Khu Vực**                            |

---

## Post-Competition

| Giai đoạn   | Việc                                                                 |
| ----------- | -------------------------------------------------------------------- |
| 02-15/11    | Nghỉ + retrospective                                                 |
| 16-30/11    | Foundation Track, Audio/Document AI, from-scratch cho topics đã skip |
| 01-07/12    | Chuẩn bị vòng chung kết (Đà Nẵng, 7-9/12)                            |
| Sau 12/2026 | Learner testing, solutions, MkDocs, community release                |

---

## Quality Gates — Trạng Thái Chương

```
Outlined → Drafted → Technically Reviewed → Learner Tested → Revised → Published

```

| Trạng thái               | Ý nghĩa                                              | Tiêu chí chuyển            |
| ------------------------ | ---------------------------------------------------- | -------------------------- |
| **Outlined**             | README skeleton: outcomes, prerequisite, concept map | Luồng learner journey rõ   |
| **Drafted**              | Tất cả file viết xong, notebook chạy được            | Code đúng, theory coherent |
| **Technically Reviewed** | Toán và code kiểm chứng                              | Self-review kỹ hoặc peer   |
| **Learner Tested**       | ≥1 người target audience đã học thử                  | Feedback ghi vào `_dev/`   |
| **Revised**              | Sửa theo feedback, misconceptions thêm               | Thời gian khớp estimate    |
| **Published**            | Sẵn sàng public                                      | Pass tất cả gate checks    |

### Quality Gate Checks (Published)

- [ ] Toán và code đã kiểm chứng
- [ ] Notebook chạy lại từ Colab mới / fresh venv
- [ ] Có nguồn cho dữ liệu, hình ảnh, phát biểu quan trọng
- [ ] Learning outcomes khớp với exercises
- [ ] Có ít nhất 1 bài tập Transfer (tầng 4)
- [ ] ≥1 learner đã thử
- [ ] Misconceptions phổ biến đã ghi
- [ ] Thời gian học thực tế không lệch >50%

---

## PROGRESS.md Format

```markdown
## Module 01: Machine Learning

| Chương              | Loại    | Track   | Status   | Notes     |
| ------------------- | ------- | ------- | -------- | --------- |
| linear_regression   | Core    | F⭐ C📖 | Drafted  |           |
| logistic_regression | Core    | F⭐ C📖 | Outlined |           |
| metrics_validation  | Core    | F⭐ C⭐ | —        | Priority! |
| tree_ensembles      | Concept | F⭐ C⭐ | —        |           |

| ...
```

---

## Quỹ Thời Gian

### Thời gian soạn theo loại

| Loại            | Soạn   | Học (reader) |
| --------------- | ------ | ------------ |
| Core Chapter    | 10-15h | 6-10h        |
| Concept Lesson  | 3-5h   | 2-3h         |
| Competition Lab | 5-8h   | 3-5h         |

### Budget 10 tuần (~200-270h)

**20-27h/tuần ≈ 3-4h/ngày.** Ngày bận trường 2h, ngày nghỉ 5-6h.

### Cắt giảm nếu thiếu thời gian (ưu tiên bỏ)

1. Module 05 Generative AI → v0.2 (trừ `prompt_engineering/`)
2. `03/generative_cv/` → v0.2
3. `04/audio_fundamentals/` + `04/speech_recognition/` → v0.2
4. `04/document_ai/` → v0.2
5. `01/unsupervised/` → outline only
6. Solutions.md → v0.5

---

## Commit Convention

```
feat(core): draft linear regression chapter
feat(concept): draft augmentation lesson
feat(comp): create image classification competition lab
feat(pipeline): build EDA template v1
solve(ioai25): baseline for task 2
postmortem(mock1): week 8 mock analysis
outline(transformer): skeleton with outcomes
review(linreg): fix gradient derivation
template(cv): update image classification pipeline
release(v0.1): tag pre-competition release

```
