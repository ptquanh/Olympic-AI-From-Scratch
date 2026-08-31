# Postmortem: Text Classification Competition

## Kết quả baseline Beta

Dataset nhỏ chứa tín hiệu lexical có thể học được. Solution chạy `Data → EDA → Train → Validate → Infer → Submit` với TF–IDF + Logistic Regression, không phụ thuộc Internet/model hub. Mục tiêu là kiểm pipeline và validation trước khi fine-tune encoder.

## Điều làm đúng

- `TfidfVectorizer` nằm trong pipeline và chỉ fit trên train.
- Split giữ tỷ lệ lớp và seed cố định.
- Macro F1 được ưu tiên khi mỗi lớp quan trọng như nhau.
- Submission giữ ID của test và kiểm schema.

## Failure modes cần kiểm

- Duplicate hoặc near-duplicate đi qua train/validation làm score ảo.
- Normalize quá mạnh làm mất dấu, phủ định, emoji hoặc mã định danh có tín hiệu.
- Vocabulary được fit trên validation/test gây leakage.
- Accuracy cao nhưng lớp hiếm có recall bằng 0.
- Threshold được chọn trực tiếp trên test/public leaderboard.
- Tokenizer/model pretrained thiếu cache khi phòng thi offline.

## Cải tiến hợp lệ

Thử n-gram, character features, class weight và calibrated threshold trước. Chỉ dùng pretrained encoder khi model/revision đã cache, package được profile cho phép và baseline chứng minh đủ thời gian/VRAM. Không có quy tắc “learning rate bắt buộc 1e-5–5e-5” hoặc “luôn dùng PhoBERT”; chọn theo model, dữ liệu và validation.

## Checklist trước nộp

Khởi động kernel sạch, bật offline, chạy lại solution, infer test, assert đúng số dòng/ID/cột/NaN và lưu vectorizer/model/config cùng submission.
