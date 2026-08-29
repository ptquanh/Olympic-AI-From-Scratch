# Loss Functions

> **Track:** Foundation ⭐ | Contest 📖

## ① Prerequisite Check

- Bạn đã hiểu bài toán Hồi quy (Regression) và Phân loại (Classification) khác nhau chỗ nào chưa?

## ② Learning Outcomes

- Phân biệt và sử dụng đúng L1 Loss (MAE), L2 Loss (MSE) cho Hồi quy.
- Sử dụng thành thạo Cross-Entropy Loss cho bài toán Phân loại.
- Triển khai được Focal Loss để xử lý mất cân bằng dữ liệu (Class Imbalance).

## ③ Concept Map

Activation Functions ➔ **Loss Functions** ➔ Optimization ➔ Regularization

## ④ Intuition

Nếu Mạng nơ-ron là một học sinh, thì Hàm Loss chính là thang điểm của giáo viên. Nó định lượng xem học sinh làm bài "tệ" đến mức nào. Điểm "tệ" (Loss) càng lớn, học sinh càng phải sửa sai (Gradient Descent) nhiều hơn. Việc chọn đúng hàm Loss cũng giống như chọn đúng thang điểm (thi trắc nghiệm phải chấm khác thi tự luận).

## ⑤ Math/Derivation

- **MSE (Mean Squared Error):** $\frac{1}{n}\sum(y - \hat{y})^2$. Rất nhạy cảm với Outlier (nhiễu).
- **Cross-Entropy:** $-\sum y \log(\hat{y})$. Phạt cực nặng những dự đoán tự tin 100% nhưng lại... sai (ví dụ: tự tin 99% đây là chó, nhưng thực ra là mèo).
- **Focal Loss:** $-(1 - \hat{y}_t)^\gamma \log(\hat{y}_t)$. Nếu mô hình đã dự đoán đúng và dễ ($\hat{y}_t \approx 1$), loss sẽ bị triệt tiêu về $0$.

## ⑥ Worked Example

Bài toán phân loại ảnh Mèo (1) và Chó (0). Ảnh đưa vào là Chó. Mô hình dự đoán xác suất là Mèo: $\hat{y} = 0.9$.

- $y = 0$. $\hat{y} = 0.9$.
- BCE Loss = $- [0 \cdot \log(0.9) + 1 \cdot \log(0.1)] = -\log(0.1) = 2.3$. (Phạt rất nặng vì tự tin sai).

## ⑩ Misconceptions

❌ **Sai:** `nn.CrossEntropyLoss` nhận đầu vào là xác suất (sau khi qua Softmax).
✅ **Đúng:** Đầu vào phải là **Logits** (giá trị thô chưa qua Softmax). PyTorch sẽ tự gộp Softmax và tính toán ở C cấp độ để tránh lỗi `NaN` (chia cho 0).

## ⑮ Mastery Check

- Tập dữ liệu phát hiện ung thư có 99% người khỏe, 1% người bệnh. Tại sao không nên dùng CrossEntropyLoss thông thường?
- L1 Loss khác L2 Loss điểm cốt lõi nào khi gặp nhiễu (outliers)?

## ⑯ Time Estimate

Theory: ~1h, Code: ~1h, Exercises: ~1h
