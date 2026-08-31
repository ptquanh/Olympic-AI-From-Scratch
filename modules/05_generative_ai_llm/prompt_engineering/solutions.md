# Lời giải: Prompt Engineering

<details><summary><b>U-1 — Understand</b></summary>

1. Đây là few-shot/in-context learning: prompt đưa các cặp input–output rồi yêu cầu hoàn tất cùng mẫu.
2. Với **profile PTIT 2026** được nêu trong bài, 5.000 dòng vượt xa ngân sách 2.000 token/phiên, làm mất phần ngữ cảnh quan trọng và tạo output khó kiểm thử. Không được suy diễn giới hạn này sang VOAI/IOAI.
3. Prompt thứ hai tốt hơn vì khóa framework, kiến trúc và dataset, nhưng vẫn thiếu metric, split, hardware và output contract. Một prompt tốt hơn nữa phải nêu các ràng buộc đó.

Kiểm tra tối thiểu bằng một contract thuần Python:

```python
required = {"task", "constraints", "output_format", "tests"}
prompt_spec = {
    "task": "viết training loop ResNet18/CIFAR-10",
    "constraints": "offline, 8 GB VRAM, seed=42",
    "output_format": "một hàm Python",
    "tests": "assert logits.shape == (batch, 10)",
}
assert required <= prompt_spec.keys()

```

**Lỗi thường gặp:** gọi mọi prompt có ví dụ là Chain-of-Thought; quên nêu profile; tin output chỉ vì code có vẻ hợp lý.

</details>

<details><summary><b>I-1 — Implement</b></summary>

Không cần yêu cầu mô hình tiết lộ suy luận nội bộ dài. Yêu cầu lời giải ngắn có các giả định và phép kiểm tra là đủ:

```text
Giải bài toán: "Có 5 con ếch trên lá, 3 con quyết định nhảy".
Nêu giả định về từ "quyết định", đưa đáp án, rồi kiểm lại đáp án trong tối đa 3 câu.

```

Prompt trích xuất có schema và cách xử lý thiếu dữ liệu:

```text
Trích xuất từ TEXT thành đúng một JSON object theo schema:
{"name": string|null, "age": integer|null, "phone": string|null}.
Không thêm markdown. Không suy đoán trường bị thiếu. TEXT: {{text}}

```

Có thể kiểm output offline:

```python
import json
result = json.loads('{"name":"An","age":17,"phone":null}')
assert set(result) == {"name", "age", "phone"}
assert result["age"] is None or isinstance(result["age"], int)

```

**Lỗi thường gặp:** chỉ nói “trả JSON” nhưng không cho schema; không định nghĩa giá trị thiếu; đưa dữ liệu nhạy cảm vào dịch vụ ngoài.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

Tạo trước một tập 20–50 câu có nhãn và một parser output. Chạy zero-shot và few-shot trên **cùng** model/version, temperature và dữ liệu; lặp ít nhất hai lần. Báo accuracy/Macro F1, tỷ lệ JSON parse được, latency và token usage. Ví dụ phần chấm offline:

```python
from sklearn.metrics import f1_score

y_true = ["pos", "neg", "neu", "pos"]
zero = ["pos", "neg", "pos", "pos"]
few = ["pos", "neg", "neu", "pos"]
assert f1_score(y_true, few, average="macro") >= f1_score(y_true, zero, average="macro")

```

Kết luận chỉ có hiệu lực cho model/version và tập test đã ghi. Few-shot có thể cải thiện format nhưng cũng có thể gây bias theo ví dụ; không được tuyên bố luôn tốt hơn.

**Lỗi thường gặp:** đổi đồng thời model/temperature; chấm bằng vài ví dụ thuận lợi; ghi API key vào notebook; gọi API khi competition profile không cho phép.

</details>
