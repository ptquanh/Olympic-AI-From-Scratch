# Bài tập: Text Preprocessing

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Tại sao dùng Subword?**
Kể tên 1 điểm yếu chết người của Word-level tokenization (Cắt theo khoảng trắng) và 1 điểm yếu của Character-level tokenization (Cắt từng chữ cái a, b, c).

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Code thử BPE**
Cài đặt thư viện `transformers`. Load `AutoTokenizer` của `bert-base-uncased` và `roberta-base`. Encode từ "unhappiness". Quan sát mảng tokens trả về của hai tokenizer này có giống nhau không?

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Khảo sát special tokens**
Dùng `AutoTokenizer` của `bert-base-uncased` để encode câu "Hello world".
Sau đó dùng `tokenizer.decode()` để dịch ngược cái `input_ids` lại thành chữ. Bạn thấy có những ký tự kỳ lạ nào tự động xuất hiện ở đầu và cuối câu? Chúng có ý nghĩa gì?

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
