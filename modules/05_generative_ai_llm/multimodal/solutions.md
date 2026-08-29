# Lời giải: Multimodal (VQA)

<details><summary><b>Tầng 1: Understand</b></summary>

1. Vision Encoder (như CLIP) thường được đóng băng để giữ nguyên khả năng trích xuất đặc trưng ảnh chung đã học được từ dữ liệu khổng lồ.
2. Không thể ghép trực tiếp vì đầu ra của CNN là vector trong "không gian hình ảnh", trong khi LLM chỉ hiểu vector trong "không gian văn bản" (text embeddings). Projection layer đóng vai trò như một thông dịch viên.
3. ViT-B/32 chia ảnh thành các patch $32\times32$. Nếu resize ảnh 1920x1080 xuống $224\times224$, các chữ cái nhỏ sẽ bị mờ đi và biến mất hoàn toàn. Các patch sẽ không chứa thông tin đọc được.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

1. Tải ảnh bằng `PIL`:

```python
from PIL import Image
import requests
url = "..."
image = Image.open(requests.get(url, stream=True).raw)
```

2. Gọi pipeline VQA:

```python
from transformers import pipeline
vqa = pipeline("visual-question-answering", model="dandelin/vilt-b32-finetuned-vqa")
print(vqa(image=image, question="What color is the car?"))
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

1. Các mô hình VQA cơ bản (như ViLT) thường làm tốt ở việc nhận diện màu sắc, đối tượng lớn. Nhưng chúng cực kỳ kém ở bài toán **đếm số lượng** (counting) hoặc **đọc chữ** (OCR), do hạn chế của Vision Encoder và cách gán patch. Chúng cũng gặp khó trong việc suy luận logic phức tạp (Ví dụ: "Tại sao người đàn ông lại khóc?").

</details>
