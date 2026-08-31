# Exercises: Regex & Data Handling

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Giải thích ý nghĩa của biểu thức Regex sau:**

`r'^[A-Z][a-z]+ \d{2,4}$'`
(Gợi ý: Nó khớp với chuỗi "Hanoi 2024" nhưng không khớp với "hanoi 24" hay "Hanoi 2024").

**2. Điểm khác biệt mấu chốt:**
Cho biết kết quả của hai dòng code sau khác nhau như thế nào?

- `Path('data').glob('*.json')`
- `Path('data').glob('**/*.json')`

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Chuẩn hóa ngày tháng**
Đoạn text chứa ngày tháng định dạng lộn xộn: `"Sinh nhật: 12-05-2000, Ngày thi: 01/11/2026, Hết hạn: 2026.12.31"`
Hãy viết một function dùng regex để chuyển tất cả về định dạng `DD/MM/YYYY`.

_Kỳ vọng:_ `"Sinh nhật: 12/05/2000, Ngày thi: 01/11/2026, Hết hạn: 31/12/2026"`

**2. File Parser**

_Chạy đoạn code sau để tạo dữ liệu giả lập (mock data):_

```python
from pathlib import Path
import random

log_dir = Path('./logs')
log_dir.mkdir(exist_ok=True)

for i in range(3):
    with (log_dir / f'server_{i}.log').open('w', encoding='utf-8') as f:
        f.write(f"INFO: Server {i} started\n")
        if random.choice([True, False]):
            f.write(f"[ERROR] Failed to connect to DB on server {i}\n")
        f.write("INFO: Processing data...\n")
        if random.choice([True, False]):
            f.write(f"[ERROR] Timeout on server {i}\n")
print("Đã tạo xong file log sample!")

```

**Yêu cầu:** Viết script dùng `pathlib` tìm tất cả các file có đuôi `.log` trong thư mục `./logs/`, đọc nội dung, tìm tất cả các dòng chứa từ khóa `[ERROR]`, và ghi các dòng đó ra một file mới tên `errors_summary.txt`.

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**Regex Performance Benchmarking**

1. Tạo một string rất dài bằng cách lặp lại chữ 'a' 1 triệu lần, kết thúc bằng 'b': `text = 'a' * 1000000 + 'b'`
2. Thử match bằng pattern `r'a*b'` và `r'a+b'`. Đo thời gian chạy bằng `time.time()`.
3. Thử pattern sai `r'a*c'`. Chuyện gì xảy ra với thời gian chạy? Giải thích hiện tượng "Catastrophic Backtracking".

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
