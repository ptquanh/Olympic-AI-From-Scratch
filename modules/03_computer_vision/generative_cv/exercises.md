# Bài tập: Generative CV

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

So sánh mục tiêu huấn luyện của GAN discriminator và diffusion noise-predictor. Nêu input, target và ít nhất một failure mode của mỗi hướng.

**Kết quả mong đợi:** Phân biệt adversarial classification với denoising objective; không mô tả hai loss như cùng một bài toán.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

Viết `q_sample(x0, noise, alpha_bar)` theo công thức `sqrt(alpha_bar)x0 + sqrt(1-alpha_bar)noise`. Test hai biên `alpha_bar=1` và `alpha_bar=0`, giữ nguyên shape/dtype.

**Kết quả mong đợi:** Code NumPy chạy được; biên 1 trả `x0`, biên 0 trả `noise`, output cùng shape input.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

Với cùng `x0` và cùng noise seed, chạy `alpha_bar ∈ {0.9, 0.5, 0.1}`. Báo MSE giữa `x_t` và `x0`, rồi giải thích trend.

**Kết quả mong đợi:** Bảng ba cấu hình; MSE nhìn chung tăng khi `alpha_bar` giảm và observation gắn với signal-to-noise ratio.
