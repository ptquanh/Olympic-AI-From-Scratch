# Autograd & Micrograd

> **Track:** Foundation ⭐ | Contest 📖

## ① Prerequisite Check

- Đạo hàm của $f(x) = x^2$ là gì?
- Chain Rule (Quy tắc chuỗi) trong giải tích là gì? Nếu $y = f(u)$ và $u = g(x)$ thì $\frac{dy}{dx}$ bằng gì?

## ② Learning Outcomes

- Hiểu được cấu trúc dữ liệu cơ bản tạo nên Đồ thị tính toán (Computation Graph).
- Tự tay viết được một class `Value` bằng Python thuần lưu trữ dữ liệu và độ dốc (gradient).
- Triển khai thuật toán Backpropagation bằng Python thuần trên đồ thị tính toán do chính bạn tạo ra (Micrograd).

## ③ Concept Map

PyTorch Fundamentals ➔ **Autograd & Micrograd** ➔ Backprop & Training Loop.
Hiểu phần này, PyTorch sẽ không còn là một chiếc hộp đen ma thuật đối với bạn nữa.

## ④ Intuition

Khi bạn dùng PyTorch, làm sao nó biết được đạo hàm của một hàm cực kỳ phức tạp (như hàm có 1 tỷ tham số)? Bí mật nằm ở chỗ: mọi hàm số, dù phức tạp đến đâu, đều được máy tính băm nhỏ thành các phép tính cơ bản nhất (cộng, trừ, nhân, chia, mũ). Nếu máy tính biết cách tính đạo hàm cho từng phép toán cơ bản này, và lưu lại quá trình cộng trừ nhân chia đó vào một **đồ thị** (cây gia phả), thì việc tính đạo hàm của toàn bộ hàm số khổng lồ kia chỉ là việc áp dụng **Chain Rule** (Quy tắc chuỗi) để nhân ngược các đạo hàm nhỏ lại với nhau từ ngọn cây về gốc cây.

## ⑤ Math/Derivation

Chain Rule:
$\frac{\partial z}{\partial x} = \frac{\partial z}{\partial y} \cdot \frac{\partial y}{\partial x}$

Trong đồ thị tính toán:

1. Node chứa: `data` (giá trị thực), `grad` (đạo hàm của output cuối cùng theo node này).
2. Khi tính đạo hàm (Backward): Node con nhận `grad` truyền từ Node cha xuống, nhân với đạo hàm cục bộ (Local Gradient) của chính nó, rồi truyền tiếp xuống dưới.

## ⑥ Worked Example

Xét biểu thức $f = 3x + y$. Nếu $x = -2, y = 5$, ta có $f = -1$.
Tại node $f$, đạo hàm $\frac{\partial f}{\partial f} = 1$.
Truyền ngược xuống node $y$: $\frac{\partial f}{\partial y} = 1$.
Truyền ngược xuống node $(3x)$: $\frac{\partial f}{\partial (3x)} = 1$.
Từ node $(3x)$, truyền xuống $x$: Đạo hàm cục bộ của $3x$ theo $x$ là $3$. Vậy đạo hàm toàn phần $\frac{\partial f}{\partial x} = 1 \times 3 = 3$.

## ⑩ Misconceptions

❌ **Sai:** Máy tính giải phương trình đạo hàm bằng công thức toán học giống như học sinh cấp 3.
✅ **Đúng:** Máy tính sử dụng Automatic Differentiation (Autograd). Nó xây dựng một đồ thị các phép toán và nhân các đạo hàm cục bộ (bằng con số thực) lại với nhau.

## ⑮ Mastery Check

- Tại sao khi cập nhật trọng số xong ta lại phải có bước `zero_grad()`?
- Gradient của phép toán $z = x + y$ được chia sẻ như thế nào cho $x$ và $y$?

## ⑯ Time Estimate

Theory: ~2h, Code: ~3h, Exercises: ~2h
