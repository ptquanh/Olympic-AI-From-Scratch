# Postmortem: Ensembling — Averaging, Blending và Stacking

## Phân tích reference

- **Mục tiêu:** Gộp probability theo đúng ID và class order.
- **Failure mode có chủ đích:** Stacking có thể kém forest trên dataset nhỏ do meta-feature nhiễu và OOF distribution khác full-train prediction. Đó là kết quả hợp lệ; không đổi split để ép ensemble thắng.
- **Bằng chứng cần xem:** bảng comparison/diagnostic ở solution, assertion của split và CSV đọc lại. Kết quả phải lấy từ lần chạy của bạn, không chép số dự đoán thành số đo.
- **Quyết định:** Outer hold-out 25% dành so sánh cuối của thí nghiệm. Stacking tạo OOF chỉ trong outer-train. Blending tách riêng blend set từ outer-train; chọn weight bằng log loss trên blend, rồi giữ đúng base models đó để đánh giá. Không fit meta-model hoặc weight bằng outer-validation. Sau khi chọn cách nộp bằng outer-validation, score này là development score, không phải đánh giá cuối độc lập.
- **Giới hạn:** dữ liệu nhỏ do notebook tạo; chưa kiểm chứng chất lượng trên đề thi thật hoặc thời gian học của người mới.

## Nhật ký sau bài O-1

Điền sau lần chạy có giới hạn thời gian; để trống mục chưa đo thay vì ghi pass.

| Câu hỏi               | Evidence cần ghi                                |
| --------------------- | ----------------------------------------------- |
| Bạn dự đoán gì?       | Hypothesis trước khi chạy và outcome liên quan  |
| Đã thay gì?           | Một biến/config, giữ nguyên split và metric     |
| Kết quả thực tế?      | Score, runtime, đường dẫn artifact và seed      |
| Điều gì sai?          | Repro nhỏ nhất, lỗi contract hoặc assumptions   |
| Root cause?           | Quan sát phân biệt nguyên nhân với triệu chứng  |
| Đã sửa và kiểm lại?   | Lệnh/cell rerun, before/after và kết quả assert |
| Lần sau làm gì trước? | Một hành động cụ thể, timebox và điều kiện dừng |

## Kế hoạch lần kế tiếp

Lặp lại trên một biến thể bài T-1. Đóng băng split trước khi tune; giữ baseline và log cả thử nghiệm thất bại. Dành phần cuối timebox cho kernel sạch, đọc file output và kiểm ID.
