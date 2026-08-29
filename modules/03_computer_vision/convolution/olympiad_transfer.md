# Olympiad Transfer: Convolution

## 1. Nhận diện trong đề

Bất kỳ bài toán nào liên quan đến ảnh đều phải dùng CNN. Mặc định là vậy. Trừ khi đề bài yêu cầu cụ thể dùng Vision Transformer (ViT).

## 2. Lỗi thường gặp

- **Lỗi Shape mismatch khi nối Conv sang Linear**:
  Giả sử ảnh đầu vào 28x28, đi qua Conv1 (out=16), MaxPool(2x2), Conv2 (out=32), MaxPool(2x2).
  Kích thước ảnh sau cùng sẽ bị thu nhỏ lại (28 -> 14 -> 7).
  Do đó tensor đầu ra sẽ là `(Batch, 32, 7, 7)`.
  Khi Flatten, ta có `32 * 7 * 7 = 1568`.
  Lớp Linear đầu tiên của bạn BẮT BUỘC phải nhận input là 1568 (`nn.Linear(1568, 128)`). Nếu tính nhầm, code sẽ văng lỗi ngay lập tức!
- **Mẹo chống cháy**: Cứ khai báo `nn.Linear(1, 128)` trước, in ra shape của tensor ngay trước lớp Linear để xem nó là bao nhiêu, sau đó sửa lại số 1 thành con số đó. (Kỹ năng hack trong phòng thi rất quan trọng).
