# Lời giải: Augmentation

<details><summary><b>Tầng 1: Understand</b></summary>
KHÔNG. Nếu lật ngang, số 3 có thể biến thành chữ E, số 9 lật có thể không ra số gì. Nhãn (Label) bị mất ý nghĩa.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
import torchvision.transforms as T
transform = T.Compose([
    T.Resize(256),
    T.RandomCrop(224),
    T.ToTensor()
])
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

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

</details>
