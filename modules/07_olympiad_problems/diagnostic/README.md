# Diagnostic Contest — 90 phút

Mục tiêu của diagnostic là tìm phần yếu trước khi lao vào đề thật. Không dùng Internet trong 90 phút.

## Bài 1 — Tabular leakage, 25 phút

Lấy notebook `modules/06_competition_pipeline/validation/starter.ipynb`. Trong 25 phút:

1. Nêu group hoặc time key có thể làm split sai.
2. Viết validation đúng hơn random hold-out.
3. Chỉ ra ít nhất một feature có nguy cơ nhìn thấy tương lai.
4. Ghi metric baseline và một thay đổi duy nhất.

**Pass:** giải thích được vì sao validation đáng tin hơn, không chỉ tăng score.

## Bài 2 — Vision debugging, 30 phút

Chọn một notebook CV đã học. Không train model lớn. Hãy tạo checklist để phân biệt 4 lỗi: label sai, normalization sai, overfit, split leakage. Với mỗi lỗi phải có một kiểm tra nhỏ có kết quả quan sát được.

**Pass:** có thể chạy hoặc mô tả chính xác fixture tối thiểu để xác nhận từng giả thuyết.

## Bài 3 — NLP/retrieval strategy, 25 phút

Giả sử có 5.000 đoạn văn và 100 query, metric là Recall@5. Trong 25 phút:

1. Chọn lexical, dense hoặc hybrid baseline.
2. Viết kế hoạch validation.
3. Nêu hai failure mode.
4. Đề xuất một ablation có thể hoàn thành trong 10 phút.

**Pass:** quyết định gắn với metric và giới hạn thời gian.

## Postmortem, 10 phút

Ghi ba lỗ hổng lớn nhất và map ngược về chapter trong Module 00–06. Chỉ bắt đầu đề thật sau khi có kế hoạch sửa ít nhất một lỗ hổng.
