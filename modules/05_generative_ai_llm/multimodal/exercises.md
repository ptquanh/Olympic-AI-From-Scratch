# Bài tập: Multimodal VLM

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

1. Trong kiến trúc LLaVA, phần nào của mạng Neural thường được "đóng băng" (freeze) trong quá trình fine-tuning?
2. Tại sao ta không ghép trực tiếp đầu ra của CNN vào LLM mà cần qua một lớp Projection?
3. Nếu bạn đưa một tấm ảnh 1920x1080 chứa rất nhiều văn bản nhỏ li ti vào CLIP (ViT-B/32), tại sao mô hình thường không đọc được chữ?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

1. Mở `lab.ipynb`. Tải một bức ảnh từ internet bằng Python (sử dụng thư viện `requests` và `PIL`).
2. Khởi tạo pipeline `visual-question-answering`. Truyền bức ảnh vừa tải và một câu hỏi liên quan. In ra câu trả lời của mô hình.

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

1. Thử thay đổi các câu hỏi từ dễ đến khó (Ví dụ: "Có màu gì?", "Có bao nhiêu người?", "Họ đang cảm thấy thế nào?"). Ghi nhận xem mô hình VQA gặp khó khăn ở loại câu hỏi nào nhất (Đếm số lượng, suy luận logic, hay nhận diện màu sắc?).

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
