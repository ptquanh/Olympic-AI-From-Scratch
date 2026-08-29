# Code Notes: Python Essentials

## 🔑 Core Patterns (Phải nhớ)

### Pattern 1: Tận dụng Enumerate và Zip

```python
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

# Duyệt lấy cả index
for i, name in enumerate(names):
    print(f"Top {i+1}: {name}")

# Kết hợp 2 list cùng lúc
for name, score in zip(names, scores):
    print(f"{name} được {score} điểm")
```

**Ghi nhớ:** Bỏ thói quen `range(len())`. Luôn dùng `enumerate` và `zip`.

### Pattern 2: Xử lý ngoại lệ (Try/Except)

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Lỗi chia cho 0:", e)
finally:
    print("Luôn chạy dù có lỗi hay không")
```

**Ghi nhớ:** Dùng để bắt các lỗi runtime (vd: không tìm thấy file, chia cho 0) để chương trình không bị crash ngang.

### Pattern 3: Hàm với `*args` và `**kwargs`

```python
def my_func(*args, **kwargs):
    print("Tham số không tên (tuple):", args)
    print("Tham số có tên (dict):", kwargs)

my_func(1, 2, 3, a='hello', b=True)
```

**Ghi nhớ:** Dùng khi không biết trước người dùng sẽ truyền vào bao nhiêu tham số.

### Pattern 4: Class PyTorch-style cơ bản

```python
class MyDataset:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

dataset = MyDataset([10, 20, 30])
print(len(dataset)) # Gọi __len__
print(dataset[1])   # Gọi __getitem__
```

**Ghi nhớ:** Các hàm có 2 dấu gạch dưới (Dunder methods) là các hàm đặc biệt, giúp Class của bạn tương tác với các toán tử Python có sẵn (`len()`, `[]`).

## 📋 API Cheat Sheet

| Việc cần làm           | Code                                             | Docs                                  |
| ---------------------- | ------------------------------------------------ | ------------------------------------- |
| Sort list in place     | `my_list.sort(reverse=True)`                     | Sửa trực tiếp list                    |
| Sort trả về list mới   | `new_list = sorted(my_list, key=lambda x: x[1])` | Có thể truyền hàm tuỳ chỉnh qua `key` |
| Ghép list thành string | `", ".join(['a', 'b', 'c'])`                     | Ra `'a, b, c'`                        |
| Tách string thành list | `"a,b,c".split(",")`                             | Ra `['a', 'b', 'c']`                  |

## 🏋️ Bài Luyện Code Tay

**Quy tắc:** Đóng tất cả tài liệu. Mở notebook trống. Hẹn giờ.

| #   | Bài                                                                                               | Thời gian | Hint (chỉ xem khi bí)                                       |
| --- | ------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------- |
| 1   | Cho list of dicts: `[{'id': 1, 'v': 5}, {'id': 2, 'v': 2}]`. Viết code sắp xếp theo `v` giảm dần. | 5 phút    | `sorted(lst, key=lambda x: x['v'], reverse=True)`           |
| 2   | Viết một Generator tên là `fibonacci(n)` để sinh ra `n` số Fibonacci đầu tiên. Dùng `yield`.      | 10 phút   | Tạo biến `a, b = 0, 1` rồi lặp và `yield a`, `a,b = b, a+b` |
| 3   | Viết List Comprehension để làm phẳng ma trận 2D: `[[1,2], [3,4]]` thành `[1, 2, 3, 4]`            | 5 phút    | `[x for row in matrix for x in row]`                        |

## 🧠 Flashcards (Hỏi → Trả lời)

| Hỏi                                                          | Trả lời                                                                                        |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| Dictionary truy xuất giá trị bằng key mất thời gian bao lâu? | O(1) - siêu nhanh nhờ Hash table.                                                              |
| Phân biệt `append()` và `extend()` của List?                 | `append` thêm cả 1 object vào đuôi. `extend` phá vỡ list/iterable thêm vào, thêm từng phần tử. |
| Biến `self` trong Class là gì?                               | Đại diện cho chính object/instance hiện tại đang gọi hàm đó.                                   |
