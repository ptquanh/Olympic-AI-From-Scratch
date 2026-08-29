# Bài tập: Tuning

## Tầng 1: Understand

**1. Tại sao dùng Log Scale cho Learning Rate?**
Khi tinh chỉnh `learning_rate` trong XGBoost, ta thường dùng `trial.suggest_float('lr', 1e-4, 1e-1, log=True)`. Việc dùng log scale mang lại lợi ích gì so với uniform scale?

## Tầng 2: Implement

**1. Random Search**
Sử dụng RandomSearch thay cho GridSearch trên mô hình XGBoost. So sánh thời gian chạy khi số lượng cấu hình quá lớn.

## Tầng 3: Experiment

**1. Chinh phục Optuna**
Sử dụng bộ dữ liệu Breast Cancer. Thử nghiệm thuật toán LightGBM và dùng Optuna tìm bộ tham số tốt nhất với 50 lần thử (trials). Cố gắng đạt F1-Score cao nhất trên Cross Validation.
