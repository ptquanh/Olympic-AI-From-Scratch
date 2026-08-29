# Backprop & Training Loop

> **Track:** Foundation ⭐ | Contest 📖

## ① Prerequisite Check

- Bạn có hiểu cách Autograd (Micrograd) tự động truyền ngược gradient ở chương trước không?
- Bạn có nhớ 5 bước của một vòng lặp huấn luyện chuẩn bên PyTorch Fundamentals không?

## ② Learning Outcomes

- Kết nối class `Value` (Autograd Engine) thành một cấu trúc Mạng Nơ-ron hoàn chỉnh: `Neuron`, `Layer`, `MLP`.
- Khởi tạo ngẫu nhiên trọng số và bias cho toàn bộ mạng.
- Tự tay viết hàm lan truyền tiến (Forward Pass).
- Viết vòng lặp huấn luyện hoàn chỉnh để giải bài toán phân loại nhị phân siêu đơn giản (không dùng PyTorch).

## ③ Concept Map

Autograd & Micrograd ➔ **Backprop & Training Loop** ➔ Tối ưu hóa (Optimization, Loss, Activation).
Chương này đánh dấu việc bạn đã tự tay build thành công một mô hình Deep Learning từ con số 0.

## ④ Intuition

Mạng nơ-ron thực chất là một chuỗi các phép toán nhân ma trận và cộng vector.

- 1 Neuron: Nhận nhiều inputs, nhân với trọng số tương ứng (weights), cộng bias, rồi đẩy qua hàm kích hoạt (activation).
- 1 Layer: Gồm nhiều Neurons nằm cạnh nhau.
- Mạng đa tầng (MLP - Multi-Layer Perceptron): Gồm nhiều Layers xếp nối tiếp nhau.
  Khi ta cho mạng ăn dữ liệu, luồng dữ liệu chạy từ đầu đến cuối tạo ra dự đoán (Forward Pass). Dựa trên sai số (Loss), Autograd tính đạo hàm truyền ngược lại (Backward Pass). Có đạo hàm, ta tiến hành cập nhật trọng số để mạng thông minh hơn (Gradient Descent).

## ⑤ Math/Derivation

Thuật toán Gradient Descent cập nhật trọng số bằng công thức:
$w = w - \eta \cdot \frac{\partial L}{\partial w}$
Trong đó:

- $w$: Trọng số hiện tại.
- $\eta$: Tốc độ học (Learning Rate), thường lấy giá trị nhỏ như 0.01.
- $\frac{\partial L}{\partial w}$: Đạo hàm của hàm mất mát (Loss) theo trọng số $w$ (do quá trình backward cung cấp).

## ⑥ Worked Example

Sử dụng hàm mất mát SVM (Max-Margin Loss) hoặc Mean Squared Error.
Ví dụ mạng dự đoán ra kết quả `y_pred = 0.8`, nhãn thật `y_true = 1.0`.
Hàm MSE: $L = (0.8 - 1.0)^2 = 0.04$.
Sau khi gọi `L.backward()`, ta cập nhật toàn bộ `w` và `b` của mạng bằng lệnh:
`p.data -= 0.01 * p.grad` (với `p` là từng tham số trong mạng).

## ⑩ Misconceptions

❌ **Sai:** Chỉ cần tính đạo hàm xong là trọng số tự thay đổi.
✅ **Đúng:** Tính đạo hàm (Backward) chỉ cung cấp thông tin "cần phải thay đổi như thế nào". Trọng số chỉ thực sự thay đổi khi bạn gọi hàm Cập nhật (Optimizer Step / Gradient Descent).

## ⑮ Mastery Check

- Làm sao để mô hình có thể mô phỏng lại các đường cong phức tạp (phi tuyến tính)?
- Nếu không gọi `zero_grad()` ở đầu mỗi vòng lặp thì mô hình sẽ ra sao?

## ⑯ Time Estimate

Theory: ~1h, Code: ~3h, Exercises: ~2h
