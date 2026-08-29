# Code Notes: Data Augmentation

## 🔑 Core Patterns

```python
import torchvision.transforms as T
transform = T.Compose([T.RandomHorizontalFlip(p=0.5), T.ColorJitter(brightness=0.2)])
```

## 📋 API Cheat Sheet

| torchvision.transforms | `T.Compose` | [Docs](https://pytorch.org/vision/stable/transforms.html) |

## 🧠 Flashcards

| Có nên Augment tập Test không? | KHÔNG. Trừ khi dùng kỹ thuật TTA (Test Time Augmentation). |
