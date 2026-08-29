# Regularization

> **Track:** Foundation ⭐ | Contest 📖

## ① Prerequisite Check

- Overfitting là gì? Bạn nhận biết nó trên đồ thị Loss như thế nào?

## ② Learning Outcomes

- Giải thích được tác dụng của Dropout và Batch Normalization.
- Cài đặt được Early Stopping để tránh Overfitting tự động.
- Biết cách thiết lập trạng thái `.train()` và `.eval()` cho mô hình.

## ③ Concept Map

Optimization ➔ **Regularization** ➔ Model Evaluation

## ④ Intuition

- **Dropout:** Giống như một phòng tập gym bắt các thành viên bịt mắt luân phiên. Khi một số người bị "tắt", những người còn lại phải tự gánh vác công việc, từ đó ai cũng trở nên mạnh mẽ và độc lập. Tránh việc mô hình quá phụ thuộc vào một đặc trưng cụ thể.
- **BatchNorm:** Giống như việc tổ chức lại đội hình. Khi tín hiệu đi qua nhiều lớp, nó bị méo mó (mean chạy lệch, variance phình to). BatchNorm kéo tất cả về mean=0, std=1, giúp luồng thông tin đi ổn định và học nhanh hơn cực kỳ nhiều.

## ⑤ Math/Derivation

- **Dropout:** Trong lúc train, mỗi nơ-ron có xác suất $p$ bị gán giá trị bằng 0. Giá trị của các nơ-ron sống sót được nhân với $\frac{1}{1-p}$ để giữ nguyên tổng năng lượng. Trong lúc test, không nơ-ron nào bị tắt (nhưng đã tắt dropout).
- **Weight Decay (L2):** Cộng thêm $\lambda \sum w^2$ vào hàm Loss, ép các trọng số $w$ phải nhỏ, ngăn mô hình vẽ ra đường biên quá phức tạp.

## ⑥ Worked Example

Mô hình chạy qua 50 epochs.

- Train Loss tiếp tục giảm từ 0.1 -> 0.05 -> 0.01.
- Validation Loss lại bắt đầu TĂNG từ 0.3 -> 0.4 -> 0.6.
  Đó là tín hiệu Overfitting. Nếu áp dụng Early Stopping với `patience=5`, vòng lặp sẽ tự động ngắt ở epoch 55 (lấy lại model tốt nhất ở epoch 50).

## ⑩ Misconceptions

❌ **Sai:** Có thể dùng cả Dropout và BatchNorm chung một chỗ thoải mái.
✅ **Đúng:** Nhiều nghiên cứu chỉ ra Dropout và BatchNorm đôi khi "đánh nhau" (Variance Shift). Nếu dùng, hãy đặt theo thứ tự: Linear -> BatchNorm -> Kích hoạt -> Dropout. Ở các kiến trúc mới (CNN, ResNet), người ta thường chỉ dùng BatchNorm và bỏ luôn Dropout.

## ⑮ Mastery Check

- Lệnh `model.eval()` làm thay đổi hành vi của lớp nào trong mạng?
- Tại sao BatchNorm lại giúp sử dụng Learning Rate lớn hơn?

## ⑯ Time Estimate

Theory: ~1h, Code: ~1h, Exercises: ~1h
