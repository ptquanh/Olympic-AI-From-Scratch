# Lời giải: Autograd & Micrograd

<details><summary><b>Tầng 1: Understand</b></summary>

Đạo hàm của $\max(0, x)$ là 1 nếu $x > 0$, và là 0 nếu $x \le 0$.
Vì vậy khi Backward qua hàm ReLU:

- Nếu dữ liệu (data) của node lớn hơn 0, nó sẽ cho phép toàn bộ Gradient đi qua nguyên vẹn (`self.grad += 1.0 * out.grad`).
- Nếu dữ liệu nhỏ hơn hoặc bằng 0, nó sẽ chặn Gradient lại (`self.grad += 0.0`). Hành động này giống như một cái van khóa dòng chảy gradient (Dead ReLU).
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
def __pow__(self, other):
    assert isinstance(other, (int, float)), "only supporting int/float powers for now"
    out = Value(self.data**other, (self,), f'**{other}')

    def _backward():
        # Đạo hàm của x^n là n * x^(n-1)
        self.grad += (other * (self.data ** (other - 1))) * out.grad

    out._backward = _backward
    return out
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

Tính tay phương trình: $z = 2x^2 - y^3 + xy$
Đạo hàm theo $x$: $\frac{\partial z}{\partial x} = 4x + y = 4(2) + (-3) = 5$
Đạo hàm theo $y$: $\frac{\partial z}{\partial y} = -3y^2 + x = -3(-3)^2 + 2 = -27 + 2 = -25$

Chạy bằng code, bạn cũng sẽ ra đúng kết quả này. Điều này chứng minh engine tự code của ta hoàn toàn chính xác.

</details>

<details><summary><b>Tầng 4: Transfer</b></summary>

```python
def backward(self):
    topo = []
    visited = set()

    def build_topo(v):
        if v not in visited:
            visited.add(v)
            for child in v._prev:
                build_topo(child)
            topo.append(v)

    build_topo(self)

    # Khởi tạo đạo hàm đầu nguồn bằng 1
    self.grad = 1.0
    # Đảo ngược danh sách và thực thi backward từ đỉnh xuống gốc
    for node in reversed(topo):
        node._backward()
```

</details>
