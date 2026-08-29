# Rubric Chấm Điểm

Tổng điểm: 100đ. Cần đạt >= 80đ để xem như "qua môn" chương này.

## 1. Data Pipeline (30đ)

- [ ] (10đ) Kế thừa chuẩn `torch.utils.data.Dataset`. Hàm `__len__` và `__getitem__` hoạt động không có lỗi.
- [ ] (10đ) Sử dụng ít nhất 2 phương pháp Augmentation (VD: HorizontalFlip, ColorJitter) vào tập Train.
- [ ] (10đ) Áp dụng đúng `transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])` của ImageNet.

## 2. Model & Training (40đ)

- [ ] (10đ) Tải thành công Pre-trained model và sửa lại số Output Classes chuẩn xác.
- [ ] (10đ) Vòng lặp Train đúng 5 bước chuẩn mực (Zero grad -> Forward -> Loss -> Backward -> Step).
- [ ] (10đ) Vòng lặp Validation đúng chuẩn (`model.eval()` và `torch.no_grad()`).
- [ ] (10đ) Viết code lưu lại file `best_model.pth` khi Valid Loss giảm.

## 3. Evaluation & Inference (30đ)

- [ ] (15đ) Load lại file `best_model.pth` và chạy dự đoán thử trên 1 tấm ảnh bên ngoài (Ảnh tải trên mạng xuống).
- [ ] (15đ) Sử dụng `sklearn.metrics.confusion_matrix` kết hợp `seaborn.heatmap` để vẽ ma trận nhầm lẫn đẹp mắt.
