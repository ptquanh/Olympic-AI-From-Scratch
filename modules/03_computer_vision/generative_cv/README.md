# Generative CV

> **Track:** Foundation ⚡ | Contest 📖

## ① Prerequisite Check

(Chưa có)

## ② Learning Outcomes

- Phân biệt được GAN và Diffusion Models.
- Nắm được khái niệm chung của Self-supervised learning (CLIP).

## ③ Concept Map

Segmentation ➔ **Generative CV** ➔ Hết Module 03

## ④ Intuition

Thay vì phân loại chó, ta bắt máy tính VẼ ra con chó. GAN dùng 2 mạng đánh nhau (1 họa sĩ vẽ giả, 1 cảnh sát bắt giả). Diffusion thì giống như tạc tượng: thêm nhiễu (noise) làm hỏng bức ảnh, rồi dạy mô hình cách gột rửa nhiễu để khôi phục lại ảnh.

## ⑤ Math/Derivation

Diffusion Forward Process: $x_t = \sqrt{\alpha_t} x_{t-1} + \sqrt{1 - \alpha_t} \epsilon$

## ⑥ Worked Example

Midjourney và Stable Diffusion đều sử dụng cốt lõi là Diffusion Model.

## ⑩ Misconceptions

❌ **Sai:** GAN đã lỗi thời, giờ ai cũng dùng Diffusion.
✅ **Đúng:** Diffusion cho ra ảnh chất lượng rất cao nhưng chạy CỰC KỲ CHẬM (phải lặp vài chục bước khử nhiễu). GAN thì sinh ra ảnh cực nhanh (chỉ cần 1 forward pass), ứng dụng tốt ở realtime video deepfake.

## ⑮ Mastery Check

- Generator và Discriminator trong GAN đối kháng nhau như thế nào?

## ⑯ Time Estimate

Theory: ~1h, Code: ~30m, Exercises: ~30m
