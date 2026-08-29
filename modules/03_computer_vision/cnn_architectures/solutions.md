# Lời giải: Cnn Architectures

<details><summary><b>Tầng 1: Understand</b></summary>
import torch.nn as nn
model = models.resnet18()
for p in model.parameters():
    p.requires_grad = False
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
import torchvision.models as models
import torch.nn as nn

model = models.resnet18()
for p in model.parameters():
    p.requires_grad = False
model.fc = nn.Linear(512, 5)
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

```python
import torchvision.models as models

mobilenet = models.mobilenet_v2()
total_params = sum(p.numel() for p in mobilenet.parameters())
print(f"MobileNetV2 params: {total_params / 1e6:.2f} M")
```

MobileNetV2 chỉ có khoảng 3.5 triệu tham số, bằng chưa tới 1/3 so với ResNet18 nhưng độ chính xác lại rất đáng gờm nhờ kỹ thuật Depthwise Separable Convolution.

</details>
