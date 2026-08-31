# Competition Lab — Text Classification

> **Track:** Foundation ⭐ | Contest ⭐

## Learning Outcomes

- Xây pipeline Split → Vectorize/Tokenize → Train → Macro F1 → Infer → Submit.
- Tạo TF-IDF + linear baseline trước khi fine-tune encoder.
- Ngăn vocabulary, duplicate, author/thread hoặc temporal leakage.
- Phân tích confusion/error slices và chọn threshold trên validation.

## Problem và dữ liệu

CPU smoke path dùng câu sentiment nhỏ, deterministic và không tải mạng. Nó kiểm tra data contract chứ không mô phỏng đầy đủ toxic-comment data. Full practice phải ghi nguồn/license, language, label policy và class distribution.

## Metric

Lab dùng Macro F1: tính F1 riêng từng class rồi lấy trung bình không trọng số. Metric này không tự động là lựa chọn đúng cho mọi task; luôn theo định nghĩa chính xác trong đề, gồm averaging và label order.

## Validation

- Fit vocabulary/TF-IDF chỉ trên train fold.
- Group split theo author/thread/source khi các mẫu liên quan.
- Deduplicate trước split hoặc giữ duplicate trong cùng group.
- Chọn threshold/checkpoint trên validation; khóa pipeline trước test/private inference.

## Starter và Solution

- `starter.ipynb`: keyword baseline chạy được, có Macro F1 và submission contract.
- `solution.ipynb`: TF-IDF bigram + Logistic Regression, phù hợp CPU/offline.
- BERT/PhoBERT là bước cải thiện khi cache, compute và luật cho phép; không phải baseline bắt buộc.

## Failure Modes

1. Fit tokenizer/vectorizer trên toàn bộ dữ liệu.
2. Accuracy cao do class majority nhưng Macro F1 thấp.
3. Truncation cắt mất phần chứa tín hiệu.
4. Text normalization xóa emoji, dấu câu hoặc casing có ích.

## Time Estimate

Starter baseline: ~45m · Improvement: ~2h · Postmortem: ~30m
