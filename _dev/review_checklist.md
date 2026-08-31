# Technical review checklist

## Nội dung

- [ ] Prerequisite cụ thể và link đúng chương.
- [ ] Learning outcomes đo được và có bài đánh giá cùng ID.
- [ ] Ký hiệu được định nghĩa; derivation giải thích từng bước.
- [ ] Worked example xuất hiện trước exercises.
- [ ] Công thức, đáp số và code đã đối chiếu độc lập.
- [ ] Misconceptions phản ánh lỗi thật của người học.

## Notebook

- [ ] Setup cell ghi runtime, hardware, network và competition-safe.
- [ ] `OAI_FAST_MODE=1` chạy CPU từ đầu đến cuối.
- [ ] Notebook có randomness chạy hai lần; numeric outputs nằm trong tolerance đã khai báo.
- [ ] Seed Python/NumPy/framework đầy đủ.
- [ ] Không auto-install, clone repo hoặc dùng absolute path.
- [ ] From-scratch không dùng framework để cài thuật toán.
- [ ] Framework so sánh với reference; experiment có hypothesis và observation.
- [ ] Report chứa SHA-256 khớp notebook hiện tại; report stale không được dùng làm evidence.
- [ ] Chương `gpu_full` thực sự route tensor/module sang CUDA và có full report không bật fast mode.

## Bài tập và nguồn

- [ ] ID và expected output khớp 1–1 với solution.
- [ ] Core có U/I/E/T/O; Concept có U/I/E; Competition có E/T/O qua rubric.
- [ ] Link official docs trỏ đúng API; nguồn có vai trò và ngày truy cập khi cần.
- [ ] Luật thi có profile + năm; không suy rộng từ một kỳ thi.

## Trạng thái

- [ ] Có bằng chứng lệnh kiểm tra trong `review_log.md`.
- [ ] CPU clean environment và Colab/Kaggle GPU được ghi riêng; không dùng local pass để giả làm cloud pass.
- [ ] Chỉ đặt `technically_reviewed` sau khi toàn bộ mục trên pass.
- [ ] Không đặt `published` nếu chưa có learner-test record.
