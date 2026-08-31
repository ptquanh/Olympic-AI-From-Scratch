# Lời giải: Augmentation

<details><summary><b>U-1 — Understand</b></summary>
KHÔNG. Nếu lật ngang, số 3 có thể biến thành chữ E, số 9 lật có thể không ra số gì. Nhãn (Label) bị mất ý nghĩa.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

```python
import torchvision.transforms as T
transform = T.Compose([
    T.Resize(256),
    T.RandomCrop(224),
    T.ToTensor()
])

```

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

```python
import torchvision.transforms as T
import torch

img = torch.rand(1, 100, 100) # Ảnh ngẫu nhiên [0, 1]
norm = T.Normalize((0.5,), (0.5,))
out = norm(img)

print("Min:", out.min().item())
print("Max:", out.max().item())

```

Kết quả sẽ nằm trong khoảng [-1, 1]. Phép tính là `(x - 0.5) / 0.5 = 2x - 1`. Do x thuộc [0, 1] nên 2x-1 thuộc [-1, 1].

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>
