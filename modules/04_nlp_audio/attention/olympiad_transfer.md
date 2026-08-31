# Olympic transfer: Attention

> **Profile mặc định:** General. Không có thời lượng, thư viện hay quyền truy cập mạng mặc định. Xem [competition profiles](../../../COMPETITION_PROFILES.md) trước khi dùng trong một kỳ thi cụ thể.

## Nhận diện trong đề

Attention hữu ích khi mỗi phần tử cần tổng hợp thông tin từ các phần tử khác: văn bản, chuỗi thời gian, tập hợp hoặc đặc trưng ảnh. Đây không phải lựa chọn tự động cho mọi dữ liệu; với bảng nhỏ, mô hình cây thường là baseline nhanh và mạnh hơn.

## Baseline tối thiểu

1. Chốt shape `(batch, sequence, embedding)`.
2. Tạo padding/causal mask đúng semantics của API.
3. Assert trọng số attention hữu hạn và tổng theo hàng xấp xỉ 1.
4. So sánh với baseline không attention trên cùng split và metric.

Trong learning profile có thể dùng `torch.nn.MultiheadAttention(batch_first=True)`. Trong contest profile, chỉ dùng khi PyTorch và API này có trong danh sách cho phép.

## Metric và validation

Attention không có metric downstream riêng. Dùng metric của nhiệm vụ: Macro F1 cho phân loại lệch lớp, BLEU/chrF cho dịch máy, ROUGE cho tóm tắt khi phù hợp. Giữ nguyên split khi so sánh kiến trúc và báo cả thời gian/VRAM.

## Failure modes

- Mask sai chiều hoặc ngược semantics làm mô hình chú ý vào padding/tương lai.
- Logit lớn gây softmax bão hòa; cần chia `sqrt(d_k)` và softmax ổn định.
- Bộ nhớ tăng theo `O(sequence_length²)`; giảm chiều dài, batch hoặc dùng kernel tối ưu nếu profile cho phép.
- Gọi `view` sau `transpose` trên tensor không contiguous; dùng `reshape` hoặc `contiguous().view(...)`.

## Sau baseline

Chỉ thay đổi một yếu tố mỗi lần: số head, `d_model`, mask, pooling hoặc độ dài chuỗi. Lưu seed, config, metric và runtime. Không thêm FlashAttention/xFormers nếu package không nằm trong môi trường contest.

## Timebox

Không gán mốc 4h/6h chung. Dành tối đa 10–15% timebox của profile để dựng baseline và shape tests; giữ tối thiểu 15% cuối để infer, kiểm file nộp và chạy lại từ môi trường sạch.
