# Đóng góp cho Olympic AI From Scratch

Cảm ơn bạn muốn giúp giáo trình tốt hơn. Repo đang ở trạng thái **Technical Review Beta**: nội dung có thể đã qua kiểm tra kỹ thuật nhưng chưa được coi là `Published` cho đến khi có người thuộc đúng nhóm độc giả học thử.

## Trước khi bắt đầu

1. Đọc `.agents/rules/curriculum-design.md` và `curriculum.yml`.
2. Mở issue mô tả chương, lỗi hoặc learning outcome cần sửa. Với lỗi toán/code, kèm ví dụ tái hiện và nguồn.
3. Chỉ sửa đúng phạm vi issue. Không đổi archetype hoặc dependency graph nếu chưa cập nhật manifest và tài liệu liên quan.

## Chuẩn pull request

- Nội dung chính viết bằng tiếng Việt; thuật ngữ English được giải thích ở lần đầu.
- Mọi phát biểu dễ thay đổi theo kỳ thi phải có competition profile, năm, nguồn chính thức và ngày kiểm chứng.
- Mọi bài tập có ID `U/I/E/T/O-n`, expected output và lời giải cùng ID.
- Notebook không tự cài package, không clone repo, không dùng đường dẫn tuyệt đối và phải hỗ trợ `OAI_FAST_MODE=1`.
- Luôn chạy static audit. Nếu PR thay notebook, chỉ chạy các notebook bị ảnh hưởng và xác minh report tạm:

```bash
python tools/audit_curriculum.py
python tools/run_notebooks.py --fast --profile cpu --offline --repeats 2 --changed-since origin/master
python tools/verify_notebook_report.py _dev/notebook_report.json --profile cpu --min-repeats 2 --allow-partial

```

- Không commit report JSON. CI lưu report dưới dạng artifact tạm; full CPU run chỉ chạy theo lịch, khi phát hành hoặc khi thay dependency/runtime dùng chung.
- Chương `gpu_full: true` cần full report trên GPU; local GPU là evidence kỹ thuật, Colab/Kaggle là portability gate của Beta.
- Không tự đổi status sang `learner_tested` hoặc `published`; hai trạng thái này cần bằng chứng người học thật.

## Báo cáo review

Ghi kết quả vào `_dev/review_log.md`: phạm vi, nguồn đã đối chiếu, commit/CI run, kết quả và giới hạn chưa kiểm chứng. Chạy `python tools/build_review_records.py` để tái tạo bảng 41 chương. Reviewer không được ghi `pass` nếu chỉ kiểm tra việc file tồn tại.

## Quyền sử dụng đóng góp

Bằng việc gửi đóng góp, bạn đồng ý cấp phép code theo MIT và nội dung giáo dục gốc theo CC BY-SA 4.0. Không gửi nội dung bạn không có quyền phân phối.
