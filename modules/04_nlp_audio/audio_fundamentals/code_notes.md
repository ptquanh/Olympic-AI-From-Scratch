# Code Notes: Audio Fundamentals

## 🔑 Core Patterns

```python
import torchaudio
import matplotlib.pyplot as plt

# Đọc file (waveform shape: [channels, time])
waveform, sample_rate = torchaudio.load('speech.wav')

# Chuyển thành MelSpectrogram
transform = torchaudio.transforms.MelSpectrogram(sample_rate=sample_rate)
mel_specgram = transform(waveform)

plt.imshow(mel_specgram.log2()[0,:,:].numpy(), aspect='auto')
plt.show()
```

### 🏋️ Bài Luyện Code Tay

| #   | Bài                                                 | Thời gian | Hint (ẩn)                                                                 |
| --- | --------------------------------------------------- | --------- | ------------------------------------------------------------------------- |
| 1   | Load file .wav và resample về 16kHz bằng torchaudio | 10p       | Dùng `torchaudio.load` và `torchaudio.transforms.Resample`                |
| 2   | Vẽ đồ thị Mel-Spectrogram từ Waveform               | 15p       | Dùng `torchaudio.transforms.MelSpectrogram` và `matplotlib.pyplot.imshow` |

### 🧠 Flashcards

| Hỏi                                                      | Trả lời                                                                                                    |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Sample rate (Tần số lấy mẫu) là gì?                      | Số lượng mẫu (samples) âm thanh được chụp lại trong 1 giây (VD: 16kHz = 16,000 mẫu/giây).                  |
| Tại sao dùng Mel-Spectrogram thay vì Spectrogram thường? | Vì thang đo Mel mô phỏng lại cách tai người cảm nhận âm thanh (nhạy với tần số thấp, kém nhạy tần số cao). |
