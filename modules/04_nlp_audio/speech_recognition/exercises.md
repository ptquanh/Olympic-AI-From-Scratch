# Bài tập: Speech Recognition

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

Reference “mẹ đi chợ mua rau”, hypothesis “mẹ đi chợ rau”. Xác định edit operation và WER.

**Kết quả mong đợi:** Một deletion trên năm reference words, WER `1/5 = 0.2`.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

Tự viết Levenshtein distance và `wer(reference,hypothesis)` theo word tokens. Xử lý reference rỗng bằng lỗi rõ ràng.

**Kết quả mong đợi:** Ví dụ trên trả 0.2; identical strings trả 0; insertion-only case có thể trả WER lớn hơn 1.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

So sánh WER trước/sau ba normalization policy: lowercase, bỏ punctuation và chuẩn hóa số. Dùng ít nhất năm cặp transcript cố định.

**Kết quả mong đợi:** Bảng policy–WER và ví dụ lỗi; nêu policy nào hợp lệ theo evaluation contract thay vì chọn policy chỉ vì score thấp.
