# Code Notes: Regex & Data Handling

## 🔑 Core Patterns (Phải nhớ)

### Pattern 1: Tìm tất cả kết quả với Regex

```python
import re
text = "Hóa đơn: 150000 VND, Tiền thừa: 5000 VND."
# Trích xuất số
numbers = re.findall(r'\d+', text) # ['150000', '5000']
```

**Ghi nhớ:** `findall` trả về list các chuỗi khớp. Dùng `r'...'` để viết regex (raw string) tránh lỗi escape `\`.

### Pattern 2: Thay thế với Regex

```python
text = "Giá   là    100    đô."
# Chuẩn hóa khoảng trắng
clean_text = re.sub(r'\s+', ' ', text) # "Giá là 100 đô."
```

**Ghi nhớ:** `sub` (substitute) thay thế phần khớp pattern bằng chuỗi mới.

### Pattern 3: Lấy danh sách file (Globbing)

```python
from pathlib import Path
# Tìm tất cả file .csv trong folder data và các folder con
csv_files = list(Path('data').glob('**/*.csv'))
```

**Ghi nhớ:** `glob('**/*.ext')` đệ quy tìm trong tất cả subdirectories.

### Pattern 4: Đọc JSON nhanh

```python
import json
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
```

**Ghi nhớ:** Luôn truyền `encoding='utf-8'` khi thao tác với text tiếng Việt.

## 📋 API Cheat Sheet

| Việc cần làm                         | Code                                  | Docs                                                         |
| ------------------------------------ | ------------------------------------- | ------------------------------------------------------------ |
| Compile regex (để tái sử dụng nhanh) | `regex = re.compile(r'\d+')`          | [link](https://docs.python.org/3/library/re.html#re.compile) |
| Lọc tên file, lấy đuôi               | `path.name`, `path.suffix`            | [link](https://docs.python.org/3/library/pathlib.html)       |
| Nối đường dẫn                        | `Path('folder') / 'file.txt'`         | [link](https://docs.python.org/3/library/pathlib.html)       |
| Đọc CSV thành list of dicts          | `list(csv.DictReader(open('f.csv')))` | [link](https://docs.python.org/3/library/csv.html)           |

## 🏋️ Bài Luyện Code Tay

**Quy tắc:** Đóng tất cả tài liệu. Mở notebook trống. Hẹn giờ.

| #   | Bài                                                                  | Thời gian | Hint (chỉ xem khi bí)                   |
| --- | -------------------------------------------------------------------- | --------- | --------------------------------------- |
| 1   | Viết regex tìm tất cả các thẻ `#hashtag` trong đoạn tweet            | 5 phút    | `r'#\w+'`                               |
| 2   | Liệt kê tất cả file `.jpg` trong thư mục hiện tại (không tìm đệ quy) | 5 phút    | `Path('.').glob('*.jpg')`               |
| 3   | Mở file json, sửa 1 field, lưu lại vào file json mới                 | 10 phút   | `json.load(f)` rồi `json.dump(data, f)` |

## 🧠 Flashcards (Hỏi → Trả lời)

| Hỏi                                            | Trả lời                                                     |
| ---------------------------------------------- | ----------------------------------------------------------- |
| `re.search()` trả về gì?                       | Trả về `Match` object đầu tiên tìm thấy, hoặc `None`        |
| Khác biệt giữa `*` và `+` trong regex?         | `*` là 0 hoặc nhiều lần. `+` là 1 hoặc nhiều lần.           |
| Tại sao nên dùng `pathlib` thay cho `os.path`? | Hướng đối tượng, dễ đọc, tự xử lý '/' vs '\' trên Win/Linux |
