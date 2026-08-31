# Code Notes: Speech Recognition

> ⚠️ **Online/optional appendix:** một số snippet bên dưới cần package hoặc model cache bổ sung và có thể tải dữ liệu ở lần chạy đầu. Chúng không competition-safe nếu profile chính thức không cho phép rõ ràng. Notebook chính của chương luôn có đường chạy fast/offline và không tự cài/tải.

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

## 📋 API Cheat Sheet

| API                    | Dùng khi                           |
| ---------------------- | ---------------------------------- |
| `torchaudio.load`      | waveform input in learning profile |
| `torch.nn.CTCLoss`     | CTC alignment loss                 |
| `custom edit_distance` | offline WER/CER                    |

### 🧠 Flashcards

| Hỏi                             | Trả lời                                                                                              |
| ------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Kiến trúc của Whisper là gì?    | Là mô hình Sequence-to-Sequence (Encoder-Decoder) dựa trên Transformer.                              |
| WER tính toán dựa trên điều gì? | Số lỗi Thêm (Insertions), Xóa (Deletions), Thay thế (Substitutions) chia cho tổng số từ của câu gốc. |
