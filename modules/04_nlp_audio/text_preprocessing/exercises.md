# Bài tập: Text Preprocessing

## Tầng 1: Understand

**1. Tại sao dùng Subword?**
Kể tên 1 điểm yếu chết người của Word-level tokenization (Cắt theo khoảng trắng) và 1 điểm yếu của Character-level tokenization (Cắt từng chữ cái a, b, c).

## Tầng 2: Implement

**1. Code thử BPE**
Cài đặt thư viện `transformers`. Load `AutoTokenizer` của `bert-base-uncased` và `roberta-base`. Encode từ "unhappiness". Quan sát mảng tokens trả về của hai tokenizer này có giống nhau không?

## Tầng 3: Experiment

**1. Khảo sát special tokens**
Dùng `AutoTokenizer` của `bert-base-uncased` để encode câu "Hello world".
Sau đó dùng `tokenizer.decode()` để dịch ngược cái `input_ids` lại thành chữ. Bạn thấy có những ký tự kỳ lạ nào tự động xuất hiện ở đầu và cuối câu? Chúng có ý nghĩa gì?
