# Bài tập: Data Augmentation

## Tầng 1: Understand

**1. Câu hỏi lý thuyết**
Bài toán nhận diện chữ số viết tay (MNIST). Có nên dùng RandomHorizontalFlip không? Tại sao?

## Tầng 2: Implement

**1. Thực hành code**
Viết Compose kết hợp 3 transform: Resize(256), RandomCrop(224), ToTensor().

## Tầng 3: Experiment

**1. Tác động của Normalize**
Thử Normalize một ảnh bằng `transforms.Normalize((0.5,), (0.5,))`.
In ra giá trị lớn nhất và nhỏ nhất của tensor ảnh sau khi chuẩn hóa. Giá trị giờ nằm trong khoảng nào?
