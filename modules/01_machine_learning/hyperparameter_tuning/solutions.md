# Lời giải: Tuning

<details><summary><b>Tầng 1: Understand</b></summary>

Learning rate ảnh hưởng lớn nhất ở dải từ 0.01 đến 0.1. Nếu dùng uniform scale từ 0.0001 đến 0.1, Optuna sẽ lãng phí phần lớn thời gian để thử ở dải (0.05 - 0.1) và rất hiếm khi rà trúng các giá trị bé như 0.005. Log scale giúp thuật toán thử nghiệm **đều đặn** ở mọi bậc độ lớn (vd: 1e-4, 1e-3, 1e-2, 1e-1).

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
from sklearn.model_selection import RandomizedSearchCV
import scipy.stats as stats

param_dist = {
    'n_estimators': stats.randint(50, 300),
    'max_depth': stats.randint(3, 10),
    'learning_rate': stats.uniform(0.01, 0.2)
}

rs = RandomizedSearchCV(model, param_dist, n_iter=20, cv=3, random_state=42)
rs.fit(X_train, y_train)
```

Thời gian chạy của RandomSearch cố định bởi `n_iter`, trong khi GridSearch sẽ chạy tất cả tổ hợp.

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

Sử dụng thư viện `optuna`.

```python
import optuna
import lightgbm as lgb
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)

def objective(trial):
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 50, 500),
        'learning_rate': trial.suggest_float('learning_rate', 1e-3, 1e-1, log=True),
        'num_leaves': trial.suggest_int('num_leaves', 10, 50),
        'max_depth': trial.suggest_int('max_depth', 3, 10)
    }
    clf = lgb.LGBMClassifier(**params, random_state=42)
    return cross_val_score(clf, X, y, cv=3, scoring='f1').mean()

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=50)
print(study.best_params)
```

</details>
