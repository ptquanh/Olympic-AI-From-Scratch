# Olympiad Transfer: Object Detection

> **Profile áp dụng:** General, trừ các mục ghi rõ PTIT 2026. Các mốc 4h/6h trong tài liệu này chỉ là timebox của PTIT 2026, không phải luật chung. Đã kiểm chứng 2026-08-31; xem [competition profiles](../../../COMPETITION_PROFILES.md) và ưu tiên thông báo chính thức mới hơn.

## 1. Nhận diện trong đề

Bài toán yêu cầu "Phát hiện", "Đếm số lượng", "Xác định tọa độ" của vật thể trong ảnh (Xe cộ, Biển số xe, Tế bào ung thư). Metric thường dùng là mAP@0.5 hoặc mAP@0.5:0.95.

## 2. Baseline tối thiểu

**ĐỪNG TỰ CODE KIẾN TRÚC**. Hãy tải ngay thư viện `ultralytics` (YOLO) về.

- Chuẩn bị dữ liệu: Chuyển dữ liệu của Ban tổ chức sang định dạng `.txt` của YOLO.
- File `data.yaml` chuẩn:

```yaml
train: ../train/images
val: ../val/images
nc: 2
names: ["cat", "dog"]
```

- Khởi chạy training: `yolo train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640`
  Baseline này thường giải quyết được 70-80% số điểm của bài toán Detection.

## 3. Failure modes

- **Quên chuẩn hóa tọa độ**: File YOLO `.txt` yêu cầu tọa độ $x, y, w, h$ chia cho Width/Height ảnh gốc (giá trị từ 0-1). Nếu bạn ghi thẳng pixel (vd: 500), loss sẽ bị văng (NaN) lập tức.
- **Dữ liệu nhỏ**: Ảnh quá to (1920x1080) nhưng vật thể lại quá nhỏ (tế bào 5x5 pixel). Khi train YOLO resize về 640x640, vật thể nhỏ bị mất hoàn toàn thông tin, không thể detect được. Giải pháp là chia nhỏ ảnh ra bằng thuật toán Slicing (SAHI).
