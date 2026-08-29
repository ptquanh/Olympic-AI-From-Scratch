# Data Augmentation

> **Track:** Foundation ⭐ | Contest 📖

## ① Prerequisite Check

(Chưa có)

## ② Learning Outcomes

- Sử dụng được `torchvision.transforms` để biến đổi ảnh.
- Hiểu tại sao cần tăng cường dữ liệu: chống overfitting.

## ③ Concept Map

Image Fundamentals ➔ **Augmentation** ➔ CNN

## ④ Intuition

Nếu bạn chỉ cho em bé xem ảnh con chó đứng thẳng, em bé sẽ không nhận ra con chó nếu ảnh bị lộn ngược. Data Augmentation giúp tạo ra vô số "phiên bản" ảo của tấm ảnh gốc (lật, xoay, làm nhòe, đổi màu) để mô hình học được đặc trưng bản chất của vật thể, thay vì học vẹt.

## ⑤ Math/Derivation

Không có công thức toán cốt lõi. Thuần túy là phép biến đổi hình học (Affine Transformation).

## ⑥ Worked Example

Từ 1000 ảnh gốc, nếu ta lật ngang ngẫu nhiên (xác suất 50%), ta đã giúp model tiếp xúc với "không gian" 2000 bức ảnh.

## ⑩ Misconceptions

❌ **Sai:** Càng áp dụng nhiều kỹ thuật Augmentation càng tốt.
✅ **Đúng:** Augmentation phải phù hợp với thực tế. Ví dụ bài toán nhận diện biển báo giao thông: không được lật ngang ảnh (Flip), vì biển "Rẽ phải" lật ngang sẽ thành "Rẽ trái" (sai nhãn).

## ⑮ Mastery Check

- Khi nào thì KHÔNG ĐƯỢC lật dọc (Vertical Flip) ảnh?

## ⑯ Time Estimate

Theory: ~45m, Code: ~45m, Exercises: ~45m
