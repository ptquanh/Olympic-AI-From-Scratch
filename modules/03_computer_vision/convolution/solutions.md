# Lời giải: Convolution

<details><summary><b>Tầng 1: Understand</b></summary>
Mỗi out_channel đại diện cho một "bộ lọc" (filter) chuyên biệt. Ví dụ: Filter 1 chuyên tìm đường thẳng đứng, Filter 2 tìm đường chéo, Filter 3 tìm góc vuông, Filter 4 tìm vùng màu đỏ. Việc tạo ra nhiều out_channels giúp mạng lưới học được đồng thời rất nhiều đặc trưng khác nhau của ảnh.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>
Áp dụng công thức: $W_{out} = \lfloor\frac{W_{in} + 2P - K}{S}\rfloor + 1$
$W_{out} = \lfloor\frac{128 + 2(2) - 5}{3}\rfloor + 1 = \lfloor\frac{127}{3}\rfloor + 1 = 42 + 1 = 43$.
Vậy kích thước đầu ra là 43x43.
</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sample_image.jpg', cv2.IMREAD_GRAYSCALE)
kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

# Áp dụng chập
edges = cv2.filter2D(img, -1, kernel)

plt.imshow(edges, cmap='gray')
plt.show()
```

Đồ thị sẽ nổi bật lên toàn bộ những đường thẳng dọc trong bức ảnh gốc.

</details>

<details><summary><b>Tầng 4: Transfer</b></summary>

```python
import torch
import torch.nn as nn

x = torch.randn(32, 16, 8, 8)
flatten = nn.Flatten()
out = flatten(x)
print(out.shape) # (32, 1024)
```

</details>
