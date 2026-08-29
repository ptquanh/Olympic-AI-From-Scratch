# PyTorch Fundamentals

> **Track:** Foundation ⭐ | Contest 📖

## ① Prerequisite Check

- Bạn có hiểu khái niệm Broadcasting trong NumPy không?
- Bạn có biết ma trận chuyển vị (Transpose) và nhân ma trận (Dot Product) khác nhau thế nào không?

## ② Learning Outcomes

- Khởi tạo và thao tác cơ bản (Reshape, Squeeze, Unsqueeze) với PyTorch Tensor.
- Giải thích được điểm khác biệt cốt lõi giữa NumPy Array và PyTorch Tensor (Autograd & GPU acceleration).
- Chuyển đổi dữ liệu linh hoạt giữa CPU và GPU.
- Tự viết được một class kế thừa từ `torch.utils.data.Dataset` và bọc trong `DataLoader`.
- Tự tay viết được một vòng lặp huấn luyện (Training Loop) cơ bản trong PyTorch.

## ③ Concept Map

NumPy / Math Essentials ➔ **PyTorch Fundamentals** ➔ Backpropagation / Autograd ➔ Các kiến trúc mạng Neural phức tạp.

## ④ Intuition

PyTorch giống hệt như NumPy, nhưng nó được trang bị thêm "tên lửa". Tên lửa thứ nhất là khả năng chạy tính toán song song hàng loạt trên GPU (card đồ họa). Tên lửa thứ hai là Autograd — tính năng tự động ghi nhớ các phép toán bạn làm để tự động tính đạo hàm (cực kỳ cần thiết cho việc huấn luyện AI).

## ⑤ Math/Derivation

Trong AI, dữ liệu thường ở dạng "Tensor". Tensor bản chất chỉ là mảng đa chiều:

- 0D Tensor: Scalar (một con số, vd: `5`)
- 1D Tensor: Vector (vd: `[1, 2, 3]`)
- 2D Tensor: Ma trận (vd: ảnh xám chiều cao × chiều rộng)
- 3D Tensor: Vd: ảnh màu (Channels × Height × Width)
- 4D Tensor: Vd: Một lô ảnh (Batch size × Channels × Height × Width)

## ⑥ Worked Example

Khi ta có 1 ảnh màu RGB cỡ 28x28. Shape của nó trong máy tính thường là `(28, 28, 3)`. Tuy nhiên, PyTorch lại quy ước channel first: `(3, 28, 28)`. Khi ta nhóm 32 ảnh lại để đẩy vào mô hình cùng 1 lúc (gọi là mini-batch), ta sẽ có tensor shape là `(32, 3, 28, 28)`.

## ⑩ Misconceptions

❌ **Sai:** `.reshape()` và `.view()` trong PyTorch là y hệt nhau.
✅ **Đúng:** `.view()` chỉ hoạt động trên tensor liên tục trong bộ nhớ (contiguous), nó không tạo ra dữ liệu mới. `.reshape()` linh hoạt hơn, nó sẽ trả về view nếu được, còn không nó sẽ tự copy dữ liệu. Dùng `.reshape()` an toàn hơn.

❌ **Sai:** Dùng vòng lặp `for` để tính toán từng phần tử của Tensor.
✅ **Đúng:** Luôn dùng các phép toán ma trận được tích hợp sẵn (Vectorization). Vòng lặp `for` sẽ triệt tiêu sức mạnh của PyTorch.

## ⑮ Mastery Check

- Bạn làm cách nào để tính tổng các phần tử của một Tensor theo từng cột?
- Làm sao để gửi mô hình từ CPU sang GPU?
- Khi lấy tensor từ GPU về NumPy, bạn phải dùng những lệnh nào?

## ⑯ Time Estimate

Theory: ~1h, Code: ~2h, Exercises: ~2h
