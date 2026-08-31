# Speech Recognition (ASR)

> **Track:** Foundation ⚡ | Contest ⭐

## ① Prerequisite Check

Bạn cần giải thích được spectrogram, tokenization và encoder/decoder Transformer. Nếu chưa, học Audio Fundamentals và Transformer.

## ② Learning Outcomes

- Mô tả pipeline waveform → processor → acoustic/language model → decoding → transcript.
- Tính Word Error Rate (WER) và Character Error Rate (CER) bằng edit distance.
- Chuẩn hóa reference/hypothesis nhất quán trước khi chấm.
- Chẩn đoán lỗi âm học, segmentation, decoding và language/domain shift.

## ③ Concept Map

`Audio preprocessing → encoder/CTC hoặc encoder-decoder → decoding → text normalization → WER/CER`

## ④ Intuition

ASR phải ánh xạ hàng nghìn audio frames sang chuỗi token ngắn hơn. CTC cho phép alignment ẩn với blank/repetition; encoder-decoder sinh token tự hồi quy và có thể dùng ngữ cảnh mạnh hơn nhưng decoding tốn thời gian.

## ⑤ Math & Worked Example

`WER = (S + D + I) / N`, với `N` là số word trong reference. Reference “the cat sat on mat”, hypothesis “the bat sat on the mat” có một substitution (`cat→bat`) và một insertion (`the`), nên `WER=2/5=0.4`. WER có thể lớn hơn 1 khi số insertion nhiều.

## ⑧ Framework / Lab

Lab cài edit distance bằng Python và kiểm tra WER/CER offline. Model pretrained chỉ dùng ở full online profile với cache rõ ràng; không tải trong fast/offline path.

## ⑩ Misconceptions

- ❌ **Sai:** WER luôn nằm trong `[0,1]`. → ✅ Insertion có thể làm WER > 1.
- ❌ **Sai:** Lowercase/punctuation chỉ là trình bày. → ✅ Normalization policy thay đổi metric.
- ❌ **Sai:** Split ngẫu nhiên từng clip luôn an toàn. → ✅ Cùng speaker/recording có thể rò rỉ.

## ⑮ Mastery Check

Tính WER bằng tay, nêu normalization policy và thiết kế split theo speaker/domain.

## ⑯ Time Estimate

Theory: ~1.5h · Code: ~1h · Exercises: ~1h
