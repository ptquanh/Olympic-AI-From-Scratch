# Image Fundamentals

> **Track:** Foundation ⭐ | Contest ⏭️

## ① Prerequisite Check

(Chưa có)

## ② Learning Outcomes

- Đọc, hiển thị và lưu ảnh bằng `cv2` và `PIL`.
- Hiểu các kênh màu RGB, không gian màu HSV.
- Thay đổi kích thước (Resize) và Chuẩn hóa (Normalize) giá trị pixel về [0, 1].

## ③ Concept Map

Python ➔ **Image Fundamentals** ➔ Augmentation

## ④ Intuition

Máy tính không nhìn thấy bức ảnh con chó như chúng ta. Nó chỉ nhìn thấy một ma trận khổng lồ các con số từ 0 đến 255. Mỗi điểm ảnh (pixel) được pha trộn từ 3 màu cơ bản: Đỏ (Red), Lục (Green), Lam (Blue).

## ⑤ Math/Derivation

Pixel normalization: $X_{norm} = \frac{X}{255.0}$. Chuẩn hóa giúp cho Gradient Descent trơn tru hơn.

## ⑥ Worked Example

Ảnh 2x2, mỗi pixel có 3 số (R,G,B). Tổng cộng có $2 \times 2 \times 3 = 12$ con số lưu trong RAM.

## ⑩ Misconceptions

❌ **Sai:** Hàm `cv2.imread()` đọc ảnh theo chuẩn RGB.
✅ **Đúng:** OpenCV mặc định đọc ảnh theo hệ BGR (Blue, Green, Red). Nếu muốn in ra màn hình bằng `matplotlib` cho đúng màu, phải convert từ BGR sang RGB.

## ⑮ Mastery Check

- Kích thước ảnh 100x100 RGB chứa bao nhiêu giá trị pixel?

## ⑯ Time Estimate

Theory: ~30m, Code: ~30m, Exercises: ~30m
