# Bài tập: Multimodal VLM

## Tầng 1: Understand

1. Trong kiến trúc LLaVA, phần nào của mạng Neural thường được "đóng băng" (freeze) trong quá trình fine-tuning?
2. Tại sao ta không ghép trực tiếp đầu ra của CNN vào LLM mà cần qua một lớp Projection?
3. Nếu bạn đưa một tấm ảnh 1920x1080 chứa rất nhiều văn bản nhỏ li ti vào CLIP (ViT-B/32), tại sao mô hình thường không đọc được chữ?

## Tầng 2: Implement

1. Mở `lab.ipynb`. Tải một bức ảnh từ internet bằng Python (sử dụng thư viện `requests` và `PIL`).
2. Khởi tạo pipeline `visual-question-answering`. Truyền bức ảnh vừa tải và một câu hỏi liên quan. In ra câu trả lời của mô hình.

## Tầng 3: Experiment

1. Thử thay đổi các câu hỏi từ dễ đến khó (Ví dụ: "Có màu gì?", "Có bao nhiêu người?", "Họ đang cảm thấy thế nào?"). Ghi nhận xem mô hình VQA gặp khó khăn ở loại câu hỏi nào nhất (Đếm số lượng, suy luận logic, hay nhận diện màu sắc?).
