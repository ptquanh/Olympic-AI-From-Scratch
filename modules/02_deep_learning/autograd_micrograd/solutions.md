# Lời giải: Autograd & Micrograd

<details><summary><b>U-1 — Understand</b></summary>

Đạo hàm của $\max(0, x)$ là 1 nếu $x > 0$, và là 0 nếu $x \le 0$.
Vì vậy khi Backward qua hàm ReLU:

- Nếu dữ liệu (data) của node lớn hơn 0, nó sẽ cho phép toàn bộ Gradient đi qua nguyên vẹn (`self.grad += 1.0 * out.grad`).
- Nếu dữ liệu nhỏ hơn hoặc bằng 0, nó sẽ chặn Gradient lại (`self.grad += 0.0`). Hành động này giống như một cái van khóa dòng chảy gradient (Dead ReLU).

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

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

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

Tính tay phương trình: $z = 2x^2 - y^3 + xy$
Đạo hàm theo $x$: $\frac{\partial z}{\partial x} = 4x + y = 4(2) + (-3) = 5$
Đạo hàm theo $y$: $\frac{\partial z}{\partial y} = -3y^2 + x = -3(-3)^2 + 2 = -27 + 2 = -25$

Chạy bằng code, bạn cũng sẽ ra đúng kết quả này. Điều này chứng minh engine tự code của ta hoàn toàn chính xác.

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>

<details><summary><b>T-1 — Transfer</b></summary>

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

**Lỗi thường gặp:** fit preprocessing/chọn threshold trên test, dùng metric sai hoặc bỏ qua failure mode.

</details>

<details><summary><b>O-1 — Olympiad</b></summary>

Đáp án là một quy trình: baseline sớm, validation chống leakage, lưu seed/config, theo dõi metric và dành thời gian tái chạy artifact cuối. Chi tiết phụ thuộc profile kỳ thi; xem `olympiad_transfer.md`.

**Lỗi thường gặp:** áp luật của kỳ thi khác, không lưu config/artifact hoặc hết timebox mà chưa chạy infer cuối.

</details>
