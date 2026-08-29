# Audio Fundamentals

> **Track:** Foundation ⚡ | Contest 📖

## ① Giới thiệu

Máy tính biểu diễn âm thanh như thế nào? Chương này giúp bạn nắm kiến thức nền tảng để tiền xử lý file âm thanh (WAV/MP3).

## ② Learning Outcomes

- Hiểu về Waveform (Dạng sóng) và Sampling Rate (Tần số lấy mẫu).
- Chuyển Waveform thành Spectrogram (Đồ thị phổ âm thanh). Đưa âm thanh về bài toán Thị giác máy tính (CV).

## ④ Intuition

Âm thanh là sự rung động của không khí (áp suất). Micro biến dao động đó thành điện áp. ADC (Analog to Digital Converter) ghi lại mức điện áp đó $N$ lần mỗi giây (VD: Sampling rate 16000Hz nghĩa là đo 16,000 lần/giây). Một file âm thanh 1 giây bản chất chỉ là 1 mảng (vector) gồm 16,000 con số (Waveform).
Biến đổi Fourier (FFT) phân tích sóng này thành các dải tần số thấp, trung, cao. Vẽ lên hình 2D ta được Spectrogram (trục ngang là thời gian, trục dọc là tần số, màu sắc là cường độ). Từ đây, ta dùng CNN/Transformer để xử lý bức ảnh này!

## ⑯ Time Estimate

Theory: ~0.5h, Code: ~0.5h, Exercises: ~0.5h
