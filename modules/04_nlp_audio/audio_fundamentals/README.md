# Audio Fundamentals

> **Track:** Foundation ⚡ | Contest 📖

## ① Prerequisite Check

Bạn cần hiểu array, sampling và sin/cos cơ bản. Nếu chưa, đọc NumPy và Math Essentials.

## ② Learning Outcomes

- Tính duration từ số sample và sampling rate; phân biệt mono/stereo.
- Giải thích frame, hop length, STFT, magnitude và spectrogram.
- Resample/crop/pad mà không làm lệch label hoặc đơn vị thời gian.
- Chọn augmentation phù hợp và kiểm tra nó không phá semantic.

## ③ Concept Map

`Waveform → framing/STFT → spectrogram/features → audio encoder → classification/ASR`

## ④ Intuition

Waveform cho biết amplitude theo thời gian nhưng không trực tiếp cho biết tần số xuất hiện lúc nào. STFT chia tín hiệu thành cửa sổ ngắn, áp Fourier transform cho từng cửa sổ và tạo time–frequency representation.

## ⑤ Math & Worked Example

Tín hiệu 16,000 samples ở 16 kHz dài đúng 1 giây. Với frame length 400 và hop 160, số frame không padding là `1 + floor((16000-400)/160) = 98`. Shape spectrogram còn phụ thuộc số frequency bins, thường `n_fft/2+1` cho real FFT.

## ⑧ Framework / Lab

Lab tạo waveform tổng hợp để quan sát sampling và metric mà không tải file. Full dataset phải ghi license, sampling rate, channel policy và cache.

## ⑩ Misconceptions

- ❌ **Sai:** Hai file cùng số samples có cùng duration. → ✅ Còn phụ thuộc sampling rate.
- ❌ **Sai:** Normalize từng file luôn tốt. → ✅ Có thể xóa thông tin loudness có ích.
- ❌ **Sai:** Time shift luôn giữ label. → ✅ Không đúng với task định vị sự kiện chính xác.

## ⑮ Mastery Check

Tính đúng shape/duration và giải thích được mỗi preprocessing step thay đổi tín hiệu gì.

## ⑯ Time Estimate

Theory: ~1h · Code: ~1h · Exercises: ~1h
