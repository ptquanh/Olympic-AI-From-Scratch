# Activation Functions

> **Track:** Foundation ⭐ | Contest ⏭️

## ① Prerequisite Check

- Mạng nơ ron thuần tuyến tính (chỉ dùng phép nhân ma trận) khác gì với Hồi quy tuyến tính (Linear Regression)?
- Hàm ReLU hoạt động như thế nào với đầu vào âm?

## ② Learning Outcomes

- Phân tích được ưu nhược điểm và chọn đúng hàm kích hoạt (ReLU, Sigmoid, Tanh, GELU) cho từng bài toán.
- Giải thích được nguyên nhân gây ra hiện tượng Vanishing Gradient và Dead ReLU.

## ③ Concept Map

PyTorch Fundamentals ➔ **Activation Functions** ➔ Loss Functions ➔ Optimization

## ④ Intuition

Nếu không có hàm kích hoạt, việc chồng 100 lớp nơ-ron lên nhau cũng vô nghĩa vì phép nhân ma trận có tính phân phối (nhiều phép nhân gộp lại chỉ bằng 1 phép nhân duy nhất). Hàm kích hoạt giống như một cái "bản lề" bẻ cong không gian dữ liệu, giúp mạng nơ-ron có thể vẽ được những đường ranh giới phức tạp để nhận diện chó, mèo, khuôn mặt...

## ⑤ Math/Derivation

- **Sigmoid:** $\sigma(x) = \frac{1}{1 + e^{-x}}$. Range: $(0, 1)$. Đạo hàm cực đại: $0.25$.
- **Tanh:** $\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$. Range: $(-1, 1)$. Đạo hàm cực đại: $1$.
- **ReLU:** $f(x) = \max(0, x)$. Range: $[0, \infty)$. Đạo hàm: $1$ nếu $x>0$, $0$ nếu $x \le 0$.
- **GELU:** $f(x) = x \cdot \Phi(x)$ (với $\Phi(x)$ là phân phối chuẩn tích lũy). Mượt mà hơn ReLU.

## ⑥ Worked Example

Khi mạng học được đặc trưng "cái tai mèo" mang giá trị âm ($x = -5$), ReLU sẽ ép giá trị đó về $0$, coi như nơ-ron đó không kích hoạt (tắt). Nếu là "cái tai mèo" rõ ràng ($x = 5$), ReLU giữ nguyên $5$, tín hiệu được truyền đi mạnh mẽ.

## ⑩ Misconceptions

❌ **Sai:** ReLU luôn là hàm tốt nhất.
✅ **Đúng:** ReLU tốt nhất cho Hidden Layers của các mạng CNN truyền thống. Nhưng với LLM (Transformer), GELU hoặc SwiGLU mới là chuẩn mực. Output layer thì phải dùng Sigmoid (phân loại nhị phân) hoặc Softmax (phân loại đa lớp).

## ⑮ Mastery Check

- Tại sao người ta ít dùng Tanh ở các lớp ẩn sâu?
- "Dead ReLU" xảy ra khi nào?

## ⑯ Time Estimate

Theory: ~1h, Code: ~0.5h, Exercises: ~1h
