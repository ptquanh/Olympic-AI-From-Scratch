# Lời giải: PyTorch Fundamentals

<details><summary><b>Tầng 1: Understand</b></summary>

Vì `loss` thực chất vẫn là một node trong Đồ thị tính toán (Computation Graph) lưu trữ lịch sử các phép toán để phục vụ đạo hàm (chứa grad_fn). `.item()` trích xuất con số giá trị thuần túy khỏi đồ thị đó. Nếu bạn cộng dồn `loss` qua các vòng lặp mà không dùng `.item()` (vd: `total_loss += loss`), bạn sẽ lưu trữ lại toàn bộ đồ thị tính toán của mọi bước, dẫn đến tràn RAM/VRAM cực kỳ nhanh.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
import torch
X = torch.randn(100, 32, 32, 3)

# 1. Đổi chiều (Permute)
# Các chiều ban đầu: N=0, H=1, W=2, C=3. Đưa C lên vị trí số 1.
X = X.permute(0, 3, 1, 2)
print("Shape sau khi permute:", X.shape) # (100, 3, 32, 32)

# 2. Làm phẳng (Flatten/Reshape)
X_flat = X.reshape(100, -1) # -1 sẽ tự tính ra 3*32*32 = 3072
print("Shape sau khi làm phẳng:", X_flat.shape) # (100, 3072)
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

(Mã nguồn tham khảo)

```python
import torch
import time

A = torch.randn(10000, 10000)
B = torch.randn(10000, 10000)

start = time.time()
C = A @ B
print(f"CPU Time: {time.time() - start:.4f}s")

if torch.cuda.is_available():
    A_gpu = A.to('cuda')
    B_gpu = B.to('cuda')
    # Run warmup (để GPU khởi động)
    _ = A_gpu @ B_gpu

    start = time.time()
    C_gpu = A_gpu @ B_gpu
    # Đợi GPU hoàn thành đồng bộ trước khi đếm giờ (vì CUDA chạy bất đồng bộ)
    torch.cuda.synchronize()
    print(f"GPU Time: {time.time() - start:.4f}s")
```

Bạn sẽ thấy GPU nhanh hơn CPU hàng chục đến hàng trăm lần.

</details>

<details><summary><b>Tầng 4: Transfer</b></summary>

```python
from torch.utils.data import Dataset

class ImagePathDataset(Dataset):
    def __init__(self, image_paths):
        self.image_paths = image_paths

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        path = self.image_paths[idx]
        # Trong thực tế, ở đây ta sẽ dùng PIL hoặc cv2 để đọc ảnh
        # image = Image.open(path)
        # Giả lập trả về path và nhãn random 0 hoặc 1
        label = 0 if "cat" in path else 1
        return path, label
```

</details>

<details><summary><b>Tầng 5: Olympiad</b></summary>

Đây là Thần Chú 5 Bước không bao giờ được quên:

```python
# Giả sử dataloader, model, optimizer, criterion đã được khởi tạo
for epoch in range(num_epochs):
    for batch_X, batch_y in dataloader:
        # Bước 1: Xóa gradient cũ
        optimizer.zero_grad()

        # Bước 2: Truyền tiến (Dự đoán)
        predictions = model(batch_X)

        # Bước 3: Tính sai số (Loss)
        loss = criterion(predictions, batch_y)

        # Bước 4: Lan truyền ngược tính đạo hàm
        loss.backward()

        # Bước 5: Cập nhật trọng số
        optimizer.step()
```

</details>
