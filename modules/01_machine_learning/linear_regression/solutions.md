# Lời giải: Linear Regression

<details><summary><b>Tầng 1: Understand</b></summary>

Dùng bình phương vì hàm mũ 2 (Parabol) trơn tru, luôn có đạo hàm tại mọi điểm (giúp Gradient Descent hoạt động tốt). Hàm trị tuyệt đối hình chữ V bị gãy khúc ở đáy, không có đạo hàm tại đỉnh.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

Lỗi: `W = W + lr * dW`.
Gradient Descent là trượt **ngược** chiều đạo hàm để tìm đáy.
Sửa lại: `W = W - lr * dW`

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

- `lr = 1.5`: Quá lớn, Loss sẽ nhảy lên hàng tỷ rồi NaN (Diverge).
- `lr = 0.0001`: Quá nhỏ, Loss giảm rất chậm, chưa tới đáy sau 1000 iter.
- `lr = 0.1`: Vừa phải, Loss hội tụ (Converge).
</details>

<details><summary><b>Tầng 4: Transfer</b></summary>

Bậc 3 chưa fit được 2 chu kỳ của Sin. Bậc 5 fit vừa đủ. Bậc 15 sẽ uốn lượn liên tục qua từng điểm nhiễu (Overfit nặng nề).

</details>
