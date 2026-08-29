# CNN Architectures

> **Track:** Foundation ⭐ | Contest ⭐

## ① Prerequisite Check

(Chưa có)

## ② Learning Outcomes

- Liệt kê được sự khác nhau giữa LeNet, VGG, ResNet.
- Sử dụng được Transfer Learning với `timm` hoặc `torchvision`.

## ③ Concept Map

Convolution ➔ **CNN Architectures** ➔ Image Classification

## ④ Intuition

Kiến trúc mạng giống như bản vẽ thiết kế một tòa nhà. LeNet giống như ngôi nhà cấp 4. VGG giống như tòa chung cư 19 tầng. Nhưng càng xây cao thì càng dễ bị "sập" (Vanishing Gradient). ResNet đã phát minh ra "cầu thang thoát hiểm" (Residual Connection) cho phép xây tòa nhà hàng trăm tầng mà không sập.

## ⑤ Math/Derivation

Residual Connection: $F(x) = H(x) - x \rightarrow$ Lớp mạng chỉ cần học phần dư $F(x)$ thay vì học lại cả $H(x)$. Đầu ra thực sự là $F(x) + x$.

## ⑥ Worked Example

Khi đi qua 50 lớp CNN, thông tin bị "mòn" dần. Residual Connection cộng trực tiếp ảnh gốc (hoặc feature map trước đó) vào đầu ra để bù đắp sự hao mòn này.

## ⑩ Misconceptions

❌ **Sai:** Cứ lấy mạng xịn nhất, bự nhất (ViT Huge) để train là auto điểm cao.
✅ **Đúng:** Mạng càng to càng cần nhiều dữ liệu để không bị Overfitting. Với dữ liệu nhỏ, ResNet18 thường ăn đứt các mạng khổng lồ.

## ⑮ Mastery Check

- ResNet giải quyết vấn đề gì của VGG?

## ⑯ Time Estimate

Theory: ~1h, Code: ~30m, Exercises: ~30m
