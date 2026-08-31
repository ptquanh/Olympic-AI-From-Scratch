# Regex & Data Handling

> **Thời gian học ước tính:** 3 giờ (theory: 1h, code: 1h, exercises: 1h)
> **Loại:** Concept Lesson
> **Track:** Foundation ⭐ | Contest ⭐

## Prerequisite Check

Trước khi bắt đầu, bạn cần trả lời được:

1. Cấu trúc dữ liệu List và Dictionary trong Python khác biệt cơ bản nhất ở điểm nào?
2. Làm sao để duyệt qua một list và lấy được cả vị trí (index) lẫn giá trị của phần tử?

Nếu chưa → quay lại chương `python_essentials`.

## Learning Outcomes

Sau chương này, bạn sẽ có thể:

- [ ] Viết regex pattern để extract email, số điện thoại, pattern từ text
- [ ] Dùng `re.findall()`, `re.sub()`, `re.search()`, `re.compile()` thành thạo
- [ ] Đọc file CSV/JSON bằng stdlib (`csv`, `json`)
- [ ] Navigate filesystem bằng `pathlib`, `glob`, `os`
- [ ] Biết khi nào dùng regex vs string methods

## Concept Map

```text
[NumPy & Pandas] --> [CHƯƠNG NÀY] --> [Math Essentials]
                          │
                          ├── dùng trong [Text Preprocessing]
                          └── nền tảng cho [Data Loading Pipeline]

```

## 1. Intuition — Tại Sao Cần Regex & Pathlib?

Giả sử bạn đang tham gia một kỳ thi Olympic AI, ban tổ chức cung cấp bộ dữ liệu gồm 10,000 file text rải rác trong nhiều thư mục con. Bạn cần đọc từng file, tìm các đoạn văn bản có chứa số căn cước công dân (12 chữ số) và che chúng đi trước khi train mô hình.

- **String methods (`.replace()`, `.find()`)**: Không thể tìm được "bất kỳ 12 chữ số nào", chúng chỉ tìm được chuỗi chính xác.
- **Duyệt file thủ công**: Quá chậm, dễ thiếu sót.

Đây là lúc bạn cần **Regex (Regular Expressions)** để xử lý văn bản phức tạp, và **`pathlib` / `glob`** để xử lý hàng vạn file một cách tự động. Các công cụ này là "vũ khí sinh tồn" trong bất kỳ bài toán AI thực tế nào.

## 2. Regex (Biểu thức chính quy)

Regex là một chuỗi ký tự dùng để mô tả một _mẫu_ tìm kiếm. Python hỗ trợ regex qua thư viện `re`.

### Các Metacharacter thường dùng:

- `.` : Khớp với bất kỳ ký tự nào (trừ dấu xuống dòng)
- `^` : Bắt đầu chuỗi
- `$` : Kết thúc chuỗi
- `\d`: Ký tự số (0-9)
- `\w`: Ký tự chữ, số, dấu gạch dưới (a-z, A-Z, 0-9, \_)
- `\s`: Ký tự khoảng trắng (space, tab, newline)

### Quantifiers (Số lượng):

- `*`: 0 hoặc nhiều lần
- `+`: 1 hoặc nhiều lần
- `?`: 0 hoặc 1 lần
- `{n}`: Chính xác n lần

## 3. File System & File I/O

Trong Python, thư viện `pathlib` là cách hiện đại và chuẩn nhất để xử lý đường dẫn file thay vì dùng `os.path`. Kế hợp với `glob`, ta có thể tìm kiếm file rất nhanh.

Đối với file data (như JSON, CSV), Python có sẵn thư viện chuẩn (stdlib) nhẹ và đủ dùng trước khi phải gọi đến "hạng nặng" là Pandas.

## 4. Worked Example: Trích xuất Email

Giả sử ta có đoạn text: `"Liên hệ support@olpai.vn hoặc admin-team_2026@gmail.com để biết thêm chi tiết."`

Ta cần lấy ra danh sách các email.

```python
import re

text = "Liên hệ support@olpai.vn hoặc admin-team_2026@gmail.com để biết thêm chi tiết."
# Phân tích pattern:
# [a-zA-Z0-9._%-]+ : Tên email (có thể chứa chữ, số, dấu chấm, gạch dưới, gạch ngang)
# @                : Bắt buộc có còng
# [a-zA-Z0-9.-]+   : Tên miền
# \.               : Dấu chấm
# [a-zA-Z]{2,}     : Đuôi tên miền (ít nhất 2 chữ, vd: vn, com)

pattern = r'[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)
print(emails)
# Output: ['support@olpai.vn', 'admin-team_2026@gmail.com']

```

## 5. Common Mistakes & Misconceptions

> ❌ **Sai:** Dùng regex để parse toàn bộ HTML/XML lồng nhau.
> ✅ **Đúng:** Dùng parser phù hợp trong môi trường học. `BeautifulSoup` không thuộc danh sách PTIT 2026 trong PDF, vì vậy không giả định có trong competition profile.

> ❌ **Sai:** Dùng `re.match()` để tìm kiếm chuỗi ở giữa văn bản.
> ✅ **Đúng:** `re.match()` chỉ kiểm tra ở **đầu** chuỗi. Phải dùng `re.search()` nếu muốn tìm ở bất kỳ đâu, hoặc `re.findall()` để tìm tất cả.

> ❌ **Sai:** Thường xuyên dùng `os.path.join(path1, path2)`.
> ✅ **Đúng:** Nên dùng `pathlib.Path(path1) / path2`. Cú pháp ngắn gọn, hướng đối tượng và hoạt động đa nền tảng.

## ⑯ Time Estimate

Theory: ~1.5h · Code: ~1.5h · Exercises: ~1h
