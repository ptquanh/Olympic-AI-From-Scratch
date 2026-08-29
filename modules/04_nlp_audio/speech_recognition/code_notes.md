# Code Notes: Speech Recognition

## 🔑 Core Patterns

```python
import jiwer
truth = "tôi đi học"
hypothesis = "tôi đi chơi"
error = jiwer.wer(truth, hypothesis)
print(error) # 0.33 (1 từ sai trên 3 từ)
```

### 🏋️ Bài Luyện Code Tay

| #   | Bài                                                     | Thời gian | Hint (ẩn)                                                                    |
| --- | ------------------------------------------------------- | --------- | ---------------------------------------------------------------------------- |
| 1   | Khởi tạo pipeline Whisper của HuggingFace để transcribe | 15p       | Dùng `pipeline("automatic-speech-recognition", model="openai/whisper-tiny")` |
| 2   | Viết code tính WER (Word Error Rate) giữa 2 câu         | 15p       | Dùng thư viện `jiwer`                                                        |

### 🧠 Flashcards

| Hỏi                             | Trả lời                                                                                              |
| ------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Kiến trúc của Whisper là gì?    | Là mô hình Sequence-to-Sequence (Encoder-Decoder) dựa trên Transformer.                              |
| WER tính toán dựa trên điều gì? | Số lỗi Thêm (Insertions), Xóa (Deletions), Thay thế (Substitutions) chia cho tổng số từ của câu gốc. |
