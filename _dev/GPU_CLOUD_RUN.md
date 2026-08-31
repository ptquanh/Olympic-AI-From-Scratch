# Colab/Kaggle GPU portability gate

Trạng thái Beta 2026-08-31: **pending**. Local CUDA report không được đổi tên thành cloud evidence.

## Cách tạo evidence hợp lệ

1. Checkout đúng commit trên Colab hoặc Kaggle GPU runtime.
2. Giữ PyTorch/CUDA do platform cung cấp; cài dependency khai báo, không sửa notebook.
3. Chạy:

```bash
python tools/audit_curriculum.py --strict-git
python tools/run_notebooks.py --profile gpu --gpu-only --offline --timeout 300 --report _dev/gpu_cloud_report.json
python tools/verify_notebook_report.py _dev/gpu_cloud_report.json --profile gpu

```

4. Report phải chứa `cuda_available: true`, tên GPU, kernel Python/package versions, `fast_mode: false`, 19/19 notebook pass và SHA-256 khớp commit. Lưu report như run/release artifact; không commit JSON vào repo.
5. Ghi platform, runtime image/date và link job/notebook vào review log. Không commit token, credential, cache hay checkpoint.

Khi report hợp lệ có mặt, chạy `python tools/promote_reviewed_statuses.py --apply`; 10 chương GPU mới đủ điều kiện chuyển khỏi `drafted`.
