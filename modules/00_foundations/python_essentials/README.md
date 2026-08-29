# Python Essentials

> **Thời gian học ước tính:** 3 giờ (theory: 1h, code: 1h, exercises: 1h)
> **Loại:** Concept Lesson
> **Track:** Foundation ⭐ | Contest ⏭️

## Prerequisite Check

Chương này dành cho người mới chuyển sang Python từ ngôn ngữ khác (C++, Java, Pascal) hoặc chưa nắm vững Python nâng cao.
Bạn có thể bỏ qua chương này nếu trả lời được:

1. List Comprehension là gì? Viết một ví dụ.
2. Từ khóa `yield` khác gì `return`?
3. Sự khác biệt giữa `__init__` và `__repr__` trong một Class?

Nếu chưa trả lời được → tiếp tục học chương này.

## Learning Outcomes

Sau chương này, bạn sẽ có thể:

- [ ] Viết list/dict comprehension thay vì dùng vòng lặp for nhiều dòng
- [ ] Định nghĩa hàm linh hoạt với `*args` và `**kwargs`
- [ ] Thiết kế và sử dụng Python Class cơ bản (OOP)
- [ ] Viết code an toàn với Try/Except/Finally
- [ ] Định nghĩa Generator để tiết kiệm RAM khi duyệt dữ liệu lớn

## Concept Map

```text
[Bắt đầu học AI] ──→ [CHƯƠNG NÀY] ──→ [Regex & Data Handling]
                             │
                             └── nền tảng cho [Mọi code AI sau này]
```

## 1. Intuition — Tại Sao Lại Phải Học Kỹ Python?

AI/Machine Learning hiện nay sử dụng Python làm ngôn ngữ thống trị. Lý do không phải vì Python chạy nhanh, mà vì Python có cú pháp cực kỳ dễ đọc (như tiếng Anh), giúp bạn dễ dàng biểu diễn các ý tưởng toán học phức tạp.

Tuy nhiên, nếu bạn viết code Python theo phong cách của C++ (dùng for loop khắp nơi, quản lý bộ nhớ thủ công), code của bạn sẽ vừa dài dòng, vừa chạy rất chậm. "Pythonic" là thuật ngữ chỉ việc viết code một cách tối ưu, tận dụng các tính năng đặc thù của Python.

## 2. Các Cấu Trúc Dữ Liệu Cốt Lõi

- **List (`[]`)**: Mảng thay đổi được. Có thể chứa hỗn hợp nhiều kiểu dữ liệu.
- **Tuple (`()`)**: Giống List, nhưng KHÔNG thay đổi được (Immutable). Rất nhẹ, dùng để làm key của Dictionary.
- **Dictionary (`{}`)**: Cấu trúc Key-Value. Truy xuất siêu nhanh $O(1)$.
- **Set (`{}`)**: Tập hợp các giá trị duy nhất (không trùng lặp). Phép toán giao/hợp/trừ siêu nhanh.

## 3. List Comprehension & Generator

Thay vì viết:

```python
squares = []
for i in range(10):
    if i % 2 == 0:
        squares.append(i**2)
```

Pythonic way (List Comprehension):

```python
squares = [i**2 for i in range(10) if i % 2 == 0]
```

**Generator (`yield`)**: Nếu bạn tạo list 1 triệu phần tử, máy tính có thể hết RAM. Generator dùng `yield` để trả về từng phần tử một mỗi khi được gọi, gần như không tốn RAM. Rất hay dùng khi đọc tập dữ liệu khổng lồ (Dataloader).

## 4. Object-Oriented Programming (OOP) Cực Ngắn

AI dùng OOP rất nhiều (vd: định nghĩa mô hình Neural Network, Dataset).

- `class`: Bản thiết kế.
- `__init__`: Hàm khởi tạo (Constructor). Chạy đầu tiên khi tạo object.
- `self`: Từ khóa đại diện cho chính object đó (giống `this` trong C++/Java).

## 5. Common Mistakes & Misconceptions

> ❌ **Sai:** Dùng `for i in range(len(my_list)):` để duyệt danh sách và lấy index.
> ✅ **Đúng:** Dùng `for i, item in enumerate(my_list):` để vừa lấy vị trí `i`, vừa lấy phần tử `item`.

> ❌ **Sai:** Gán biến list bằng toán tử `=`: `list2 = list1`. Khi đổi `list2`, `list1` cũng bị đổi (vì tham chiếu cùng vùng nhớ).
> ✅ **Đúng:** Dùng `list2 = list1.copy()` hoặc `list2 = list(list1)` để tạo bản sao mới.

> ❌ **Sai:** Để default argument là một list/dict trống trong hàm: `def add_item(item, lst=[]):`. Nó sẽ giữ lại giá trị của các lần gọi trước.
> ✅ **Đúng:** Đặt mặc định là `None`: `def add_item(item, lst=None): if lst is None: lst = []`.
