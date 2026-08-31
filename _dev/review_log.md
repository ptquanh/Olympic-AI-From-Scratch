# Review log — Technical Review Beta

> Ngày review baseline: 2026-08-31 · Reviewer: Codex (AI-assisted technical review).

## Phạm vi và nguyên tắc

- 41 chương, 222 file Markdown và 63 notebook công khai theo manifest.
- Ba notebook hình thức của PyTorch Fundamentals được thay bằng một lab Concept; 6 notebook `*_practice` cá nhân bị loại khỏi scope.
- Static audit đọc contract, metadata, exercise/solution parity, code notes, references, source code và liên kết. Automated pass không thay learner testing.
- Report JSON là CI/release artifact tạm gắn với commit, không phải nội dung version-control.

## Execution policy

- Baseline 2026-08-31: CPU 63/63 chạy hai lần; clean Python 3.10 CPU 63/63; local GPU full 19/19.
- Pull request chỉ chạy notebook bị ảnh hưởng. Thay đổi Markdown chỉ cần static audit.
- Full CPU run chạy theo lịch Chủ nhật hoặc thủ công trước release; GPU/cloud full run là release gate cho chương `gpu_full: true`.
- CI artifact và commit/CI run URL là bằng chứng thực thi; không commit report JSON.

## Review record 41/41

| Chương                            | Archetype   | Track                                             | Runtime policy                                       | Manifest status      |
| --------------------------------- | ----------- | ------------------------------------------------- | ---------------------------------------------------- | -------------------- |
| `foundations.python_essentials`   | concept     | Foundation: required; Contest: skip_if_diagnostic | incremental CPU + scheduled full                     | technically_reviewed |
| `foundations.numpy_pandas`        | concept     | Foundation: required; Contest: skim               | incremental CPU + scheduled full                     | technically_reviewed |
| `foundations.regex_data_handling` | concept     | Foundation: required; Contest: required           | incremental CPU + scheduled full                     | technically_reviewed |
| `foundations.math_essentials`     | concept     | Foundation: required; Contest: skim               | incremental CPU + scheduled full                     | technically_reviewed |
| `foundations.visualization`       | concept     | Foundation: required; Contest: skip_if_diagnostic | incremental CPU + scheduled full                     | technically_reviewed |
| `ml.linear_regression`            | core        | Foundation: required; Contest: skim               | incremental CPU + scheduled full                     | technically_reviewed |
| `ml.logistic_regression`          | core        | Foundation: required; Contest: skim               | incremental CPU + scheduled full                     | technically_reviewed |
| `ml.metrics_and_validation`       | core        | Foundation: required; Contest: required           | incremental CPU + scheduled full                     | technically_reviewed |
| `ml.tree_ensembles`               | concept     | Foundation: required; Contest: required           | incremental CPU + scheduled full                     | technically_reviewed |
| `ml.svm_knn`                      | concept     | Foundation: skim; Contest: skip_if_diagnostic     | incremental CPU + scheduled full                     | technically_reviewed |
| `ml.unsupervised`                 | concept     | Foundation: skim; Contest: skim                   | incremental CPU + scheduled full                     | technically_reviewed |
| `ml.feature_engineering`          | concept     | Foundation: required; Contest: required           | incremental CPU + scheduled full                     | technically_reviewed |
| `ml.hyperparameter_tuning`        | concept     | Foundation: skim; Contest: required               | incremental CPU + scheduled full                     | technically_reviewed |
| `dl.pytorch_fundamentals`         | concept     | Foundation: required; Contest: required           | incremental CPU + scheduled full + release GPU/cloud | drafted              |
| `dl.autograd_micrograd`           | core        | Foundation: required; Contest: skim               | incremental CPU + scheduled full                     | technically_reviewed |
| `dl.backprop_training_loop`       | core        | Foundation: required; Contest: required           | incremental CPU + scheduled full + release GPU/cloud | drafted              |
| `dl.activation_functions`         | concept     | Foundation: required; Contest: skim               | incremental CPU + scheduled full                     | technically_reviewed |
| `dl.loss_functions`               | concept     | Foundation: required; Contest: required           | incremental CPU + scheduled full                     | technically_reviewed |
| `dl.optimization`                 | concept     | Foundation: required; Contest: required           | incremental CPU + scheduled full                     | technically_reviewed |
| `dl.regularization`               | concept     | Foundation: required; Contest: required           | incremental CPU + scheduled full + release GPU/cloud | drafted              |
| `cv.image_fundamentals`           | concept     | Foundation: required; Contest: required           | incremental CPU + scheduled full                     | technically_reviewed |
| `cv.augmentation`                 | concept     | Foundation: required; Contest: required           | incremental CPU + scheduled full                     | technically_reviewed |
| `cv.convolution`                  | core        | Foundation: required; Contest: required           | incremental CPU + scheduled full                     | technically_reviewed |
| `cv.cnn_architectures`            | concept     | Foundation: required; Contest: required           | incremental CPU + scheduled full + release GPU/cloud | drafted              |
| `cv.image_classification`         | competition | Foundation: required; Contest: required           | incremental CPU + scheduled full + release GPU/cloud | drafted              |
| `cv.detection`                    | core        | Foundation: required; Contest: required           | incremental CPU + scheduled full + release GPU/cloud | drafted              |
| `cv.segmentation`                 | concept     | Foundation: required; Contest: required           | incremental CPU + scheduled full + release GPU/cloud | drafted              |
| `cv.generative_cv`                | concept     | Foundation: advanced; Contest: skim               | incremental CPU + scheduled full                     | technically_reviewed |
| `nlp.text_preprocessing`          | concept     | Foundation: required; Contest: required           | incremental CPU + scheduled full                     | technically_reviewed |
| `nlp.embeddings`                  | concept     | Foundation: required; Contest: required           | incremental CPU + scheduled full                     | technically_reviewed |
| `nlp.attention`                   | core        | Foundation: required; Contest: required           | incremental CPU + scheduled full                     | technically_reviewed |
| `nlp.transformer`                 | core        | Foundation: required; Contest: required           | incremental CPU + scheduled full + release GPU/cloud | drafted              |
| `nlp.pretrained_encoders`         | concept     | Foundation: required; Contest: required           | incremental CPU + scheduled full + release GPU/cloud | drafted              |
| `nlp.text_classification`         | competition | Foundation: required; Contest: required           | incremental CPU + scheduled full                     | technically_reviewed |
| `nlp.document_ai`                 | concept     | Foundation: advanced; Contest: required           | incremental CPU + scheduled full                     | technically_reviewed |
| `audio.audio_fundamentals`        | concept     | Foundation: advanced; Contest: skim               | incremental CPU + scheduled full                     | technically_reviewed |
| `audio.speech_recognition`        | concept     | Foundation: advanced; Contest: required           | incremental CPU + scheduled full                     | technically_reviewed |
| `genai.language_modeling`         | concept     | Foundation: advanced; Contest: skim               | incremental CPU + scheduled full                     | technically_reviewed |
| `genai.prompt_engineering`        | concept     | Foundation: skim; Contest: required               | incremental CPU + scheduled full                     | technically_reviewed |
| `genai.finetuning_patterns`       | core        | Foundation: advanced; Contest: required           | incremental CPU + scheduled full + release GPU/cloud | drafted              |
| `genai.multimodal`                | concept     | Foundation: advanced; Contest: skim               | incremental CPU + scheduled full                     | technically_reviewed |

## Release decision

Repo mang nhãn **Technical Review Beta**, không phải Published. `learner_tested`, `revised` và `published` chỉ được cập nhật sau learner testing có người thật. Chương GPU còn `drafted` cho đến khi portability gate của release được hoàn tất.
