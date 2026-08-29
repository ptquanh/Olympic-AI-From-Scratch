# Postmortem: Text Classification

## 1. Bài học kinh nghiệm (What went right/wrong)

- **OOM (Out Of Memory):** Bạn có bị văng lỗi CUDA OOM không? Nếu có, có lẽ `max_length` của bạn quá lớn (ví dụ 512) hoặc `batch_size` quá to. Mẹo trong NLP là thường giữ `max_length` ở 128 hoặc 256. Rất ít văn bản (hoặc phần quan trọng của nó) dài hơn mức đó.
- **Learning Rate quá to:** Nếu bạn dùng `lr = 0.01` hay `0.001` (giống như ở các mô hình CNN/MLP cũ), mô hình BERT của bạn sẽ bị "Catastrophic Forgetting" - mất hoàn toàn kiến thức pre-trained và Loss sẽ ghim ở một mức không giảm. Với Transformer fine-tuning, Learning rate BẮT BUỘC phải nằm trong khoảng $1e-5$ đến $5e-5$.

## 2. Các điểm mù (Blind spots)

- **Padding token:** Trong quá trình infer (dự đoán), việc padding token bằng 0 là chuẩn. Tuy nhiên nếu quên đẩy `attention_mask` vào model, BERT sẽ tự coi phần padding token đó là những từ "hợp lệ" và cố gắng phân tích, dẫn đến kết quả sai lệch.
- **Tiếng Việt:** Tokenizer của BERT Tiếng Anh không biết cắt từ Tiếng Việt (nó sẽ cắt vụn ra thành các chữ cái). Luôn dùng `vinai/phobert-base` cho Tiếng Việt.

## 3. Cải tiến tiếp theo

- Dùng kỹ thuật Freezing: Đóng băng 6 lớp Encoder đầu tiên của BERT, chỉ huấn luyện 6 lớp cuối để tăng tốc và tránh Overfitting.
- Dùng LoRA / PEFT để fine-tune tiết kiệm RAM (rất hay dùng cho LLM hiện nay).
