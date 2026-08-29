# Lời giải: Math Essentials

<details><summary><b>Tầng 1: Understand</b></summary>

**1. Đạo hàm (Derivative/Gradient)**
Gradient vector chỉ ra hướng mà hàm số sẽ TĂNG LÊN dốc nhất. Trong AI, ta muốn làm GIẢM hàm lỗi (Loss), nên ta đi ngược hướng gradient (Gradient Descent).

**2. Tích vô hướng (Dot Product)**
Nếu Dot Product lớn, tức là hai vector chiếu lên nhau dài, góc giữa chúng nhỏ -> Chúng "giống nhau" (Cosine Similarity).
Nếu bằng 0, hai vector vuông góc -> Hoàn toàn không liên quan.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

**1. MSE Gradient from scratch**

```python
# L = (W*X - Y)^2
# dL/dW = 2 * X * (W*X - Y)
# Tính tay:
# W*X = 2 * 3 = 6
# W*X - Y = 6 - 5 = 1
# dL/dW = 2 * 3 * 1 = 6
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

**1. Chấm dứt vòng lặp vô tận**
Một hàm Gradient Descent cần điểm dừng.

1. `max_epochs`: Chạy cố định N vòng.
2. `patience` / `early_stopping`: Nếu Loss không giảm thêm quá `epsilon` (ví dụ `1e-5`) sau vài vòng thì dừng sớm.
3. Nếu Loss bùng nổ ra `NaN` (ví dụ learning rate quá to) thì cũng phải bẫy lỗi và break.
</details>
