# Code Notes: Backprop & Training Loop

## 🔑 Core Patterns

### Pattern 1: Cấu trúc của một Neuron (Micrograd style)

```python
import random

class Neuron:
    def __init__(self, nin):
        # nin: số lượng input. Khởi tạo weight và bias ngẫu nhiên từ -1 đến 1
        self.w = [Value(random.uniform(-1, 1)) for _ in range(nin)]
        self.b = Value(random.uniform(-1, 1))

    def __call__(self, x):
        # w * x + b
        act = sum((wi * xi for wi, xi in zip(self.w, x)), self.b)
        # Đi qua hàm kích hoạt phi tuyến tính (ví dụ ReLU)
        out = act.relu()
        return out

    def parameters(self):
        return self.w + [self.b]

```

### Pattern 2: Cấu trúc của một Tầng (Layer) và Mạng (MLP)

```python
class Layer:
    def __init__(self, nin, nout):
        self.neurons = [Neuron(nin) for _ in range(nout)]

    def __call__(self, x):
        outs = [n(x) for n in self.neurons]
        return outs[0] if len(outs) == 1 else outs

    def parameters(self):
        return [p for neuron in self.neurons for p in neuron.parameters()]

class MLP:
    def __init__(self, nin, nouts):
        # nin: input size, nouts: list of sizes of hidden layers + output layer
        sz = [nin] + nouts
        self.layers = [Layer(sz[i], sz[i+1]) for i in range(len(nouts))]

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]

```

### Pattern 3: Training Loop From Scratch

```python
# Mạng có 3 input, 2 hidden layer (mỗi cái 4 nơ ron), 1 output layer
n = MLP(3, [4, 4, 1])

# Training Loop
for k in range(20):
    # 1. Forward pass
    ypred = [n(x) for x in xs]

    # 2. Tính Loss (MSE)
    loss = sum((yout - ygt)**2 for yout, ygt in zip(ypred, ys))

    # 3. Zero grad
    for p in n.parameters():
        p.grad = 0.0

    # 4. Backward
    loss.backward()

    # 5. Gradient Descent (Cập nhật trọng số)
    for p in n.parameters():
        p.data -= 0.05 * p.grad

```

## 📋 API Cheat Sheet

Chương này thực hành code từ đầu bằng Python thuần, không sử dụng API thư viện ngoài.

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                                         | Thời gian | Hint (ẩn)                           |
| --- | --------------------------------------------------------------------------- | --------- | ----------------------------------- |
| 1   | Sửa đoạn code tính Loss trong Pattern 3 thành loss Trung bình thay vì Tổng. | 3 phút    | Dùng `sum() / len(ys)`              |
| 2   | Viết nhanh đoạn code Zero Grad cho một danh sách các parameters.            | 2 phút    | Dùng vòng lặp for gán `.grad = 0.0` |

## 🧠 Flashcards

| Hỏi                                                                          | Trả lời                                                                                                                                                             |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chuyện gì xảy ra nếu quên khởi tạo weights ngẫu nhiên mà gán toàn bộ bằng 0? | Tất cả nơ-ron sẽ tính ra cùng một kết quả, đạo hàm bằng nhau, và chúng sẽ học chung một đặc trưng. Mạng sẽ vĩnh viễn không hội tụ được (Symmetry Breaking failure). |
| Tại sao hàm Loss lại cần đi kèm với Label (Y)?                               | Mạng sẽ không thể biết được output hiện tại của nó là đúng hay sai nếu không có "đáp án" để đối chiếu. Hàm Loss là bộ so sánh đáp án đó.                            |
