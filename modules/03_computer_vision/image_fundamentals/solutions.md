# Lời giải: Image Fundamentals

<details><summary><b>Tầng 1: Understand</b></summary>
Chuẩn hóa giúp đưa dữ liệu về khoảng [0, 1], tránh hiện tượng giá trị pixel quá lớn làm nổ (exploding) gradient lúc tính toán Neural Network.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
img_rgb = img[:, :, ::-1]
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

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

</details>
