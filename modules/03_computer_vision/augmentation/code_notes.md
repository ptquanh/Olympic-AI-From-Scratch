# Code Notes: Data Augmentation

## 🔑 Core Patterns

```python
import torchvision.transforms as T
transform = T.Compose([T.RandomHorizontalFlip(p=0.5), T.ColorJitter(brightness=0.2)])

```

## 📋 API Cheat Sheet

| torchvision.transforms | `T.Compose` | [Docs](https://pytorch.org/vision/stable/transforms.html) |

## 🏋️ Bài Luyện Code Tay

1. Viết horizontal flip bằng NumPy và assert flip hai lần trả ảnh gốc.
2. Áp cùng geometric transform lên ảnh và mask; assert shape/nhãn vẫn khớp.

## 🧠 Flashcards

| Có nên Augment tập Test không? | KHÔNG. Trừ khi dùng kỹ thuật TTA (Test Time Augmentation). |
