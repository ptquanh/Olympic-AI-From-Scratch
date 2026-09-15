# Notebook Checklist — Restart & Run All

Chạy checklist này trên notebook tạo kết quả cuối, ví dụ `generate_result.ipynb` nếu thể lệ yêu cầu tên đó.

## Trước khi chạy

- [ ] Kernel/environment đúng profile thi.
- [ ] Seed được cố định ở một cell setup rõ ràng.
- [ ] Không có `pip install`, `git clone` hoặc download ngầm nếu luật cấm mạng.
- [ ] Không có path tuyệt đối theo máy cá nhân.
- [ ] Input path và output path nằm trong cấu trúc được phép.
- [ ] Model/config được load từ artifact final, không từ checkpoint thử nghiệm.

## Restart & Run All

- [ ] Restart kernel.
- [ ] Run All từ cell đầu đến cuối mà không chạy cell riêng lẻ.
- [ ] Không có exception/warning làm thay đổi kết quả.
- [ ] Runtime tổng nằm trong giới hạn.
- [ ] File output được tạo mới từ đầu.

## Kiểm tra output

- [ ] Tên file đúng.
- [ ] Số dòng/bản ghi đúng.
- [ ] Tên cột/key đúng schema.
- [ ] ID giữ đúng thứ tự nếu đề yêu cầu.
- [ ] Không có NaN/Inf/null ngoài quy định.
- [ ] Label/range/type hợp lệ.
- [ ] Hash hoặc timestamp của artifact final được ghi vào report nếu cần tái lập.

## Cross-review

Một thành viên khác mở notebook từ đầu và trả lời được ba câu: input ở đâu, model nào được dùng, output được sinh ở cell nào. Nếu không trả lời được, notebook chưa đủ rõ để freeze.
