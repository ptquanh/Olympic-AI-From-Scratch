# Exercises: Python Essentials

## Tầng 1: Understand

**1. Mutable vs Immutable**
Trong Python, `List` là mutable (có thể thay đổi), còn `Tuple` và `String` là immutable (không thể thay đổi).
Chuyện gì sẽ xảy ra nếu bạn cố gắng gán `my_string[0] = 'a'`?
Việc Tuple immutable mang lại lợi ích gì về mặt tốc độ và bộ nhớ?

**2. Giải thích kết quả**
Cho đoạn code sau:

```python
def add_item(item, basket=[]):
    basket.append(item)
    return basket

print(add_item('Apple'))
print(add_item('Banana'))
```

Bạn kỳ vọng hàm in ra gì ở dòng thứ 2? Tại sao kết quả thực tế lại khác với kỳ vọng? (Đây là một trong những bug nguy hiểm nhất Python).

## Tầng 2: Implement

**1. Refactoring với Comprehension**
Viết lại đoạn code dưới đây chỉ bằng 1 dòng duy nhất (dùng dictionary comprehension):

```python
words = ['apple', 'banana', 'cherry', 'date']
word_lengths = {}
for word in words:
    if len(word) > 4:
        word_lengths[word] = len(word)
```

**2. Xây dựng Class Dataset**
Viết một class `ImageDataset` nhận vào 2 tham số lúc khởi tạo (`__init__`):

1. `image_paths`: một list các đường dẫn (string).
2. `labels`: một list các nhãn (integer).
   Class phải có:

- Hàm `__len__` trả về tổng số lượng ảnh.
- Hàm `__getitem__` nhận tham số `index`, trả về một tuple dạng `(image_paths[index], labels[index])`.
  Ném ra lỗi `ValueError` nếu độ dài của `image_paths` và `labels` không bằng nhau lúc khởi tạo.

## Tầng 3: Experiment

**1. Đoạn Bộ Nhớ (Memory Profiling) của Generator**
Tạo 2 hàm để sinh ra bình phương của các số từ 0 đến 10 triệu:

1. Trả về một List:

```python
def list_squares(n):
    return [i**2 for i in range(n)]
```

2. Dùng Generator:

```python
def generator_squares(n):
    for i in range(n):
        yield i**2
```

Thử gọi cả 2 hàm với $N = 10,000,000$. Kiểm tra xem bộ nhớ (RAM) thay đổi như thế nào ở mỗi cách. Tại sao nên dùng cách 2 khi dữ liệu quá lớn?
