# Lời giải: Generative Cv

<details><summary><b>Tầng 1: Understand</b></summary>
Cố gắng tối đa hóa xác suất đoán ĐÚNG ảnh thật (cho điểm 1) và đoán ĐÚNG ảnh giả (cho điểm 0).
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

(Phần này là lý thuyết, vì Diffusion model rất khó code chay tầng Implement cơ bản. Bạn chỉ cần hiểu là Diffusion phải chạy qua vòng lặp nhiều bước (scheduler.step())).

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>
- **CFG thấp (VD: 1.0 - 3.0):** Model sẽ tự do sáng tạo, ít bám sát vào prompt, ảnh trông tự nhiên hơn, nghệ thuật hơn nhưng có thể xuất hiện vật thể lạ không liên quan.
- **CFG cao (VD: 10.0 - 15.0):** Model tuân thủ răm rắp đoạn prompt của bạn, ép bức ảnh phải có đầy đủ chi tiết. Tuy nhiên màu sắc thường bị quá bão hòa (oversaturated) và ảnh trông có vẻ "cứng" (nhân tạo). Ngưỡng chuẩn thường là 7.0 - 7.5.
</details>
