# Code Notes: Document AI

> ⚠️ **Online/optional appendix:** một số snippet bên dưới cần package hoặc model cache bổ sung và có thể tải dữ liệu ở lần chạy đầu. Chúng không competition-safe nếu profile chính thức không cho phép rõ ràng. Notebook chính của chương luôn có đường chạy fast/offline và không tự cài/tải.

## 🔑 Core Patterns

### Pattern 1: OCR Cơ bản với EasyOCR

```python
import easyocr
# Khởi tạo reader hỗ trợ tiếng Việt và tiếng Anh (Có thể sẽ tải model nếu chạy lần đầu)
reader = easyocr.Reader(['vi', 'en'])

# Kết quả là một list các tuples: (bounding_box, text, độ_tự_tin)
result = reader.readtext('hoa_don.jpg')

for bbox, text, prob in result:
    print(f"[{prob:.2f}] {text}")

```

### 🏋️ Bài Luyện Code Tay

| #   | Bài                                                             | Thời gian | Hint (ẩn)                                                |
| --- | --------------------------------------------------------------- | --------- | -------------------------------------------------------- |
| 1   | Viết pipeline load ảnh và trích xuất chữ bằng Tesseract/EasyOCR | 15p       | Dùng `easyocr.Reader` hoặc `pytesseract.image_to_string` |
| 2   | Khởi tạo LayoutLM Processor để tokenize text và bounding boxes  | 20p       | Cần cả PIL Image và list text/boxes                      |

## 📋 API Cheat Sheet

| API             | Dùng khi                              |
| --------------- | ------------------------------------- |
| `numpy.asarray` | token/box arrays                      |
| `torch.clamp`   | bound normalized coordinates          |
| `OCR engine`    | optional online/learning profile only |

### 🧠 Flashcards

| Hỏi                                                | Trả lời                                                                        |
| -------------------------------------------------- | ------------------------------------------------------------------------------ |
| Điểm đột phá của LayoutLM so với BERT thuần là gì? | LayoutLM đưa thêm tọa độ (bounding boxes) và thông tin hình ảnh vào embedding. |
| OCR thường gặp khó khăn gì?                        | Chữ viết tay, nhiễu nền, và văn bản cong (curved text).                        |
