# Unsupervised Learning

> **Track:** Foundation 📖 | Contest 📖

## ① Prerequisite Check

Bạn cần tính được Euclidean distance, chuẩn hóa feature và giải thích variance/covariance. Nếu chưa, quay lại Math Essentials và Feature Engineering.

## ② Learning Outcomes

- Thực hiện một vòng assign–update của K-Means bằng tay.
- Giải thích PCA chọn trục variance lớn nhưng không dùng nhãn.
- Chọn K-Means, DBSCAN hoặc hierarchical clustering dựa trên shape/noise của dữ liệu.
- Dùng t-SNE/UMAP để khám phá mà không coi khoảng cách toàn cục hoặc cluster nhìn thấy là bằng chứng định lượng.

## ③ Concept Map

`Scaling → [clustering | dimensionality reduction] → EDA, anomaly hints, feature compression`

## ④ Intuition

Khi không có nhãn, “đúng” không còn nghĩa là accuracy cao. Ta phải nêu giả định về cấu trúc: K-Means tìm cụm gần centroid và gần dạng cầu; DBSCAN tìm vùng mật độ và có thể bỏ noise; PCA tìm phép chiếu tuyến tính giữ variance.

## ⑤ Math & Worked Example

K-Means tối thiểu hóa tổng bình phương khoảng cách trong cụm `Σ_i ||x_i-μ_{c_i}||²`. Với các điểm `[0, 2, 8, 10]` và centroid ban đầu `0, 10`, bước assign tạo hai nhóm `[0,2]`, `[8,10]`; bước update cho centroid mới `1, 9`. Objective không tăng sau mỗi assign/update, nhưng có thể hội tụ vào local optimum.

PCA center dữ liệu, rồi lấy eigenvectors của covariance (hoặc right singular vectors từ SVD). Không chuẩn hóa có thể khiến feature đơn vị lớn chi phối principal components.

## ⑧ Framework / Lab

Lab so sánh K-Means/PCA trên dữ liệu nhỏ. Fit scaler và PCA trên train khi chúng nằm trong supervised downstream pipeline.

## ⑩ Misconceptions

- ❌ **Sai:** Elbow luôn cho một `k` duy nhất. → ✅ Elbow có thể mơ hồ; cần stability và domain knowledge.
- ❌ **Sai:** t-SNE tạo ra ground-truth clusters. → ✅ Hình phụ thuộc perplexity/seed và bóp méo global geometry.
- ❌ **Sai:** PCA chọn feature quan trọng cho target. → ✅ PCA không nhìn target.

## ⑮ Mastery Check

Nêu được assumption, metric nội tại và ít nhất một kiểm tra stability trước khi diễn giải cluster.

## ⑯ Time Estimate

Theory: ~1.5h · Code: ~1h · Exercises: ~1h
