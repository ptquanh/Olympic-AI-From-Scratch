# Code Notes: Image Fundamentals

## 🔑 Core Patterns

```python
import cv2
img = cv2.imread('img.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

```

## 📋 API Cheat Sheet

| PIL | `Image.open()` | [Docs](https://pillow.readthedocs.io/) |

## 🏋️ Bài Luyện Code Tay

1. Đổi HWC↔CHW và assert round-trip.
2. Chuẩn hóa uint8 sang float rồi khôi phục với sai số lượng tử cho phép.

## 🧠 Flashcards

| OpenCV đọc ảnh hệ màu gì? | BGR |
