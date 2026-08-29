# Competition Lab: Image Classification

> **Track:** Foundation ⭐ | Contest ⭐

## Giới thiệu

Chào mừng bạn đến với mô hình thi đấu (Competition Lab). Đây không phải là chương lý thuyết. Bạn sẽ đóng vai trò là một chiến binh Olympic AI, nhận một bộ dữ liệu chưa qua chỉnh sửa và phải nộp một pipeline hoàn chỉnh (thường là dưới dạng file `.ipynb` hoặc `submission.csv`).

## Nhiệm vụ: Dog vs Cat Classification (Nhưng khó hơn)

Trong cuộc thi này, bạn sẽ xây dựng một mô hình phân loại ảnh. Bạn KHÔNG ĐƯỢC train model từ con số 0 (vì mất quá nhiều thời gian). Bắt buộc phải sử dụng **Transfer Learning**.

### Yêu cầu cụ thể:

1. Tải một mô hình Pre-trained từ `torchvision.models` hoặc `timm` (Ví dụ: ResNet18 hoặc EfficientNet).
2. Viết Custom `Dataset` và `DataLoader` để đọc ảnh từ folder (sử dụng thư viện `PIL` hoặc `cv2`).
3. Thực hiện Data Augmentation ngẫu nhiên (chỉ trên tập Train, tập Val phải giữ nguyên).
4. Thay thế lớp cuối cùng của mô hình để Output ra 2 classes thay vì 1000 classes như ImageNet.
5. Huấn luyện mô hình, lưu lại Checkpoint có Loss trên tập validation nhỏ nhất (`best_model.pth`).
6. Trình bày được Test Accuracy và vẽ Confusion Matrix.

## ⑯ Time Estimate

Lab: ~3h (Bao gồm thời gian cho GPU train mô hình)
