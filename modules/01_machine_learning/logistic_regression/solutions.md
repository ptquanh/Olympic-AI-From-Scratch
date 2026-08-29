# Lời giải: Logistic Regression

<details><summary><b>Tầng 1: Understand</b></summary>

Nếu dùng MSE + Sigmoid, hàm Loss sẽ là **Non-convex** (Nhiều đáy cục bộ). Gradient Descent dễ bị kẹt ở đáy cục bộ (Local Minima) và không tìm được nghiệm tốt nhất. Cross-Entropy Loss đảm bảo hàm là **Convex** (chỉ có 1 cái đáy sâu nhất - Global Minimum).

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

Dự đoán là class 1 (vì 0.4 lớn nhất). Dùng `np.argmax(probs, axis=1)`.

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

Với `C=1000`, trọng số thường rất lớn (vd: > 10.0). Với `C=0.01`, các trọng số bị ép nhỏ gần bằng 0 (vd: < 0.1). L2 Regularization hoạt động mạnh khi C nhỏ.

</details>

<details><summary><b>Tầng 4: Transfer</b></summary>

Tham số `class_weight='balanced'`. Nó sẽ tự động tính toán để phạt mô hình nặng gấp 99 lần nếu đoán sai 1 giao dịch lừa đảo.

</details>
