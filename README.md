# 🏆 Olympic AI From Scratch

> **Technical Review Beta · v0.2.0**  
> Phạm vi hiện tại: Module 00–06, 48 chương. Module 06 mới được triển khai ở mức Drafted; dự án đang được review và kiểm thử.

Giáo trình AI tiếng Việt, open-source, đi từ nền tảng Python và toán đến Machine Learning, Deep Learning, Computer Vision, NLP/Audio và Generative AI. Hai mục tiêu được duy trì song song:

- **Foundation Track:** học từ con số 0, hiểu bản chất và tự cài đặt phần cốt lõi.
- **Contest Track:** tập trung validation, pipeline, failure modes và khả năng tái lập trong Olympic AI.

Giáo trình không coi luật của một cuộc thi là luật chung. Nội dung ổn định được trình bày ở profile `general`; quy định về thời lượng, Internet, LLM, thư viện và nộp bài phải ghi rõ kỳ thi, năm và nguồn.

## Bắt đầu

1. Đọc [hướng dẫn học](docs/HOW_TO_STUDY.md) và chọn track.
2. Cài môi trường theo [SETUP.md](docs/SETUP.md).
3. Chọn đúng luật tại [COMPETITION_PROFILES.md](docs/COMPETITION_PROFILES.md) nếu học Contest Track.
4. Xem [PROGRESS_TRACKER.md](docs/PROGRESS_TRACKER.md) để theo dõi tiến độ và `curriculum.yml` để biết trạng thái của từng chương.
5. Trong mỗi chương: README → notebook → code notes → exercises → solutions.

## Nội dung hiện có

### [Module 00 — Python & Toán nền tảng](modules/00_foundations/MODULE_README.md)

Python Essentials · NumPy & Pandas · Regex & Data Handling · Math Essentials · Visualization

### [Module 01 — Machine Learning](modules/01_machine_learning/MODULE_README.md)

Linear Regression · Logistic Regression · Metrics & Validation · Tree Ensembles · SVM & KNN · Unsupervised Learning · Feature Engineering · Hyperparameter Tuning

### [Module 02 — Deep Learning](modules/02_deep_learning/MODULE_README.md)

PyTorch Fundamentals · Autograd & Micrograd · Backprop & Training Loop · Activation Functions · Loss Functions · Optimization · Regularization

### [Module 03 — Computer Vision](modules/03_computer_vision/MODULE_README.md)

Image Fundamentals · Augmentation · Convolution · CNN Architectures · Image Classification Competition · Object Detection · Segmentation · Generative CV

### [Module 04 — NLP & Audio](modules/04_nlp_audio/MODULE_README.md)

Text Preprocessing · Embeddings · Attention · Transformer · Pre-trained Encoders · Text Classification Competition · Document AI · Audio Fundamentals · Speech Recognition

### [Module 05 — Generative AI & LLM](modules/05_generative_ai_llm/MODULE_README.md)

Language Modeling · Prompt Engineering · Fine-tuning Patterns · Multimodal

### [Module 06 — Competition Pipeline](modules/06_competition_pipeline/MODULE_README.md)

EDA · Validation · Public Test / Pseudo-labeling / TTA · Debugging ML · Ensembling · JupyterLab Workflow · Experiment Tracking

4 Competition Lab và 3 Concept Lesson, gồm 11 notebook CPU offline. Học từ tuần 1 cùng ML baseline; mở JupyterLab Workflow trước nếu chưa quen notebook.

### Practice layer ngoài manifest

- [Module 07 — Olympiad Problems](modules/07_olympiad_problems/MODULE_README.md): curated link registry, practice protocol, IOAI/Polish OAI/PTIT sources, mock playlists và postmortem.
- [Module 08 — Team Competition](modules/08_team_competition/MODULE_README.md): phân vai đội 2–3 người, workflow 4h/6h, contest toolkit, notebook checklist, FINAL template và technical report.

Hai module này là tài liệu luyện thi/operations, chưa được tính vào `chapter_count: 48` và không mang status trong manifest.

## Ba loại chương

| Loại        | Mục tiêu                                     | Bài thực hành                                         |
| ----------- | -------------------------------------------- | ----------------------------------------------------- |
| Core        | Derive và implement thuật toán nền tảng      | `01_from_scratch`, `02_framework`, `03_experiments`   |
| Concept     | Dùng đúng API, giải thích và debug           | `lab.ipynb`                                           |
| Competition | Xây pipeline và ra quyết định trong giới hạn | `starter.ipynb`, `solution.ipynb`, rubric, postmortem |

`solutions.md` là bắt buộc cho cả Core và Concept. Bài tập Core dùng năm tầng U/I/E/T/O; Concept dùng U/I/E; Competition đánh giá E/T/O qua rubric.

## Trạng thái chất lượng

`curriculum.yml` là nguồn trạng thái duy nhất. Luồng hợp lệ:

`outlined → drafted → technically_reviewed → learner_tested → revised → published`

Beta này đặt mục tiêu `technically_reviewed`. Trong 48 chương, 31 chương đã đạt; 10 chương GPU và 7 chương Module 06 mới ở `drafted`. Các chương GPU còn thiếu portability evidence trên Colab/Kaggle; Module 06 chưa có learner testing. Một chương chỉ đạt mốc khi lý thuyết và đáp án được đối chiếu, notebook chạy từ đầu đến cuối và audit cấu trúc pass. Log review nội bộ nằm trong `_dev/`.

## Ngoài phạm vi quality gate 48 chương

Module 07 và 08 đã có resource layer để luyện đề và mô phỏng thi đội, nhưng chưa nằm trong manifest 48 chương. Đề thật chỉ được tham chiếu bằng link nguồn; statement, dataset, notebook và code của cuộc thi không được mirror vào repo.

## Đóng góp và giấy phép

Xem [CONTRIBUTING.md](.github/CONTRIBUTING.md) và [CODE_OF_CONDUCT.md](.github/CODE_OF_CONDUCT.md). Code/notebook dùng MIT; nội dung giáo dục gốc dùng CC BY-SA 4.0. PDF cẩm nang và tài sản bên thứ ba không được cấp lại theo các giấy phép này; xem [THIRD_PARTY_NOTICES.md](docs/THIRD_PARTY_NOTICES.md).
