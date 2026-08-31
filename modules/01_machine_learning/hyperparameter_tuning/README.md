# Hyperparameter Tuning

> **Track:** Foundation 📖 | Contest ⭐

## ① Prerequisite Check

Bạn cần phân biệt parameter/hyperparameter, tạo cross-validation split phù hợp và nhận diện leakage. Nếu chưa, đọc Metrics & Validation và Feature Engineering.

## ② Learning Outcomes

- Thiết kế search space có scale phù hợp, ví dụ log-uniform cho learning rate.
- Đặt preprocessing và estimator trong cùng `Pipeline` khi cross-validation.
- Phân biệt model selection score với final unbiased estimate.
- Chọn grid, randomized hoặc Bayesian search theo budget và số chiều.

## ③ Concept Map

`Validation protocol → search space + budget → select on validation → evaluate once on held-out test`

## ④ Intuition

Tuning là một vòng lặp học trên validation. Thử càng nhiều cấu hình, nguy cơ overfit validation càng tăng. Vì vậy phải khóa metric/split trước, log mọi run và chỉ dùng test đúng một lần sau khi chọn pipeline.

## ⑧ Framework / Lab

`RandomizedSearchCV` thường khám phá tốt hơn grid khi nhiều hyperparameter không quan trọng. Dùng `Pipeline` để scaler/encoder được fit riêng trong từng fold; dùng `StratifiedKFold` cho classification mất cân bằng và group/time split khi dữ liệu yêu cầu.

## ⑩ Misconceptions

- ❌ **Sai:** Grid search exhaustive nên luôn tốt nhất. → ✅ Nó chỉ exhaustive trên grid đã chọn và tăng theo cấp số nhân.
- ❌ **Sai:** Có thể tune trên test nếu không train bằng test. → ✅ Lựa chọn dựa trên test đã làm test thành validation.
- ❌ **Sai:** Best CV score là performance chắc chắn. → ✅ Báo mean, spread và final held-out score.

## ⑮ Mastery Check

Tạo được search space, scoring, CV splitter và budget trước khi chạy; giải thích được vì sao pipeline không leakage.

## ⑯ Time Estimate

Theory: ~1h · Code: ~1.5h · Exercises: ~1h
