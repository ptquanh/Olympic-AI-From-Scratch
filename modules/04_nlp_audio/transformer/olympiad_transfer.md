# Olympic transfer: Transformer

> **Profile mặc định:** General. Model pretrained, Internet và Hugging Face không được coi là có sẵn. Xem [competition profiles](../../../COMPETITION_PROFILES.md).

## Nhận diện trong đề

Transformer phù hợp với dữ liệu chuỗi hoặc token khi quan hệ xa quan trọng. Với dữ liệu ít, giới hạn thời gian ngắn hoặc không có model cache, TF–IDF + linear model là baseline NLP bắt buộc trước khi fine-tune encoder.

## Baseline tối thiểu

- Offline/general: tokenizer xác định, vocabulary cố định, encoder nhỏ hoặc TF–IDF baseline.
- Learning online: `AutoTokenizer`/`AutoModel...` chỉ sau khi khai báo model ID, revision, cache và phương án mất mạng.
- Contest: chỉ dùng model/package đã được profile cho phép và chuẩn bị trước; notebook không tải ngầm.

Mọi pipeline phải assert `input_ids.shape == attention_mask.shape`, kiểm padding mask và chạy được infer trên một batch trước khi train.

## Metric và validation

- Classification: Macro F1 khi lệch lớp; thêm confusion matrix.
- Translation: BLEU hoặc chrF, nêu tokenizer/casing.
- Summarization: ROUGE, kèm ví dụ lỗi định tính.
- Không fit tokenizer, scaler hoặc chọn threshold trên test/private data.

## Failure modes

- Padding/causal mask sai làm mô hình dùng thông tin không hợp lệ.
- Learning rate quá lớn có thể phá trọng số pretrained; không có một ngưỡng như `5e-5` đúng cho mọi model/batch.
- Cắt chuỗi làm mất phần chứa tín hiệu; chọn `max_length` từ train/validation distribution.
- OOM do sequence dài; giảm batch/length trước khi đổi kiến trúc.
- Model cache thiếu khi offline; fail sớm với thông báo chỉ cách chuẩn bị cache.

## Sau baseline

So sánh từng cải tiến trên cùng split: pooling, max length, class weights, layer freezing, learning rate. Pretrained model không “luôn thắng”; quyết định bằng validation và runtime. Lưu checkpoint tốt nhất theo metric công bố, không theo test leaderboard.

## Timebox

Không áp mặc định “chung kết 6 giờ”. Dùng tỷ lệ: 15% EDA/baseline, 55% train có kiểm soát, 15% error analysis, 15% infer và kiểm submission; điều chỉnh theo profile chính thức.
