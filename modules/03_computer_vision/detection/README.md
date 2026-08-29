# Object Detection

> **Track:** Foundation ⭐ | Contest ⭐

## ① Prerequisite Check

- Bạn có biết làm cách nào để tính diện tích của một hình chữ nhật giao nhau giữa hai hình chữ nhật khác không?

## ② Learning Outcomes

- Cài đặt được hàm tính IoU (Intersection over Union).
- Hiểu và cài đặt được thuật toán NMS (Non-Maximum Suppression) để lọc các bounding box trùng lặp.
- Nắm vững khái niệm mAP (Mean Average Precision) để đánh giá mô hình.
- Nắm được luồng kiến trúc cơ bản của dòng họ YOLO.

## ③ Concept Map

Convolution ➔ **Detection** ➔ Segmentation

## ④ Intuition

Nếu Phân loại ảnh (Classification) chỉ trả lời câu hỏi "Bức ảnh này có con chó không?", thì Phát hiện đối tượng (Detection) trả lời 2 câu hỏi: "Con chó NẰM Ở ĐÂU?" và "Có BAO NHIÊU con chó?". Để làm được điều này, mô hình phải học cách dự đoán các Bounding Box (khung hình chữ nhật) bao quanh vật thể, thường được biểu diễn bằng 4 tọa độ: `[x_min, y_min, x_max, y_max]` hoặc `[x_center, y_center, width, height]`.

## ⑤ Math/Derivation

**IoU (Giao trên Hợp):**
$IoU = \frac{\text{Diện tích phần giao}}{\text{Diện tích tổng 2 khung} - \text{Diện tích phần giao}}$
IoU chạy từ 0 đến 1. IoU càng cao tức là 2 khung hình càng chồng khít lên nhau.

## ⑥ Worked Example

Box A (dự đoán): Diện tích 100.
Box B (thực tế): Diện tích 120.
Diện tích phần giao nhau: 60.
$IoU = \frac{60}{100 + 120 - 60} = \frac{60}{160} = 0.375$.
Với ngưỡng IoU là 0.5, dự đoán này được coi là Sai (False Positive).

## ⑩ Misconceptions

❌ **Sai:** Mô hình Detection sẽ trực tiếp output ra số lượng đúng khung hình chữ nhật trong ảnh.
✅ **Đúng:** Mô hình luôn phun ra HÀNG NGÀN khung hình (anchors/predictions) trên toàn bộ bức ảnh. Nhiệm vụ của ta là dùng NMS (Non-Maximum Suppression) để vứt đi những khung hình bị trùng lặp và giữ lại khung tự tin nhất.

## ⑮ Mastery Check

- Nếu hai khung hình không giao nhau chút nào, IoU bằng mấy?
- Trong NMS, ta vứt bỏ các khung hình thỏa mãn điều kiện gì?

## ⑯ Time Estimate

Theory: ~1.5h, Code: ~2h, Exercises: ~1.5h
