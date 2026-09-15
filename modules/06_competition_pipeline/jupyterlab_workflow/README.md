# JupyterLab Workflow — Kernel sạch và bài nộp tái lập

> **Loại:** Concept Lesson
> **Track:** Foundation ⭐ | Contest ⭐
> **Thời gian học ước tính:** 3 giờ (theory: 0.75h, code: 1.25h, exercises: 1h)
> **Profile mặc định:** general · CPU · offline · dữ liệu mô phỏng tự tạo.
> **Trạng thái:** technically_reviewed; chưa có learner testing. Xem [manifest](../../../curriculum.yml).

## Prerequisite Check

1. Biến nằm trong RAM hay được lưu trong file notebook?
2. Đường dẫn tương đối được tính từ thư mục nào?
3. Đóng tab notebook có chắc dừng kernel không?

Nếu chưa trả lời được, quay lại [Python Essentials](../../00_foundations/python_essentials/README.md) và [Regex & Data Handling](../../00_foundations/regex_data_handling/README.md).

## Learning Outcomes

- [ ] LO1: Phân biệt document, kernel, terminal và working directory.
- [ ] LO2: Khôi phục pipeline từ artifact sau khi xóa state trong RAM.
- [ ] LO3: Thực hiện Restart & Run All và kiểm tra file nộp từ disk.

## Concept Map

```text
Python Essentials + Regex & Data Handling → JupyterLab Workflow → Experiment Tracking
                              └→ baseline chạy lại được trong phòng thi
```

## 1. Intuition — Tại sao cần?

Notebook có output đẹp nhưng chỉ chạy được vì biến còn sót từ hôm trước. Document là các cell được lưu trên disk; kernel là tiến trình giữ biến trong RAM; terminal là shell riêng. Đóng tab không đồng nghĩa dừng kernel. Bài nộp cần chạy theo thứ tự từ state sạch.

## 2. Math & Derivation

Chương thao tác nên không derive thuật toán học mới. Mô hình phụ thuộc: state_(k+1)=cell_k(state_k, files). Muốn replay được, mọi input của cell phải đến từ setup, cell phía trước hoặc file được khai báo. Artifact contract gồm tên file, schema, số dòng, kiểu dữ liệu và version. Kiểm tra n_output=n_test là điều kiện cần; ID và thứ tự cũng phải khớp.

## 3. Worked Example

Cell A đặt scale=2. Cell B tính y=scale·[1,3]=[2,6]. Nếu sửa A thành 3 nhưng không chạy lại, B vẫn cho [2,6], còn Restart & Run All cho [3,9]. Bài học: output lưu sẵn không chứng minh source hiện tại đúng. Lab lưu mean/std/weight vào NPZ, xóa biến model, đọc lại và assert predictions bằng trước khi xóa.

## 4. Shape Analysis

Feature `(n,2)`, mean/std/weight `(2,)`, bias scalar, submission `(n_test,2)` với cột id/label. JSON giữ schema/config, NPZ giữ array; không phụ thuộc absolute path.

## 5. Complexity

Restart mất toàn bộ RAM của kernel và cần chạy lại tính toán. Checkpoint (trạng thái lưu trên disk) giúp khôi phục nhưng chỉ đúng khi source/config/split cùng phiên bản. Lab CPU nhỏ; không cần GPU.

## Thao tác JupyterLab cần tự thực hành

1. Mở notebook, chọn kernel đúng môi trường trong [SETUP](../../../docs/SETUP.md). Kiểm tra `sys.executable` và `Path.cwd()` trong cell riêng; không ghi absolute path vào source.
2. Chạy cell bằng Shift+Enter; dùng chế độ edit cho nội dung, command mode để thao tác cell. Save document sau khi sửa.
3. Dùng Kernel → Interrupt khi cell quá lâu. Nếu state khó xác định, dùng Restart Kernel and Run All Cells, kiểm tra từ cell đầu đến CSV cuối.
4. Mở Running panel để xem kernel/terminal còn hoạt động; shutdown kernel không còn dùng. Đóng tab có thể vẫn giữ kernel chạy.
5. Mở Launcher → Terminal để kiểm tra file output hoặc tiến trình. Python trong terminal có thể khác Python của kernel.
6. Trên máy có NVIDIA GPU và tiện ích được cài sẵn, xem `nvidia-smi` trong terminal: memory dùng/còn, utilization và PID. Nếu không có lệnh hoặc không có GPU, tiếp tục CPU lab. Không kết luận GPU memory đầy là model đang tiến bộ; tìm kernel dư và giảm batch khi thực sự OOM.

Không có bước cài package hoặc gọi GPU trong notebook này. Kiểm tra thao tác UI và GPU monitoring là bài tự làm, tách khỏi kiểm tra code CPU tự động.

## 6. From-Scratch & Framework

Không tạo bộ ba notebook Core vì đây là Concept Lesson. Các phép tính nhỏ trong worked example được đối chiếu bằng code; trọng tâm là dùng và debug pipeline. Thực hành theo [lab.ipynb](lab.ipynb). Notebook tự đủ setup/data, không cần chạy chương khác trước.

Lab có code chạy hoàn chỉnh xen câu hỏi dự đoán; làm bài tập riêng trước khi mở đáp án. Dùng thư viện có sẵn trong [environment](../../../envs/requirements.txt), thuộc nhóm được liệt kê trong rules; quyền dùng trong kỳ thi cụ thể lấy từ [competition profile](../../../docs/COMPETITION_PROFILES.md). Không tự cài package hay tải dữ liệu.

## 7. Experiments — Predict → Run → Explain

Dự đoán điều gì còn tồn tại sau `del` các biến model. Lab chứng minh reload cho predictions giống nhau. Sau đó tự thực hiện thao tác UI Restart Kernel and Run All Cells: đây là bài thực hành người học, không được coi tự động là đã kiểm thử UI.

Ghi theo năm bước: **Hypothesis → Code → Result → Observation → Why**. Result phải là số/plot thực chạy; Observation phân biệt bằng chứng và giả thuyết. Mọi plot cần title, axis labels và legend. Kết quả synthetic chỉ minh họa cơ chế, không dự báo leaderboard.

## 8. Common Mistakes & Misconceptions

> ❌ **Sai:** Save notebook là save model.
> ✅ **Đúng:** Save lưu cell/output; array và model trong RAM phải được xuất riêng.

> ❌ **Sai:** Đóng tab là giải phóng GPU.
> ✅ **Đúng:** Kernel có thể còn chạy; mở Running panel để shutdown đúng tiến trình.

> ❌ **Sai:** Terminal dùng cùng Python với kernel.
> ✅ **Đúng:** Có thể khác môi trường; kiểm tra sys.executable ở notebook và python ở terminal.

## 9. Code Notes

Đọc [code_notes.md](code_notes.md), đóng tài liệu rồi làm ít nhất hai bài code tay. Tự kiểm tra bằng assert trước khi so reference.

## 10. Exercises

Làm [exercises.md](exercises.md) theo tầng Understand, Implement, Experiment. Đáp án có thể mở riêng từng bài tại [solutions.md](solutions.md).

## 11. Olympiad Transfer & Connections

Khi đề yêu cầu pipeline có thể chạy lại hoặc cung cấp notebook starter, áp dụng chương này trước khi tăng độ phức tạp model. Baseline tối thiểu là chạy notebook và kiểm tra file nộp; dành khoảng 15–20 phút sau khi đã chuẩn bị môi trường. Nếu notebook chạy khi bấm cell riêng nhưng fail sau restart, tìm biến dùng trước định nghĩa hoặc file phụ thuộc chưa tạo. Không sửa bằng cách chạy ngẫu nhiên các cell.

Sau baseline: (1) xác nhận data/split/metric; (2) thử một giả thuyết có log; (3) đóng băng phương án và chạy lại inference. Profile general dùng khoảng 10% thời gian đọc đề/EDA, 20% baseline, 50% thí nghiệm, 20% kiểm tra và nộp. Đây là gợi ý luyện tập, không phải lịch chính thức 4h/6h của bất kỳ kỳ thi nào.

## 12. References

Nguồn cho API, phương pháp và bài đọc mở rộng nằm trong [references.md](references.md). Quy chế hiện hành luôn ưu tiên thông báo đúng mùa thi.

## 13. Mastery Check

- [ ] Explain: giải thích worked example mà không mở tài liệu.
- [ ] Debug: tạo và phát hiện một lỗi trong phần misconceptions.
- [ ] Apply: hoàn thành lab, lưu kết quả và làm bài I-1 trên notebook trống.

Đạt tối thiểu 2/3 gate; nếu chưa pass Apply thì làm lại lab trước khi chuyển chương.

## 14. Time Estimate

Theory: ~0.75h; Code: ~1.25h; Exercises: ~1h. Runtime notebook: thường dưới 1 phút trên CPU cho fast mode, dự trù dưới 2 phút chế độ đầy đủ trên máy học tập/Colab CPU; đây là ước lượng, không phải benchmark Colab đã đo. Ghi thời gian học thực tế để phản hồi learner testing.

[← Module 06](../MODULE_README.md)
