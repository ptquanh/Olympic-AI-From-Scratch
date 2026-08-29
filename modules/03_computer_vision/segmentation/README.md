# Image Segmentation

> **Track:** Foundation 📖 | Contest ⭐

## ① Prerequisite Check

(Chưa có)

## ② Learning Outcomes

- Phân biệt được Semantic Segmentation và Instance Segmentation.
- Hiểu kiến trúc U-Net (Encoder - Decoder).
- Đánh giá bằng Dice Coefficient / mIoU.

## ③ Concept Map

Detection ➔ **Segmentation** ➔ Generative CV

## ④ Intuition

Nếu Detection vẽ hình hộp quanh con chó, thì Segmentation vẽ một đường viền ôm SÁT từng sợi lông của con chó. Nó gán nhãn cho TỪNG PIXEL một trên bức ảnh. U-Net là kiến trúc nổi tiếng nhất, có hình dạng chữ U: Bên trái (Encoder) thu nhỏ ảnh để gom ngữ cảnh, bên phải (Decoder) phóng to ảnh lại kích thước ban đầu để tô màu.

## ⑤ Math/Derivation

Dice Coefficient = $\frac{2 \times |A \cap B|}{|A| + |B|}$. Khá giống với IoU nhưng hệ số phạt/thưởng hơi khác một chút.

## ⑥ Worked Example

Tập ảnh y tế: phân đoạn khối u. Mọi pixel thuộc khối u phải trả về giá trị 1, các pixel khác trả về 0.

## ⑩ Misconceptions

❌ **Sai:** Output của Segmentation Model là 1 bức ảnh JPEG có màu.
✅ **Đúng:** Output là 1 ma trận (Tensor) chứa xác suất từng pixel thuộc class nào, giống hệt bài Classification, nhưng diễn ra ở mức độ Pixel.

## ⑮ Mastery Check

- Kiến trúc U-Net kết nối nhánh Encoder và Decoder bằng kỹ thuật gì?

## ⑯ Time Estimate

Theory: ~1h, Code: ~45m, Exercises: ~45m
