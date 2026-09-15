# Technical Report Template

> Mục tiêu: một người không tham gia experiment vẫn hiểu được vì sao đội chọn pipeline cuối.

## 1. Tóm tắt

- Task:
- Metric:
- Final validation score:
- Final public/private score (nếu được phép ghi):
- Runtime train/inference:

## 2. Dữ liệu và validation

- Dataset/schema:
- Split strategy:
- Leakage checks:
- Data cleaning/augmentation:
- Vì sao validation mô phỏng test hợp lý:

## 3. Baseline

- Model/pipeline:
- Feature/preprocessing:
- Baseline score:
- Failure mode lớn nhất:

## 4. Experiments

| #   | Hypothesis | Change | Val score | Runtime | Decision |
| --- | ---------- | ------ | --------: | ------: | -------- |
| 1   |            |        |           |         |          |
| 2   |            |        |           |         |          |
| 3   |            |        |           |         |          |

## 5. Final solution

- Model(s):
- Hyperparameters quan trọng:
- Ensemble/blending:
- Checkpoint/artifact:
- Seed:

## 6. Reproducibility

- Environment/profile:
- Notebook entrypoint:
- Input path:
- Output path/schema:
- Restart & Run All: PASS / FAIL

## 7. Postmortem

- Quyết định tốt nhất:
- Thử nghiệm lãng phí nhất:
- Rủi ro validation còn lại:
- Nếu có thêm 30 phút, việc đầu tiên sẽ làm:
