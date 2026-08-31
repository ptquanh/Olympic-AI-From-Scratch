# Bài tập: Object Detection

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Tại sao phải có bước NMS?**
Mô hình YOLO có thiết kế dự đoán rất nhiều bounding box tại mỗi ô lưới (grid). Điều này dẫn đến vấn đề gì khi nhận diện một đối tượng lớn như chiếc xe hơi? Tại sao NMS lại giải quyết được?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Tự code IoU bằng Python**
Viết hàm `def compute_iou(boxA, boxB):` nhận vào 2 list tọa độ dạng `[x1, y1, x2, y2]`.
Tính và trả về giá trị IoU. Hãy cẩn thận xử lý trường hợp 2 hình chữ nhật không giao nhau (diện tích giao = 0).

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Phân tích kết quả của NMS**
Viết đoạn code sử dụng hàm `torchvision.ops.nms`.
Cho `boxes = torch.tensor([[100, 100, 210, 210], [105, 105, 215, 215], [300, 300, 400, 400]], dtype=torch.float)`
Cho `scores = torch.tensor([0.9, 0.75, 0.85])`

- Đặt `iou_threshold = 0.5`, chạy NMS và in ra index của các box được giữ lại.
- Thử thay đổi `iou_threshold = 0.9` và xem chuyện gì xảy ra.

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.

## T-1 — Transfer

**Learning outcome:** Chuyển kỹ thuật sang dữ liệu mới mà không leakage, dùng metric và failure mode phù hợp.

**1. Format Conversion**
Trong OpenCV và thư viện albumentations, Bounding box đôi khi được lưu ở dạng YOLO: `[x_center, y_center, width, height]` (tất cả được chuẩn hóa về từ 0 đến 1).
Hãy viết hàm chuyển đổi từ định dạng YOLO sang chuẩn Pascal VOC `[x1, y1, x2, y2]`.
(Giả sử bạn biết kích thước ảnh gốc là $W, H$).

**Kết quả mong đợi:** Pipeline chạy trên dữ liệu/bối cảnh mới, metric phù hợp và phân tích ít nhất một failure mode.

## O-1 — Olympiad

**Learning outcome:** Dựng baseline theo đúng competition profile, timebox và artifact nộp có thể chạy lại.

Trong phòng thi, thường ta sẽ sử dụng thư viện Ultralytics (YOLOv8/v11) để giải bài Object Detection thay vì tự code từ đầu. Lỗi phổ biến nhất khi dùng Ultralytics là file cấu hình `data.yaml` chỉ sai đường dẫn đến thư mục `images/train` và `labels/train`. Hãy lưu ý cấu trúc thư mục YOLO chuẩn.

**Kết quả mong đợi:** Baseline tái lập được trong timebox, validation đúng, metric và checklist file cần nộp.
