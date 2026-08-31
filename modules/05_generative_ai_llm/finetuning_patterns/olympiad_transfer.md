# Olympic transfer: Fine-tuning và LoRA

> **Profile mặc định:** General. Phần cốt lõi dùng LoRA tự cài đặt trong NumPy/PyTorch cơ bản. `peft`, `bitsandbytes`, model hub và tải model là appendix online, **không competition-safe** nếu quy chế không cho phép rõ ràng. Xem [competition profiles](../../../COMPETITION_PROFILES.md).

## Nhận diện trong đề

LoRA đáng cân nhắc khi có model pretrained được cung cấp hợp lệ, full fine-tuning vượt giới hạn VRAM và nhiệm vụ đủ dữ liệu để adaptation có ý nghĩa. Không dùng LoRA chỉ vì đây là kỹ thuật phổ biến; baseline frozen encoder hoặc head tuyến tính có thể rẻ và ổn định hơn.

## Baseline tối thiểu

Với ma trận gốc `W` có shape `(out, in)`, dùng cập nhật `ΔW = scale * B @ A`, trong đó `A: (r, in)`, `B: (out, r)` và `scale = alpha/r`. Assert:

- output giữ shape `(batch, out)`;
- số tham số trainable là `r * (in + out)`;
- khi `B = 0`, output ban đầu bằng linear layer gốc;
- gradient chỉ cập nhật adapter nếu base weight bị freeze.

Notebook framework của chương dùng `LoRALinear` tự viết; không cài package và không tải model.

## Metric và validation

Dùng metric downstream, đồng thời báo trainable parameter count, peak memory và runtime. So sánh LoRA với head-only/full fine-tune trên cùng split; không chọn rank từ test score.

## Failure modes

- Nhầm thứ tự `A/B` hoặc scale khiến shape sai hay update quá lớn.
- Khởi tạo cả `A` và `B` bằng 0 làm gradient ban đầu bị chặn; thường random một ma trận và zero ma trận còn lại.
- Base parameters chưa freeze nên phép so sánh parameter-efficient không còn hợp lệ.
- Rank cao hơn không đảm bảo metric tốt hơn và có thể overfit.
- Adapter không tự chứa base model; artifact thiếu base revision sẽ không tái lập.

## Appendix online: PEFT/QLoRA

Chỉ tham khảo khi learning environment đã cài `peft`/`bitsandbytes`, model đã cache và giấy phép cho phép. Notebook không tự `pip install`, clone hay tải model. Trước thi phải đối chiếu danh sách package/model chính thức của đúng kỳ và năm.

## Timebox

Không áp PTIT 4h/6h cho các kỳ khác. Dùng tỷ lệ của profile: baseline và shape test 15%, train/ablation 60%, error analysis 10%, export–reload–infer 15%.
