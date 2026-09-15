# Postmortem: Debugging ML — Tìm lỗi bằng kiểm chứng nhỏ

## Phân tích reference

- **Mục tiêu:** Khoanh vùng lỗi data, shape, loss và update bằng kiểm tra tối thiểu.
- **Failure mode có chủ đích:** Fixture của lab xác định lỗi dấu update. Nếu dữ liệu thật có NaN, sai shape hoặc label mapping, cần sửa những lỗi đó trước; không gán mọi loss tăng cho learning rate.
- **Bằng chứng cần xem:** bảng comparison/diagnostic ở solution, assertion của split và CSV đọc lại. Kết quả phải lấy từ lần chạy của bạn, không chép số dự đoán thành số đo.
- **Quyết định:** Stratified hold-out 25%, scaler chỉ fit train. Batch gradient check và tiny-overfit dùng training hoặc fixture riêng; không fit theo y_validation. Seed 42, float64 cho kiểm tra số.
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
