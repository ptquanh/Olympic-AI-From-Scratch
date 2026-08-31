# Code Notes: Prompt Engineering

> API và quyền dùng LLM phụ thuộc provider/profile. Phần cốt lõi dưới đây chỉ tạo, kiểm và chấm prompt offline; không gọi dịch vụ ngoài.

## 🔑 Core Patterns

### Pattern 1: Prompt contract

```python
contract = {
    "task": "phân loại sentiment",
    "labels": ["positive", "negative"],
    "input": "Sản phẩm này tốt",
    "output_schema": {"sentiment": "label", "confidence": "float[0,1]"},
    "constraints": ["không thêm markdown", "không suy đoán trường thiếu"],
}
required = {"task", "input", "output_schema", "constraints"}
assert required <= contract.keys()

```

Tách nhiệm vụ, input, ràng buộc và output schema giúp test được prompt mà không phụ thuộc cú pháp SDK đang thay đổi.

### Pattern 2: Parse và validate output

```python
import json

raw = '{"sentiment":"positive","confidence":0.82}'
result = json.loads(raw)
assert result["sentiment"] in {"positive", "negative"}
assert 0.0 <= float(result["confidence"]) <= 1.0

```

Prompt không bảo đảm JSON hợp lệ. Parser/schema validation và retry policy phải nằm trong code; không dùng `eval` trên output của model.

### Pattern 3: Evaluation harness

```python
gold = ["positive", "negative", "positive"]
pred = ["positive", "positive", "positive"]
accuracy = sum(a == b for a, b in zip(gold, pred)) / len(gold)
assert accuracy == 2 / 3

```

So sánh zero-shot/few-shot trên cùng model version, temperature, test set và parser. Ghi cả metric, tỷ lệ parse thành công, latency và token usage.

## 📋 API Cheat Sheet

| Thành phần    | Câu hỏi kiểm tra                                  |
| ------------- | ------------------------------------------------- |
| Task          | Động từ và phạm vi có rõ không?                   |
| Context       | Chỉ đưa dữ liệu cần thiết, không chứa secret/PII? |
| Constraints   | Ngôn ngữ, độ dài, tool và profile đã khóa?        |
| Output schema | Parser có kiểm type/range/missing field?          |
| Examples      | Bao phủ edge case, không làm lộ nhãn test?        |
| Evaluation    | Có gold set và metric tái lập được?               |

## 🏋️ Bài Luyện Code Tay

1. Viết prompt contract cho trích xuất tên/tuổi/điện thoại; định nghĩa `null` khi thiếu.
2. Viết parser JSON và năm test: hợp lệ, thiếu field, sai type, ngoài range, có markdown thừa.
3. Lập bảng ablation zero-shot/few-shot; chỉ thay một yếu tố mỗi lần.

## 🧠 Flashcards

| Hỏi                                     | Trả lời                                                                      |
| --------------------------------------- | ---------------------------------------------------------------------------- |
| In-context learning là gì?              | Điều chỉnh hành vi từ context/ví dụ trong prompt mà không cập nhật trọng số. |
| Zero-shot và few-shot khác gì?          | Few-shot thêm ví dụ input–output; không bảo đảm luôn tốt hơn.                |
| Prompt tốt có loại hallucination không? | Không. Cần grounding, validation, tests và cơ chế từ chối/fallback.          |
| Có được dùng LLM trong Olympic không?   | Chỉ khi quy chế đúng kỳ, năm và giai đoạn cho phép rõ ràng.                  |
