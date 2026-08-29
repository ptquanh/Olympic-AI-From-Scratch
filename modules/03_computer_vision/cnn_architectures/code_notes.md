# Code Notes: CNN Architectures

## 🔑 Core Patterns

```python
import torchvision.models as models
model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
```

## 📋 API Cheat Sheet

| timm | `timm.create_model('resnet18', pretrained=True)` | [Docs](https://huggingface.co/docs/timm) |

## 🧠 Flashcards

| Mạng nào mở đầu cho xu hướng xếp chồng Conv 3x3 thay vì dùng Conv lớn? | VGG. |
