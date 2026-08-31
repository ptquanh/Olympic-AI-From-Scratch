# Code Notes: Generative CV

> ⚠️ **Online/optional appendix:** một số snippet bên dưới cần package hoặc model cache bổ sung và có thể tải dữ liệu ở lần chạy đầu. Chúng không competition-safe nếu profile chính thức không cho phép rõ ràng. Notebook chính của chương luôn có đường chạy fast/offline và không tự cài/tải.

## 🔑 Core Patterns

```python
# Thường sử dụng thư viện `diffusers` của HuggingFace

```

## 📋 API Cheat Sheet

| diffusers | `DiffusionPipeline.from_pretrained(...)` | [Diffusers](https://huggingface.co/docs/diffusers/) |

## 🏋️ Bài Luyện Code Tay

1. Cài forward diffusion `x_t` bằng NumPy với seed cố định.
2. Đo SNR theo timestep và giải thích khi ảnh mất tín hiệu.

## 🧠 Flashcards

| Mạng nào dùng cơ chế phá hủy ảnh bằng nhiễu (noise)? | Diffusion Models |
