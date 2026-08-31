# Code Notes: CNN Architectures

> ⚠️ **Online/optional appendix:** một số snippet bên dưới cần package hoặc model cache bổ sung và có thể tải dữ liệu ở lần chạy đầu. Chúng không competition-safe nếu profile chính thức không cho phép rõ ràng. Notebook chính của chương luôn có đường chạy fast/offline và không tự cài/tải.

## 🔑 Core Patterns

```python
import torchvision.models as models
model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)

```

## 📋 API Cheat Sheet

| timm | `timm.create_model('resnet18', pretrained=True)` | [Docs](https://huggingface.co/docs/timm) |

## 🏋️ Bài Luyện Code Tay

1. Tính output shape và parameter count của một conv block trước khi chạy code.
2. Viết residual block tối thiểu và test cả trường hợp đổi số channel.

## 🧠 Flashcards

| Mạng nào mở đầu cho xu hướng xếp chồng Conv 3x3 thay vì dùng Conv lớn? | VGG. |
