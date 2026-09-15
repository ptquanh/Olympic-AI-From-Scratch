# Postmortem: Validation — Đo đúng khả năng tổng quát hóa

## Phân tích reference

- **Mục tiêu:** Chọn K-fold, stratified, group hoặc time split theo đơn vị dự đoán.
- **Failure mode có chủ đích:** Nếu row CV cao còn group CV thấp, pipeline có thể đang nhớ group. Group score thấp là thông tin về bài toán; không được đổi về row split để làm báo cáo đẹp.
- **Bằng chứng cần xem:** bảng comparison/diagnostic ở solution, assertion của split và CSV đọc lại. Kết quả phải lấy từ lần chạy của bạn, không chép số dự đoán thành số đo.
- **Quyết định:** So sánh StratifiedKFold với GroupKFold bằng cùng KNN pipeline và cùng dữ liệu. Đó là so sánh hai cách ước lượng, không phải chọn split có điểm cao nhất. KFold dùng khi dòng i.i.d.; StratifiedKFold thêm cân bằng nhãn nhưng không tách group; TimeSeriesSplit cần dữ liệu đã sort và gap phù hợp độ trễ label.
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
