# Bài tập: Object Detection

## Tầng 1: Understand

**1. Tại sao phải có bước NMS?**
Mô hình YOLO có thiết kế dự đoán rất nhiều bounding box tại mỗi ô lưới (grid). Điều này dẫn đến vấn đề gì khi nhận diện một đối tượng lớn như chiếc xe hơi? Tại sao NMS lại giải quyết được?

## Tầng 2: Implement

**1. Tự code IoU bằng Python**
Viết hàm `def compute_iou(boxA, boxB):` nhận vào 2 list tọa độ dạng `[x1, y1, x2, y2]`.
Tính và trả về giá trị IoU. Hãy cẩn thận xử lý trường hợp 2 hình chữ nhật không giao nhau (diện tích giao = 0).

## Tầng 3: Experiment

**1. Phân tích kết quả của NMS**
Viết đoạn code sử dụng hàm `torchvision.ops.nms`.
Cho `boxes = torch.tensor([[100, 100, 210, 210], [105, 105, 215, 215], [300, 300, 400, 400]], dtype=torch.float)`
Cho `scores = torch.tensor([0.9, 0.75, 0.85])`

- Đặt `iou_threshold = 0.5`, chạy NMS và in ra index của các box được giữ lại.
- Thử thay đổi `iou_threshold = 0.9` và xem chuyện gì xảy ra.

## Tầng 4: Transfer

**1. Format Conversion**
Trong OpenCV và thư viện albumentations, Bounding box đôi khi được lưu ở dạng YOLO: `[x_center, y_center, width, height]` (tất cả được chuẩn hóa về từ 0 đến 1).
Hãy viết hàm chuyển đổi từ định dạng YOLO sang chuẩn Pascal VOC `[x1, y1, x2, y2]`.
(Giả sử bạn biết kích thước ảnh gốc là $W, H$).

## Tầng 5: Olympiad

Trong phòng thi, thường ta sẽ sử dụng thư viện Ultralytics (YOLOv8/v11) để giải bài Object Detection thay vì tự code từ đầu. Lỗi phổ biến nhất khi dùng Ultralytics là file cấu hình `data.yaml` chỉ sai đường dẫn đến thư mục `images/train` và `labels/train`. Hãy lưu ý cấu trúc thư mục YOLO chuẩn.
