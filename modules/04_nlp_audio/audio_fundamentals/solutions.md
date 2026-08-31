# Lời giải: Audio Fundamentals

<details><summary><b>U-1 — Understand</b></summary>

`48000/16000 = 3` giây; `48000/8000 = 6` giây. Samples không mang đơn vị thời gian nếu thiếu sampling rate.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

```python
sr = 16_000
t = np.arange(sr) / sr
x = np.sin(2*np.pi*440*t)
left, right = x[:sr//2], x[sr//2:]
freq = np.fft.rfftfreq(len(left), d=1/sr)
peak = freq[np.abs(np.fft.rfft(left)).argmax()]
assert len(left) == len(right) == 8000
assert abs(peak - 440) <= sr/len(left)

```

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

Với noise `n`, dùng `10*log10(mean(x²)/mean(n²))`. Giữ waveform và noise seed cố định; nhân noise theo từng mức. Khi standard deviation tăng 10 lần, noise power tăng khoảng 100 lần và SNR giảm khoảng 20 dB.

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>
