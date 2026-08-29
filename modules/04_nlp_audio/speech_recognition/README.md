# Speech Recognition (ASR)

> **Track:** Foundation ⚡ | Contest 📖

## ① Giới thiệu

Biến giọng nói thành văn bản (Speech-to-Text). Các mô hình như OpenAI Whisper hay Qwen Audio hiện tại đạt độ chính xác vô tiền khoáng hậu.

## ② Learning Outcomes

- Nắm được cách ứng dụng pre-trained ASR models.
- Tính toán Metric WER (Word Error Rate).

## ⑤ Math/Derivation

WER = (S + D + I) / N
Trong đó $S$ là từ thay thế sai, $D$ là từ bị bỏ sót, $I$ là từ chèn thừa, và $N$ là tổng số từ của nhãn gốc. Giá trị WER càng nhỏ càng tốt.

## ⑯ Time Estimate

Theory: ~0.5h, Code: ~0.5h, Exercises: ~0.5h
