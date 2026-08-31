# Lời giải: Generative CV

<details><summary><b>U-1 — Understand</b></summary>

GAN discriminator nhận ảnh thật/giả và học binary classification; generator nhận gradient qua discriminator để làm mẫu khó phân biệt. Failure modes gồm training mất cân bằng và mode collapse. DDPM thường lấy `x0`, timestep và noise `ε`, tạo `x_t`, rồi tối ưu model dự đoán noise/velocity/target tương ứng. Failure modes gồm sampling chậm và schedule/parameterization không phù hợp.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

```python
def q_sample(x0, noise, alpha_bar):
    if not 0 <= alpha_bar <= 1:
        raise ValueError("alpha_bar must be in [0, 1]")
    if x0.shape != noise.shape:
        raise ValueError("x0 and noise must have the same shape")
    return np.sqrt(alpha_bar) * x0 + np.sqrt(1-alpha_bar) * noise

```

`np.allclose(q_sample(x0,n,1),x0)` và `np.allclose(q_sample(x0,n,0),n)` phải đúng.

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

Giữ `x0/noise` cố định để chỉ thay một biến. Với `x0=np.ones(1000)` và Gaussian noise seed 42, tính `np.mean((xt-x0)**2)`. Giá trị cụ thể phụ thuộc mẫu noise, nhưng trend tăng khi `alpha_bar` giảm. Không so các timestep bằng noise seed khác vì variance ngẫu nhiên làm mờ causal effect.

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>
