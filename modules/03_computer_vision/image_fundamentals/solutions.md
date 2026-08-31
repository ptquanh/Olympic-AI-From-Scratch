# Lời giải: Image Fundamentals

<details><summary><b>U-1 — Understand</b></summary>
Chuẩn hóa giúp đưa dữ liệu về khoảng [0, 1], tránh hiện tượng giá trị pixel quá lớn làm nổ (exploding) gradient lúc tính toán Neural Network.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

```python
img_rgb = img[:, :, ::-1]

```

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

```python
import cv2
from matplotlib import pyplot as plt

img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
hue_channel = img_hsv[:, :, 0]

plt.imshow(hue_channel, cmap='gray')
plt.title("Hue Channel")
plt.show()

```

Kênh H (Hue - Sắc độ) thể hiện bản chất của màu (đỏ, vàng, lục, lam) thay vì độ sáng. Ở những vùng có cùng một loại màu, giá trị H sẽ gần nhau.

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>
