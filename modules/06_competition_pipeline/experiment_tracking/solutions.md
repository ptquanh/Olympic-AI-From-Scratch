# Solutions: Experiment Tracking — Ghi lại để tái lập quyết định

Chỉ mở sau khi tự làm; đối chiếu cả hành vi và lý do.

## U-1

<details><summary>Mở lời giải</summary>

Seed điều khiển randomness; hai hash xác định nội dung config và data theo schema byte đã chọn.

**Kết quả cần kiểm tra:** Nêu đúng ba vai trò; không tuyên bố hash chứng minh chất lượng hoặc seed đảm bảo mọi hardware.

**Lỗi thường gặp:** Seed=42 bảo đảm mọi máy ra cùng bit. Còn phụ thuộc environment/hardware; lưu versions và tolerance.

</details>

## I-1

<details><summary>Mở lời giải</summary>

Dùng canonical JSON, cố định split ngoài loop; xem code pattern và lab.

**Kết quả cần kiểm tra:** 3 run_id khác nhau; split giữ nguyên; có đủ metric/runtime/versions và pipeline reload.

**Lỗi thường gặp:** Chỉ cần lưu best score. Cần cả config, split, dữ liệu, code version và preprocessing để giải thích/replay.

</details>

## E-1

<details><summary>Mở lời giải</summary>

Hai cấu hình khác nhau có thể cùng predictions; hash theo config vẫn phải phân biệt chúng.

**Kết quả cần kiểm tra:** Replay probability allclose; C đổi làm config hash đổi; không yêu cầu metric bắt buộc đổi.

**Lỗi thường gặp:** Hash giống nhau nghĩa là model tốt. Hash xác định nội dung; chất lượng vẫn cần validation đúng.

</details>

## Code đối chiếu chạy độc lập

```python
import json
from hashlib import sha256
def config_hash(config):
    """Return a content hash for a JSON-serializable configuration."""
    payload = json.dumps(config, sort_keys=True, separators=(',', ':'))
    return sha256(payload.encode('utf-8')).hexdigest()
assert config_hash({'C': 1.0, 'seed': 42}) == config_hash({'seed': 42, 'C': 1.0})
assert config_hash({'C': 1.0}) != config_hash({'C': 0.1})
```

Để tái hiện toàn bộ pipeline và số đo, chạy [lab.ipynb](lab.ipynb). Các phép thử không bắt buộc phương án cải tiến phải thắng baseline.
