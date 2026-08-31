# Code Notes: Object Detection

## 🔑 Core Patterns

```python
# Cấu trúc phổ biến của Bounding Box: [x1, y1, x2, y2]
# Tọa độ (x1, y1) là góc trên cùng bên trái.
# Tọa độ (x2, y2) là góc dưới cùng bên phải.

def calculate_area(box):
    # Chiều rộng = x2 - x1, Chiều cao = y2 - y1
    width = max(0, box[2] - box[0])
    height = max(0, box[3] - box[1])
    return width * height

```

## 📋 API Cheat Sheet

Thường dùng thư viện `torchvision.ops` cho các hàm Detection chuẩn.

| Việc cần làm      | Code                                                  | Link Docs                                                                                   |
| ----------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Chạy NMS chuẩn    | `torchvision.ops.nms(boxes, scores, iou_threshold)`   | [NMS](https://pytorch.org/vision/stable/generated/torchvision.ops.nms.html)                 |
| Chuyển format box | `torchvision.ops.box_convert(boxes, in_fmt, out_fmt)` | [box_convert](https://pytorch.org/vision/stable/generated/torchvision.ops.box_convert.html) |

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                                                             | Thời gian | Hint (ẩn)                          |
| --- | ----------------------------------------------------------------------------------------------- | --------- | ---------------------------------- |
| 1   | Viết hàm tìm `x1` và `y1` của hình chữ nhật phần giao (Intersection) giữa 2 box `boxA`, `boxB`. | 2 phút    | `x_inter1 = max(boxA[0], boxB[0])` |
| 2   | Viết tiếp hàm tìm `x2` và `y2` của hình chữ nhật phần giao.                                     | 2 phút    | `x_inter2 = min(boxA[2], boxB[2])` |

## 🧠 Flashcards

| Hỏi                                                      | Trả lời                                                                                                                                                                                                                    |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AP (Average Precision) là gì?                            | Là diện tích dưới đường cong Precision-Recall. Chỉ số này phản ánh khả năng mô hình vừa bắt trúng đối tượng (Recall cao) vừa không bắt nhầm (Precision cao).                                                               |
| Thuật toán YOLO (You Only Look Once) đột phá ở điểm nào? | Trước YOLO, người ta dùng 2 mạng (1 mạng tìm vùng nghi ngờ, 1 mạng phân loại vùng đó - Faster R-CNN). YOLO gom tất cả thành 1 mạng CNN duy nhất, chia ảnh thành lưới (grid) và dự đoán trực tiếp tọa độ. Tốc độ cực nhanh. |
