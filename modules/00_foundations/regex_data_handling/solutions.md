# Lời giải: Regex & Data Handling

<details><summary><b>Tầng 1: Understand</b></summary>

**1. Giải thích ý nghĩa của biểu thức Regex `r'^[A-Z][a-z]+ \d{2,4}$'`**

- `^`: Đánh dấu bắt đầu chuỗi.
- `[A-Z]`: Ký tự đầu tiên phải là một chữ cái in hoa.
- `[a-z]+`: Theo sau là một hoặc nhiều chữ cái in thường.
- ` ` : Một khoảng trắng.
- `\d{2,4}`: Chứa từ 2 đến 4 chữ số liên tiếp.
- `$`: Đánh dấu kết thúc chuỗi.

=> Do đó, nó khớp với chuỗi "Hanoi 2024" nhưng không khớp "hanoi 24" (chữ h viết thường) hay "Hanoi 2" (chỉ có 1 chữ số).

**2. Điểm khác biệt mấu chốt:**

- `Path('data').glob('*.json')`: Chỉ tìm các file có đuôi `.json` nằm **trực tiếp** trong thư mục `data/` (không quét vào các thư mục con).
- `Path('data').glob('**/*.json')`: Tìm tất cả các file có đuôi `.json` nằm trong thư mục `data/` **và đệ quy toàn bộ các thư mục con** bên trong nó.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

**1. Chuẩn hóa ngày tháng**

```python
import re

text = "Sinh nhật: 12-05-2000, Ngày thi: 01/11/2026, Hết hạn: 2026.12.31"

def format_date(match):
    date_str = match.group()
    # Tách lấy các con số bằng \d+
    numbers = re.findall(r'\d+', date_str)

    # Nếu phần tử đầu tiên (năm) có 4 chữ số (format: YYYY.MM.DD)
    if len(numbers[0]) == 4:
        return f"{numbers[2]}/{numbers[1]}/{numbers[0]}"
    # Nếu phần tử cuối (năm) có 4 chữ số (format: DD-MM-YYYY hoặc DD/MM/YYYY)
    else:
        return f"{numbers[0]}/{numbers[1]}/{numbers[2]}"

# Regex tìm ngày tháng: 2-4 chữ số, dấu phân cách (-./), 2 chữ số, phân cách, 2-4 chữ số
pattern = r'\d{2,4}[-./]\d{2}[-./]\d{2,4}'
result = re.sub(pattern, format_date, text)

print(result)
# Output: Sinh nhật: 12/05/2000, Ngày thi: 01/11/2026, Hết hạn: 31/12/2026
```

**2. File Parser**

```python
from pathlib import Path

# Khai báo đường dẫn
log_dir = Path('./logs')
output_file = Path('errors_summary.txt')

# Tạo thư mục logs để test code không bị lỗi (nếu chưa có)
log_dir.mkdir(exist_ok=True)

# Mở file output để ghi kết quả
with output_file.open('w', encoding='utf-8') as f_out:
    # Duyệt qua các file .log
    for log_path in log_dir.glob('*.log'):
        with log_path.open('r', encoding='utf-8') as f_in:
            for line in f_in:
                # Nếu dòng có chứa [ERROR] thì ghi lại
                if '[ERROR]' in line:
                    f_out.write(line)
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

**Regex Performance Benchmarking**

```python
import re
import time

text = 'a' * 1000000 + 'b'

# 1. Đo thời gian r'a*b'
start = time.time()
re.match(r'a*b', text)
print(f"a*b time: {time.time() - start:.4f}s")

# 2. Đo thời gian r'a+b'
start = time.time()
re.match(r'a+b', text)
print(f"a+b time: {time.time() - start:.4f}s")
```

**Giải thích hiện tượng Catastrophic Backtracking (Quay lui thảm họa):**
Khi bạn chạy thử pattern không hợp lệ lên một chuỗi rất dài (ví dụ `re.match(r'(a+)+c', text)`), Regex engine sẽ cố gắng tìm chữ `c`.
Nó sẽ lấy toàn bộ chữ `a`, tìm `c` -> không thấy. Nó lùi lại nhả ra 1 chữ `a`, rồi tổ hợp lại thành 2 nhóm `(a+)` và tiếp tục tìm `c` -> không thấy. Quá trình chia nhóm chữ `a` này diễn ra theo cấp số nhân (độ phức tạp $O(2^N)$). Với 1 triệu chữ `a`, thời gian chạy sẽ lâu hơn cả tuổi thọ vũ trụ. Hiện tượng này làm treo hệ thống ngay lập tức!

</details>
