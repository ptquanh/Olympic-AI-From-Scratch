# Lời giải: Linear Regression

<details><summary><b>U-1 — Understand</b></summary>

Dùng bình phương vì hàm mũ 2 (Parabol) trơn tru, luôn có đạo hàm tại mọi điểm (giúp Gradient Descent hoạt động tốt). Hàm trị tuyệt đối hình chữ V bị gãy khúc ở đáy, không có đạo hàm tại đỉnh.

MSE còn phạt sai số lớn mạnh hơn MAE và có nghiệm đóng trong hồi quy tuyến tính khi ma trận đủ điều kiện. MAE vẫn tối ưu được bằng subgradient; “không có đạo hàm tại 0” không có nghĩa là MAE không dùng được.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

Lỗi: `W = W + lr * dW`.
Gradient Descent là trượt **ngược** chiều đạo hàm để tìm đáy.
Sửa lại: `W = W - lr * dW`

```python
import numpy as np
X = np.array([[1.0], [2.0], [3.0]])
y = np.array([2.0, 4.0, 6.0])
W = np.zeros(1); lr = 0.1
before = np.mean((X @ W - y) ** 2)
dW = 2 * X.T @ (X @ W - y) / len(y)
W = W - lr * dW
after = np.mean((X @ W - y) ** 2)
assert after < before

```

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

Không thể kết luận chỉ từ giá trị learning rate: ngưỡng ổn định phụ thuộc scale của `X` và phổ của `X.T @ X`. Chạy cùng seed/data, ghi loss cuối và trạng thái hữu hạn. Trên dữ liệu notebook hiện tại, `1.5` có thể phân kỳ, `0.0001` thường chậm và `0.1` thường nhanh hơn; đây là quan sát, không phải định luật.

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>

<details><summary><b>T-1 — Transfer</b></summary>

Không chọn bậc chỉ bằng mắt trên train. Dùng pipeline để tránh fit preprocessing ngoài fold, so sánh validation MSE và chỉ kết luận cho seed/split đã dùng:

```python
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

model = make_pipeline(PolynomialFeatures(5), StandardScaler(), LinearRegression())
model.fit(X_train, y_train)
score = ((model.predict(X_valid) - y_valid) ** 2).mean()
assert score >= 0

```

Bậc 15 có nguy cơ variance/điều kiện số lớn, nhưng không được tuyên bố chắc chắn overfit nếu chưa đo validation.

**Lỗi thường gặp:** fit preprocessing/chọn threshold trên test, dùng metric sai hoặc bỏ qua failure mode.

</details>

<details><summary><b>O-1 — Olympiad</b></summary>

Đáp án là một quy trình: baseline sớm, validation chống leakage, lưu seed/config, theo dõi metric và dành thời gian tái chạy artifact cuối. Chi tiết phụ thuộc profile kỳ thi; xem `olympiad_transfer.md`.

**Lỗi thường gặp:** áp luật của kỳ thi khác, không lưu config/artifact hoặc hết timebox mà chưa chạy infer cuối.

</details>
