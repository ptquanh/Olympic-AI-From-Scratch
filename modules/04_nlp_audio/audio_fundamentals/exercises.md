# Bài tập: Audio Fundamentals

## Tầng 1: Understand

Nếu bạn có một mảng numpy độ dài 48,000 biểu diễn âm thanh với sample rate là 16,000 Hz, file âm thanh này dài bao nhiêu giây?

## Tầng 2: Implement

**Mục tiêu:** Code các phép biến đổi Audio.

- Dùng `torchaudio`. Load 1 file audio mẫu.
- Viết code cắt file audio đó thành 2 phần bằng nhau (theo độ dài mẫu).
- Chuyển 1 nửa thành Spectrogram.

## Tầng 3: Experiment

**Mục tiêu:** Data Augmentation cho Audio.

- Viết code thêm nhiễu trắng (White Gaussian Noise) vào waveform.
- Chuyển cả bản gốc và bản có nhiễu sang Mel-Spectrogram và plot lên để xem sự khác biệt.
