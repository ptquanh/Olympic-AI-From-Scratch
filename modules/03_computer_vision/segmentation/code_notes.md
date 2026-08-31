# Code Notes: Image Segmentation

## 🔑 Core Patterns

```python
# Cấu trúc Encoder-Decoder thường dùng UpSampling2D hoặc ConvTranspose2d

```

## 📋 API Cheat Sheet

| smp | `smp.Unet(encoder_name='resnet34')` | [Segmentation Models Pytorch](https://github.com/qubvel/segmentation_models.pytorch) |

## 🏋️ Bài Luyện Code Tay

1. Cài Dice score với epsilon và test mask rỗng.
2. Resize mask bằng nearest-neighbor; assert tập label không đổi.

## 🧠 Flashcards

| Semantic vs Instance Segmentation? | Semantic: Gom tất cả con chó thành 1 màu. Instance: Mỗi con chó 1 màu riêng biệt. |
