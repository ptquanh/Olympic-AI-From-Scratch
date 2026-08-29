# Bài tập: Speech Recognition

## Tầng 1: Understand

Thử tự tính tay WER: Nhãn gốc "mẹ đi chợ mua rau". Mô hình dự đoán "mẹ đi chợ rau". Có sự thay đổi gì? Tính WER.

## Tầng 2: Implement

**Mục tiêu:** Sử dụng HuggingFace Pipeline.

- Dùng model `openai/whisper-tiny`.
- Load một đoạn ghi âm ngắn (< 10s) tiếng Anh và in ra văn bản.

## Tầng 3: Experiment

**Mục tiêu:** Đánh giá lỗi (WER).

- Ghi âm chính giọng bạn đọc một câu tiếng Anh khó.
- Chạy Whisper để nhận diện.
- Tự viết hàm tính WER (hoặc dùng `jiwer`) giữa kết quả của máy và câu bạn thực sự đọc.
