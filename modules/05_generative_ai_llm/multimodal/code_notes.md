# Code Notes: Multimodal VLM

> ⚠️ **Online/optional appendix:** một số snippet bên dưới cần package hoặc model cache bổ sung và có thể tải dữ liệu ở lần chạy đầu. Chúng không competition-safe nếu profile chính thức không cho phép rõ ràng. Notebook chính của chương luôn có đường chạy fast/offline và không tự cài/tải.

## 🔑 Core Patterns

### Pattern 1: Load và gọi mô hình VLM (HuggingFace)

```python
# Mô tả: Dùng HuggingFace pipeline cho Image-to-Text / VQA
# Khi nào dùng: Khi cần xử lý ảnh + text nhanh chóng
from transformers import pipeline
from PIL import Image

# Bài toán Image Captioning (Sinh mô tả ảnh)
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
img = Image.open("cat.jpg")
print(captioner(img))

# Bài toán VQA (Hỏi đáp trên ảnh)
vqa_pipeline = pipeline("visual-question-answering", model="dandelin/vilt-b32-finetuned-vqa")
print(vqa_pipeline(image=img, question="What is the cat sitting on?"))

```

**Ghi nhớ:** Bài toán VQA yêu cầu cả `image` và `question`.

## 📋 API Cheat Sheet

| Việc cần làm  | Code                                                 | Link Docs                                                                          |
| ------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Image to text | `pipeline("image-to-text", model="...")`             | [HF Pipeline](https://huggingface.co/docs/transformers/main_classes/pipelines)     |
| Visual QA     | `pipeline("visual-question-answering", model="...")` | [HF VQA](https://huggingface.co/docs/transformers/tasks/visual_question_answering) |

## 🏋️ Bài Luyện Code Tay

**Quy tắc:** Đóng tài liệu. Mở notebook trống. Hẹn giờ.

| #   | Bài                                                                               | Thời gian | Hint (ẩn)                                   |
| --- | --------------------------------------------------------------------------------- | --------- | ------------------------------------------- |
| 1   | Viết đoạn code load một ảnh bằng PIL và dùng pipeline sinh mô tả (image-to-text). | 5 phút    | `Image.open()`, `pipeline("image-to-text")` |

## 🧠 Flashcards

| Hỏi                              | Trả lời                                                  |
| -------------------------------- | -------------------------------------------------------- |
| 3 thành phần chính của VLM?      | Vision Encoder, Text Decoder (LLM), và Projection Layer. |
| Projection layer có tác dụng gì? | Đồng bộ không gian vector giữa Ảnh và Text.              |
| VQA là viết tắt của gì?          | Visual Question Answering (Hỏi đáp trực quan).           |
