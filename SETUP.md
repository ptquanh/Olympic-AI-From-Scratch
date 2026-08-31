# Cài đặt môi trường

Repo hỗ trợ ba profile tách biệt để không nhầm môi trường học với môi trường thi.

## 1. Learning CPU

Yêu cầu Python 3.10. Tạo virtual environment hoặc Conda environment, sau đó:

```bash
python -m pip install -r requirements.txt -c constraints-py310.txt
python -m ipykernel install --user --name olympic-ai --display-name "Python (Olympic AI)"
jupyter lab

```

Chạy kiểm tra nhanh:

```bash
python tools/audit_curriculum.py
python tools/run_notebooks.py --fast --profile cpu --offline --repeats 2 --match modules/00_foundations/python_essentials

```

Khi chuẩn bị release, bỏ `--match` để chạy toàn bộ. Trên pull request, CI tự chọn notebook bị ảnh hưởng bằng `--changed-since`; thay đổi chỉ ở Markdown không kích hoạt notebook run.

## 2. Learning GPU

Dùng `environment-gpu.yml` trên máy NVIDIA đã có driver tương thích CUDA 12.8; file dùng official PyTorch wheel index và lock `torch/torchvision/torchaudio` tương thích. Nếu driver/nền tảng khác, lấy đúng lệnh từ selector chính thức của PyTorch rồi cài phần còn lại bằng `requirements.txt` + constraints. Trên Colab/Kaggle, giữ PyTorch/CUDA tương thích do nền tảng cung cấp; không ép CUDA build của máy local. `environment.yml` là profile CPU.

Sau khi tạo environment, kiểm tra trước khi chạy full gate:

```bash
python -c "import torch; print(torch.__version__, torch.cuda.is_available(), torch.cuda.get_device_name(0))"
python tools/run_notebooks.py --profile gpu --gpu-only --offline
python tools/verify_notebook_report.py _dev/notebook_report.json --profile gpu

```

Notebook ghi `gpu_full: true` trong `curriculum.yml` vẫn phải có CPU smoke path. Chạy gate cục bộ bằng `python tools/run_notebooks.py --profile gpu --gpu-only`; evidence Colab/Kaggle phải ghi platform, GPU, phiên bản và report, không chỉ chụp ảnh output.

## 3. Competition-safe

`requirements-contest.txt` chỉ phản ánh danh sách dự kiến trong PDF Olympic AI PTIT 2026, không bảo đảm cho kỳ thi khác hoặc mùa khác. Trong phòng thi:

- dùng environment do ban tổ chức cấp;
- không chạy `pip install`, `conda install` hoặc `git clone`;
- không giả định có Internet hay model ngoài cache;
- kiểm tra đề và thông báo chính thức của đúng tác vụ trước khi dùng thư viện/model.

## Fast mode và network

PowerShell:

```powershell
$env:OAI_FAST_MODE = "1"
jupyter lab

```

Bash:

```bash
OAI_FAST_MODE=1 jupyter lab

```

Fast mode giảm số mẫu/epoch nhưng không được bỏ qua bước Data → Train → Evaluate → Infer. Notebook cần tải dữ liệu/model phải ghi rõ network requirement và đưa ra thông báo hành động được khi cache bị thiếu; không được tự cài package.

## Tái lập

Mỗi notebook đặt seed cho Python, NumPy và framework sử dụng. Seed không bảo đảm kết quả giống từng bit giữa mọi GPU hoặc phiên bản thư viện; runner so sánh numeric output với `rtol=1e-5`, `atol=1e-7` khi dùng `--repeats 2`. `constraints-py310.txt` là lock cho CI/contest-compatible Python 3.10. Report ghi môi trường thực tế nhưng chỉ được giữ như CI/release artifact, không commit vào repository.

Nếu setup không hoạt động, mở issue kèm hệ điều hành, Python, output của `python -m pip freeze`, notebook và traceback đầy đủ.
