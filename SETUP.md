# Hướng dẫn Cài đặt Môi trường (Conda)

> Để đảm bảo các file code và notebook trong khóa học chạy đúng mà không bị lỗi phiên bản thư viện, bạn nên cài đặt môi trường Conda theo hướng dẫn dưới đây.

## Dành cho Local (Máy tính cá nhân)

1. **Cài đặt Miniconda**
   Nếu máy bạn chưa có Conda, tải và cài đặt [Miniconda](https://docs.conda.io/en/latest/miniconda.html) phù hợp với hệ điều hành của bạn (Windows / macOS / Linux).

2. **Tạo môi trường từ file `environment.yml`**
   Mở Terminal (hoặc Anaconda Prompt trên Windows), điều hướng đến thư mục gốc của repository này và chạy:

   ```bash
   conda env create -f environment.yml
   ```

   _Lưu ý:_ Nếu máy bạn KHÔNG có card đồ họa NVIDIA (hoặc dùng Mac), hãy mở file `environment.yml` và xóa/comment dòng `- pytorch-cuda=12.1` trước khi chạy lệnh tạo môi trường.

3. **Kích hoạt môi trường**

   ```bash
   conda activate olympic-ai
   ```

   _(Tùy chọn) Nếu bạn không dùng Conda mà dùng Python ảo (`venv`), bạn có thể cài đặt thông qua `requirements.txt`:_

   ```bash
   pip install -r requirements.txt
   ```

4. **Đăng ký môi trường với Jupyter**

   ```bash
   python -m ipykernel install --user --name olympic-ai --display-name "Python (Olympic AI)"
   ```

5. **Mở Jupyter Lab**
   ```bash
   jupyter lab
   ```
   Sau khi Jupyter Lab mở ra trên trình duyệt, hãy đảm bảo bạn chọn Kernel là `Python (Olympic AI)` cho các notebook.

## Dành cho Google Colab / Kaggle

Các nền tảng này đã cài sẵn hầu hết các thư viện cần thiết. Khóa học đã chuẩn hóa Cell đầu tiên (Setup Cell) của tất cả Notebooks để tự động nhận diện và xử lý các thiết lập môi trường đặc thù của từng nền tảng, bạn chỉ việc bấm `Run All`!
