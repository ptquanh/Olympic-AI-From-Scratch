# Bài tập: Hyperparameter Tuning

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Grid Search vs Random Search**
Tại sao trong không gian tìm kiếm cực lớn (ví dụ: tìm 5 tham số cùng lúc), Random Search lại thường tìm ra kết quả tốt hơn Grid Search trong cùng một khoảng thời gian giới hạn?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. RandomizedSearchCV**
Sử dụng RandomSearch thay cho GridSearch trên mô hình Random Forest với 2 tham số `n_estimators` và `max_depth`.

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Dùng Optuna cho Random Forest**
Viết một hàm `objective` cho Optuna để tìm kiếm `max_depth` (từ 3 đến 15) và `min_samples_split` (từ 2 đến 10) sao cho Cross Validation Score trên tập Iris là cao nhất.

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
