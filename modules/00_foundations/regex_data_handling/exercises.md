# Exercises: Regex & Data Handling

## Tầng 1: Understand

**1. Giải thích ý nghĩa của biểu thức Regex sau:**
`r'^[A-Z][a-z]+ \d{2,4}$'`
(Gợi ý: Nó khớp với chuỗi "Hanoi 2024" nhưng không khớp với "hanoi 24" hay "Hanoi 2024").

**2. Điểm khác biệt mấu chốt:**
Cho biết kết quả của hai dòng code sau khác nhau như thế nào?

- `Path('data').glob('*.json')`
- `Path('data').glob('**/*.json')`

## Tầng 2: Implement

**1. Chuẩn hóa ngày tháng**
Đoạn text chứa ngày tháng định dạng lộn xộn: `"Sinh nhật: 12-05-2000, Ngày thi: 01/11/2026, Hết hạn: 2026.12.31"`
Hãy viết một function dùng regex để chuyển tất cả về định dạng `DD/MM/YYYY`.

_Kỳ vọng:_ `"Sinh nhật: 12/05/2000, Ngày thi: 01/11/2026, Hết hạn: 31/12/2026"`

**2. File Parser**
Viết script dùng `pathlib` tìm tất cả các file có đuôi `.log` trong thư mục `./logs/`, đọc nội dung, tìm tất cả các dòng chứa từ khóa `[ERROR]`, và ghi các dòng đó ra một file mới tên `errors_summary.txt`.

## Tầng 3: Experiment

**Regex Performance Benchmarking**

1. Tạo một string rất dài bằng cách lặp lại chữ 'a' 1 triệu lần, kết thúc bằng 'b': `text = 'a' * 1000000 + 'b'`
2. Thử match bằng pattern `r'a*b'` và `r'a+b'`. Đo thời gian chạy bằng `time.time()`.
3. Thử pattern sai `r'a*c'`. Chuyện gì xảy ra với thời gian chạy? Giải thích hiện tượng "Catastrophic Backtracking".
