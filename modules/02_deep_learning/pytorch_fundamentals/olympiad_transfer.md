# Olympiad Transfer: PyTorch Fundamentals

## 1. Nhận diện trong đề
Bất kỳ đề thi nào liên quan đến Computer Vision (Phân loại ảnh, Phân vùng ảnh, Nhận diện khuôn mặt) hoặc NLP (Dịch máy, Phân loại văn bản) sử dụng Deep Learning đều yêu cầu bạn viết vòng lặp huấn luyện PyTorch.

## 2. Baseline tối thiểu
- Hãy tạo một hàm `train_one_epoch(model, dataloader, criterion, optimizer, device)` để tái sử dụng.
- Baseline nhanh nhất là tạo được bộ `Dataset` và `DataLoader` để mô hình ăn được dữ liệu. Hãy chú ý kỹ kiểu dữ liệu:
  - Input `X`: Luôn là `torch.float32`.
  - Target `y` (cho bài toán Phân loại phân nhóm): Luôn là `torch.long`. (Cực kỳ hay dính lỗi này).

## 3. Failure modes (Lỗi thường gặp nhất phòng thi)
1. **Lỗi Runtime Error: Input and target shapes do not match**: Đặc biệt với tập nhãn 1D. Bạn cần dùng lệnh `y.squeeze()` hoặc `y.unsqueeze(1)` để đồng bộ số chiều với model output.
2. **Lỗi OOM (Out Of Memory) - Hết VRAM GPU**: Xảy ra do batch size quá to. Cách xử lý duy nhất trong phòng thi là hạ `batch_size` xuống (từ 64 -> 32 -> 16 -> 8). Nếu vẫn bị, kiểm tra xem bạn có bị quên gọi `loss.item()` khi lưu lại mảng loss hay không (việc này khiến rò rỉ bộ nhớ).
3. **Lỗi Device Mismatch**: "Expected all tensors to be on the same device". Xảy ra khi bạn truyền dữ liệu vào mô hình mà quên gọi `batch_X.to(device)`. Mô hình ở trên CUDA nhưng dữ liệu vẫn ở CPU.

## 4. Sau baseline
- Khi đã có training loop cơ bản hoạt động không báo lỗi. Bạn sẽ bắt tay vào theo dõi đồ thị Loss, tinh chỉnh kiến trúc mạng và thêm augmentation.
