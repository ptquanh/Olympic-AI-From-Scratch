# Postmortem: EDA — Khám phá dữ liệu trước baseline

## Phân tích reference

- **Mục tiêu:** Lập báo cáo schema, missing, duplicate và class balance có số liệu.
- **Failure mode có chủ đích:** Điểm tăng mạnh khi thêm after_event là phản ví dụ có chủ đích; quyết định đúng là bỏ cột. Nếu group overlap khác 0, quay về split trước khi chỉnh model.
- **Bằng chứng cần xem:** bảng comparison/diagnostic ở solution, assertion của split và CSV đọc lại. Kết quả phải lấy từ lần chạy của bạn, không chép số dự đoán thành số đo.
- **Quyết định:** Dedupe đúng các bản ghi nhân đôi trước khi chia. Dùng GroupShuffleSplit theo patient_id; assert tập người không giao nhau. Fit imputer/scaler chỉ trên train. Label validation chỉ dùng evaluate. Không dùng `after_event`, patient_id hoặc row ID làm feature.
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
