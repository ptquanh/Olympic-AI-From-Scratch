# Convolution

> **Track:** Foundation ⭐ | Contest 📖

## ① Prerequisite Check

- Bạn có hiểu phép nhân vô hướng (Dot Product) của 2 ma trận không?
- Mạng truyền thẳng (MLP) có nhược điểm gì khi xử lý ảnh?

## ② Learning Outcomes

- Hiểu được cơ chế trượt (Sliding Window) của Kernel trên ảnh.
- Cài đặt được phép tích chập (Conv2d) bằng Numpy từ con số 0.
- Giải thích được ý nghĩa và công thức tính toán của Stride, Padding.
- Khái niệm Receptive Field và lý do mạng chập (CNN) có thể "nhìn" được bối cảnh rộng hơn.

## ③ Concept Map

PyTorch Fundamentals ➔ **Convolution** ➔ CNN Architectures

## ④ Intuition

Một bức ảnh có thể có hàng triệu pixel. Fully connected layer trên ảnh lớn tạo rất nhiều tham số và bỏ qua cấu trúc không gian. Convolution dùng kernel nhỏ (ví dụ 3×3) với **trọng số được học và chia sẻ theo vị trí**, quét trên ảnh. Điều này giúp mạng:

1. Chia sẻ trọng số (cùng một kính lúp quét mọi nơi).
2. Bảo toàn tính không gian (nhận diện được mắt nằm trên miệng).

## ⑤ Math/Derivation

Kích thước ảnh đầu ra sau phép chập (cho 1 chiều, ví dụ Width):
$W_{out} = \lfloor\frac{W_{in} + 2P - K}{S}\rfloor + 1$
Trong đó:

- $W_{in}$: Kích thước đầu vào.
- $P$: Padding (đệm viền 0).
- $K$: Kích thước Kernel.
- $S$: Stride (bước nhảy).

## ⑥ Worked Example

Giả sử ảnh đầu vào 5x5. Kernel 3x3. Padding = 1. Stride = 2.
$W_{out} = \frac{5 + 2(1) - 3}{2} + 1 = \frac{4}{2} + 1 = 3$.
Vậy output sẽ là một ma trận 3x3.

## ⑩ Misconceptions

❌ **Sai:** Convolution trong Deep Learning giống hệ Convolution trong Toán tín hiệu.
✅ **Đúng:** Trong Toán tín hiệu, bạn phải "lật" (flip) kernel trước khi nhân. Deep Learning thì bỏ qua bước lật này (thực chất nó gọi là Cross-Correlation), nhưng giới AI vẫn quen miệng gọi là Convolution.

## ⑮ Mastery Check

- Làm sao để sau khi tích chập, ảnh output vẫn giữ nguyên kích thước (W, H) như input?
- 1 Conv layer có $C_{in}=3, C_{out}=16$, Kernel=3x3. Có tổng cộng bao nhiêu tham số (weights + bias)?

## ⑯ Time Estimate

Theory: ~1h, Code: ~2h, Exercises: ~1h
