# Contest Toolkit — stack và checklist thi đấu

File này không thêm framework mới. Mục tiêu là thống nhất những gì đội cần kiểm tra trước và trong contest.

## 1. Environment

- Environment và package: xem `docs/SETUP.md` và profile đúng mùa trong `docs/COMPETITION_PROFILES.md`.
- Notebook workflow: `../06_competition_pipeline/jupyterlab_workflow/`.
- Reproducibility: `../06_competition_pipeline/experiment_tracking/`.

Trước thi phải biết cách: kiểm tra GPU, xem dung lượng đĩa/RAM, restart kernel, chạy notebook từ đầu và xác định package có sẵn. Không cài thêm package nếu luật không cho phép.

## 2. Baseline stack

- EDA: `../06_competition_pipeline/eda/`.
- Validation: `../06_competition_pipeline/validation/`.
- Debugging: `../06_competition_pipeline/debugging_ml/`.
- Ensemble: `../06_competition_pipeline/ensembling/`.

Nguyên tắc: baseline end-to-end trước, rồi mới tăng độ phức tạp.

## 3. Submission gate

Trước mỗi submission quan trọng:

- đúng tên file và schema;
- đúng số dòng / ID / order;
- không NaN hoặc giá trị ngoài miền cho phép;
- inference dùng đúng checkpoint/config;
- runtime nằm trong giới hạn;
- có thể tái tạo từ notebook/script sạch.

## 4. Emergency playbook

| Sự cố                                   | Hành động đầu tiên                                                                   |
| --------------------------------------- | ------------------------------------------------------------------------------------ |
| OOM                                     | giảm batch/input size, tắt cache không cần thiết, quay về baseline đã chạy           |
| Kernel chết                             | mở notebook baseline sạch, không cố phục hồi state ẩn                                |
| Score local tăng nhưng leaderboard giảm | kiểm tra split/leakage/distribution shift trước khi tuning tiếp                      |
| Không kịp train                         | dùng checkpoint tốt nhất đã xác nhận và ưu tiên inference/submission                 |
| Submission sai                          | dừng experiment mới, sửa schema/path/order và tạo file tối thiểu hợp lệ              |
| Hai máy tranh cùng GPU                  | chỉ một job GPU tại một thời điểm; máy còn lại làm EDA, review, report hoặc CPU work |

## 5. Freeze rule

Khi còn khoảng 10–15% thời gian: ngừng experiment rủi ro, chọn candidate đã tái lập được, rerun sạch, kiểm tra output và để một thành viên khác review artifact cuối.
