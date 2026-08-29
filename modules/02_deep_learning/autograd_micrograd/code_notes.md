# Code Notes: Autograd & Micrograd

## 🔑 Core Patterns

### Pattern 1: Cấu trúc cơ bản của một Node tính toán (Micrograd style)

```python
class Value:
    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data
        self.grad = 0.0 # Bắt đầu, gradient luôn là 0
        self._backward = lambda: None # Hàm ẩn để thực thi tính toán ngược
        self._prev = set(_children) # Lưu lại các node cha đã tạo ra node này
        self._op = _op
        self.label = label

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"
```

### Pattern 2: Cài đặt phép Cộng với Local Gradient

```python
    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')

        def _backward():
            # Đối với phép cộng (z = x + y), dz/dx = 1 và dz/dy = 1
            # Theo quy tắc chuỗi: grad_của_x += grad_của_out * 1.0
            self.grad += 1.0 * out.grad
            other.grad += 1.0 * out.grad

        out._backward = _backward
        return out
```

### Pattern 3: Cài đặt phép Nhân

```python
    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')

        def _backward():
            # Đối với z = x * y, dz/dx = y và dz/dy = x
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad

        out._backward = _backward
        return out
```

## 📋 API Cheat Sheet

Bài học này xây dựng API from-scratch nên không có cheat sheet thư viện.
Trong PyTorch, logic này tương ứng với:
`x = torch.tensor([2.0], requires_grad=True)`
`y = x * 3`
`y.backward()`
`print(x.grad)`

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                                   | Thời gian | Hint (ẩn)                                                                                            |
| --- | --------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------- |
| 1   | Cài đặt phép trừ `__sub__` cho class Value.                           | 3 phút    | Gọi `self + (-other)`. Nếu không, tự viết đạo hàm: `self.grad += out.grad`, `other.grad -= out.grad` |
| 2   | Cài đặt hàm mũ tự nhiên `exp()`. Đạo hàm của $e^x$ là chính nó $e^x$. | 4 phút    | `out = Value(math.exp(self.data))`, `self.grad += out.data * out.grad`                               |

## 🧠 Flashcards

| Hỏi                                                                                 | Trả lời                                                                                                                                      |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Phép cộng định tuyến Gradient như thế nào?                                          | Phép cộng đóng vai trò như một "bộ định tuyến", nó copy gradient nguyên xi truyền xuống cho tất cả các nhánh con của nó.                     |
| Tại sao phải dùng toán tử cộng dồn (`+=`) khi tính gradient thay vì gán bằng (`=`)? | Vì một biến có thể tham gia vào nhiều phép toán khác nhau trong đồ thị. Nếu dùng `=`, gradient sẽ bị ghi đè thay vì được tích lũy tổng cộng. |
