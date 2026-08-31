# Lời giải: Convolution

<details><summary><b>U-1 — Understand</b></summary>
Mỗi out_channel đại diện cho một "bộ lọc" (filter) chuyên biệt. Ví dụ: Filter 1 chuyên tìm đường thẳng đứng, Filter 2 tìm đường chéo, Filter 3 tìm góc vuông, Filter 4 tìm vùng màu đỏ. Việc tạo ra nhiều out_channels giúp mạng lưới học được đồng thời rất nhiều đặc trưng khác nhau của ảnh.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>
Áp dụng công thức: $W_{out} = \lfloor\frac{W_{in} + 2P - K}{S}\rfloor + 1$
$W_{out} = \lfloor\frac{128 + 2(2) - 5}{3}\rfloor + 1 = \lfloor\frac{127}{3}\rfloor + 1 = 42 + 1 = 43$.
Vậy kích thước đầu ra là 43x43.

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

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

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>

<details><summary><b>T-1 — Transfer</b></summary>

```python
import torch
import torch.nn as nn

x = torch.randn(32, 16, 8, 8)
flatten = nn.Flatten()
out = flatten(x)
print(out.shape) # (32, 1024)

```

**Lỗi thường gặp:** fit preprocessing/chọn threshold trên test, dùng metric sai hoặc bỏ qua failure mode.

</details>

<details><summary><b>O-1 — Olympiad</b></summary>

Đáp án là một quy trình: baseline sớm, validation chống leakage, lưu seed/config, theo dõi metric và dành thời gian tái chạy artifact cuối. Chi tiết phụ thuộc profile kỳ thi; xem `olympiad_transfer.md`.

**Lỗi thường gặp:** áp luật của kỳ thi khác, không lưu config/artifact hoặc hết timebox mà chưa chạy infer cuối.

</details>
