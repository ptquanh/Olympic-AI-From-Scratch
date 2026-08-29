# Lời giải: Hyperparameter Tuning

<details><summary><b>Tầng 1: Understand</b></summary>
Trong nhiều trường hợp, chỉ có 1-2 tham số là thực sự quan trọng ảnh hưởng đến độ chính xác (ví dụ learning_rate). Grid Search rà quét toàn bộ kết hợp lưới nên mất quá nhiều thời gian kiểm tra các giá trị vô nghĩa của các tham số không quan trọng. Random Search lấy mẫu ngẫu nhiên, giúp phân bố thời gian hợp lý hơn và khám phá được nhiều giá trị dọc theo trục của tham số quan trọng.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint

model = RandomForestClassifier()
param_dist = {
    'n_estimators': randint(50, 200),
    'max_depth': randint(3, 10)
}

rs = RandomizedSearchCV(model, param_distributions=param_dist, n_iter=10, cv=3)
rs.fit(X_train, y_train)
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

```python
import optuna
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

def objective(trial):
    depth = trial.suggest_int('max_depth', 3, 15)
    split = trial.suggest_int('min_samples_split', 2, 10)

    model = RandomForestClassifier(max_depth=depth, min_samples_split=split)
    return cross_val_score(model, X, y, cv=3).mean()

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=10)
print(study.best_params)
```

</details>
