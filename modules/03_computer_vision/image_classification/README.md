# Competition Lab — Image Classification

> **Track:** Foundation ⭐ | Contest ⭐

## Learning Outcomes

- Xây pipeline Data → EDA → Split → Train → Validate → Infer → Submit chạy tuần tự.
- Bắt đầu bằng baseline nhỏ, sau đó so sánh CNN/transfer learning trong cùng validation protocol.
- Ngăn leakage giữa ảnh gần trùng, subject/group hoặc augmentation.
- Lưu seed, config, checkpoint và kiểm tra submission contract.

## Problem và dữ liệu

CPU smoke path tạo ảnh `16×16` có hai pattern dọc/ngang cùng noise, nên label có tín hiệu thật và pipeline có thể học được. Đây là test kỹ thuật, không đại diện độ khó dữ liệu thi. Full practice phải thay bằng dataset công khai có license và split rõ.

## Metric

Smoke task cân bằng dùng Accuracy. Khi class imbalance hoặc chi phí lỗi khác nhau, đề có thể dùng Macro F1, log loss hoặc metric riêng. Metric của đề là nguồn quyết định cuối; không đổi threshold dựa trên test labels.

## Validation

- Baseline dùng một hold-out cố định với seed 42.
- Dữ liệu có nhiều ảnh cùng đối tượng phải split theo group trước augmentation.
- Fit normalization/statistics chỉ trên train; augmentation ngẫu nhiên chỉ áp dụng train.
- Dùng validation để chọn model/checkpoint, không dùng test như validation thứ hai.

## Starter và Solution

- `starter.ipynb`: nearest-centroid baseline chạy được và TODO thay bằng CNN.
- `solution.ipynb`: CNN nhỏ, deterministic DataLoader, validation metric và submission array.
- Transfer learning là một lựa chọn khi model/cache được phép, không phải quy tắc bắt buộc. `timm` không thuộc danh sách PTIT 2026 trong PDF nên không được giả định có trong phòng thi.

## Failure Modes

1. Random split làm ảnh cùng source xuất hiện ở train và validation.
2. Normalize/augment validation như train khiến metric không phản ánh inference.
3. Chọn checkpoint theo training loss thay vì metric validation.
4. Submission sai thứ tự sample, dtype, header hoặc số dòng.

## Time Estimate

Starter baseline: ~45m · Improvement: ~2h · Postmortem: ~30m
