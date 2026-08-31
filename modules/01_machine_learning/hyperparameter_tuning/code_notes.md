# Code Notes: Hyperparameter Tuning

> ⚠️ **Online/optional appendix:** một số snippet bên dưới cần package hoặc model cache bổ sung và có thể tải dữ liệu ở lần chạy đầu. Chúng không competition-safe nếu profile chính thức không cho phép rõ ràng. Notebook chính của chương luôn có đường chạy fast/offline và không tự cài/tải.

## 🔑 Core Patterns

### Pattern 1: Optuna Cơ Bản

```python
import optuna
from sklearn.model_selection import cross_val_score
import lightgbm as lgb

def objective(trial):
    param = {
        'n_estimators': trial.suggest_int('n_estimators', 50, 300),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3, log=True),
        'max_depth': trial.suggest_int('max_depth', 3, 9)
    }
    model = lgb.LGBMClassifier(**param)
    score = cross_val_score(model, X_train, y_train, cv=3).mean()
    return score

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=20)
print(study.best_params)

```

## 📋 API Cheat Sheet

| Việc cần làm          | Code                                        | Link Docs                                                                                                                         |
| --------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Khởi tạo Optuna Study | `optuna.create_study(direction='maximize')` | [optuna create_study](https://optuna.readthedocs.io/en/stable/reference/generated/optuna.create_study.html)                       |
| Gợi ý số nguyên       | `trial.suggest_int('name', min, max)`       | [suggest_int](https://optuna.readthedocs.io/en/stable/reference/generated/optuna.trial.Trial.html#optuna.trial.Trial.suggest_int) |
| Chạy GridSearch       | `GridSearchCV(model, param_grid, cv=5)`     | [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)                       |

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                                                | Thời gian | Hint (ẩn)                                |
| --- | ---------------------------------------------------------------------------------- | --------- | ---------------------------------------- |
| 1   | Viết hàm `objective(trial)` đơn giản cho Random Forest (chọn `max_depth` từ 3-10). | 5 phút    | `trial.suggest_int('max_depth', 3, 10)`  |
| 2   | Code vòng lặp chạy tối ưu Optuna 50 trials.                                        | 3 phút    | `study.optimize(objective, n_trials=50)` |

## 🧠 Flashcards

| Hỏi                                                                             | Trả lời                                                                                                    |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Tại sao GridSearch không tối ưu cho tập tham số lớn?                            | Vì nó thử mọi tổ hợp có thể, gây bùng nổ tổ hợp và chạy cực lâu.                                           |
| Bayesian Optimization (mà Optuna sử dụng) khác GridSearch/RandomSearch thế nào? | Nó học từ kết quả của các lần thử trước đó để gợi ý bộ tham số có khả năng tốt nhất cho lần thử tiếp theo. |
