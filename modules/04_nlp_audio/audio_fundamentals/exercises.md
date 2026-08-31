# Bài tập: Audio Fundamentals

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

Waveform có 48,000 samples ở 16 kHz dài bao nhiêu giây? Nếu cùng samples nhưng metadata ghi 8 kHz thì duration thay đổi thế nào?

**Kết quả mong đợi:** Dùng `duration = samples / sample_rate`, lần lượt được 3 và 6 giây.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

Tạo sine 440 Hz dài 1 giây ở 16 kHz. Chia thành hai nửa và dùng `np.fft.rfft` tìm frequency bin có magnitude lớn nhất.

**Kết quả mong đợi:** Hai đoạn 8,000 samples; peak frequency xấp xỉ 440 Hz trong sai số một FFT bin.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

Thêm Gaussian noise ở ba mức chuẩn `0.01, 0.1, 0.5`; tính SNR và so sánh spectrum peak/noise floor.

**Kết quả mong đợi:** Bảng noise level–SNR–peak; SNR giảm và noise floor tăng khi noise mạnh hơn.
