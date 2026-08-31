# Postmortem: Image Classification Competition

## Kết quả baseline Beta

Dữ liệu được sinh deterministically: mỗi lớp có một hình học khác nhau cộng nhiễu nhẹ, vì vậy validation score phải tốt hơn random chance. Pipeline đi đủ `Data → EDA → Train → Validate → Infer → Submit` và chạy offline; nó không giả vờ đánh giá pretrained CNN trên nhãn ngẫu nhiên.

## Điều làm đúng

- Split trước mọi bước học từ dữ liệu; seed và class balance được ghi.
- Baseline đơn giản giúp kiểm chứng dữ liệu/metric/submission trước khi tăng độ phức tạp.
- Validation và test transform là deterministic; submission giữ đúng ID.

## Failure modes cần kiểm

- Ảnh/mask/label lệch hàng sau khi shuffle metadata.
- Augmentation làm đổi semantics nhãn hoặc vô tình áp lên validation.
- Accuracy che khuất lớp hiếm; dùng Macro F1/confusion matrix khi lệch lớp.
- `model.eval()` hoặc `no_grad()` bị quên trong pipeline PyTorch.
- Resize/interpolation khác giữa train và infer.
- Chọn checkpoint/threshold theo public leaderboard gây overfit.

## Cải tiến hợp lệ

Theo thứ tự: feature có cấu trúc → CNN nhỏ → augmentation có giả thuyết → pretrained encoder đã cache và được profile cho phép. Mỗi bước dùng cùng split, báo metric, runtime và memory. Không có learning rate hoặc kiến trúc nào luôn tốt; quyết định bằng validation.

## Checklist trước nộp

Chạy lại kernel sạch/offline, load artifact, infer toàn bộ test một lần, assert schema/row count/ID/NaN và lưu config + seed + metric cạnh submission.
