# Optimization

> **Track:** Foundation ⭐ | Contest 📖

## ① Prerequisite Check

- Gradient Descent hoạt động như thế nào? Learning Rate ($\eta$) đóng vai trò gì?

## ② Learning Outcomes

- Hiểu được sự cải tiến từ SGD ➔ Momentum ➔ RMSProp ➔ Adam/AdamW.
- Setup được bộ Tối ưu (Optimizer) AdamW chuẩn mực trong PyTorch.
- Ứng dụng được các Learning Rate Schedulers (StepLR, CosineAnnealing) để điều chỉnh Learning Rate động.

## ③ Concept Map

Loss Functions ➔ **Optimization** ➔ Regularization ➔ Fine-tuning

## ④ Intuition

Gradient Descent giống như một người mù đang dò đường xuống núi.

- Mới đầu, người đó bước từng bước đều đặn (SGD).
- Sau đó, người đó nhận ra nếu đang lao dốc thì nên lấy "đà" chạy nhanh hơn (Momentum).
- Kế tiếp, người đó phát hiện nếu đường quá gập ghềnh (nhiều sỏi đá), bước chân nên rón rén lại, còn chỗ bằng phẳng thì bước dài ra (RMSProp).
- Adam là sự kết hợp của cả hai: Vừa lấy đà (Momentum), vừa tự điều chỉnh bước chân tùy theo độ gập ghềnh của địa hình (RMSProp).

## ⑤ Math/Derivation

Adam update rule (rất rút gọn):
$m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t$ (Tính đà - Momentum)
$v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2$ (Tính độ gập ghềnh - RMSProp)
$w = w - \eta \frac{m_t}{\sqrt{v_t} + \epsilon}$ (Cập nhật)

## ⑥ Worked Example

Khi train mô hình LLM, 1000 bước đầu tiên người ta tăng dần Learning Rate từ 0 lên mức tối đa (gọi là Warm-up) để mô hình không bị shock. Sau đó, người ta hạ từ từ LR xuống tiệm cận 0 (Cosine Decay) để mô hình len lỏi vào được điểm tối ưu sâu nhất mà không bị văng ra ngoài.

## ⑩ Misconceptions

❌ **Sai:** Chỉ cần gọi `optimizer.step()` là xong.
✅ **Đúng:** PyTorch cộng dồn gradient mặc định. Trong loop thông thường, xóa gradient một lần trước `backward()` của bước mới; vị trí có thể ở đầu hoặc cuối iteration miễn logic nhất quán. Không xóa gradient là chủ ý hợp lệ khi dùng gradient accumulation.

## ⑮ Mastery Check

- Tại sao AdamW lại được ưa chuộng hơn Adam truyền thống?
- Learning Rate Scheduler nên được gọi trước hay sau `optimizer.step()`?

## ⑯ Time Estimate

Theory: ~1h, Code: ~1h, Exercises: ~1h
