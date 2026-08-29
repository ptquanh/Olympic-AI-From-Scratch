# Lời giải: Python Essentials

<details><summary><b>Tầng 1: Understand</b></summary>

**1. Mutable vs Immutable**

- Nếu cố gán `my_string[0] = 'a'`, Python sẽ ném ra lỗi `TypeError` vì String là Immutable, không cho phép thay đổi phần tử tại chỗ.
- Lợi ích của Tuple: Nhanh hơn List một chút khi khởi tạo và duyệt qua do bộ nhớ được cấp phát cố định; An toàn hơn khi truyền dữ liệu không muốn bị hàm khác sửa đổi; Có thể dùng làm Key cho Dictionary (List không thể).

**2. Giải thích kết quả**

- Kết quả ở dòng 2: `['Apple', 'Banana']` chứ không phải chỉ `['Banana']`.
- Lý do: Default argument `basket=[]` chỉ được khởi tạo MỘT LẦN duy nhất khi hàm được định nghĩa. Ở những lần gọi sau, hàm tiếp tục dùng chung cái list ban đầu đó (vì List là kiểu tham chiếu/mutable).
- Cách sửa: Để `basket=None`, và trong hàm kiểm tra `if basket is None: basket = []`.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

**1. Refactoring với Comprehension**

```python
word_lengths = {word: len(word) for word in words if len(word) > 4}
```

**2. Xây dựng Class Dataset**

```python
class ImageDataset:
    def __init__(self, image_paths, labels):
        if len(image_paths) != len(labels):
            raise ValueError("Độ dài của image_paths và labels không khớp!")
        self.image_paths = image_paths
        self.labels = labels

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, index):
        return (self.image_paths[index], self.labels[index])
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

**1. Memory Profiling**

- Hàm 1 (List): Bắt buộc phải tính toán đủ 10 triệu con số và nạp TẤT CẢ vào RAM cùng một lúc. Rất dễ bị tràn RAM.
- Hàm 2 (Generator): Tính toán "lazy" (đến đâu tính đến đó). Mỗi lần chỉ nhả ra 1 con số, gần như không tốn thêm RAM. Trong AI (nhất là xử lý ảnh/video), việc sinh dữ liệu theo kiểu yield/generator (DataLoader) là sống còn.
</details>
