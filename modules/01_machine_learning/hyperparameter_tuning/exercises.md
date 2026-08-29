# Bài tập: Hyperparameter Tuning

## Tầng 1: Understand

**1. Grid Search vs Random Search**
Tại sao trong không gian tìm kiếm cực lớn (ví dụ: tìm 5 tham số cùng lúc), Random Search lại thường tìm ra kết quả tốt hơn Grid Search trong cùng một khoảng thời gian giới hạn?

## Tầng 2: Implement

**1. RandomizedSearchCV**
Sử dụng RandomSearch thay cho GridSearch trên mô hình Random Forest với 2 tham số `n_estimators` và `max_depth`.

## Tầng 3: Experiment

**1. Dùng Optuna cho Random Forest**
Viết một hàm `objective` cho Optuna để tìm kiếm `max_depth` (từ 3 đến 15) và `min_samples_split` (từ 2 đến 10) sao cho Cross Validation Score trên tập Iris là cao nhất.
