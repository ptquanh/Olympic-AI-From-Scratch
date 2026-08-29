# Olympiad Transfer: Metrics & Validation

## 1. Nhận diện trong đề

Metrics & Validation không phải là một bài toán cụ thể, mà là **BẮT BUỘC** trong mọi bài toán Olympic. Nếu bạn chọn sai chiến lược Cross-Validation, Leaderboard Public có thể rất cao (Top 1), nhưng khi kết thúc giải, điểm Private sẽ tụt thê thảm (Rơi xuống Top 50) - Hiện tượng này gọi là **Shake-up**.

## 2. Kỹ năng Bắt buộc (Local Validation)

Nguyên tắc số 1 của Kaggle/Olympic: **TRUST YOUR CV (Cross-Validation)**.

- Đừng nộp bài liên tục lên hệ thống (Public LB) để lấy điểm. Hệ thống thường chỉ tính điểm trên 30% dữ liệu.
- Bạn phải tự xây dựng bộ K-Fold ở máy mình. Nếu điểm CV ở máy tăng mà điểm Public LB giảm, hãy TIN VÀO CV CỦA BẠN.

## 3. Các loại Validation Strategy

1. **KFold:** Dùng cho bài toán Regression.
2. **StratifiedKFold:** Dùng cho bài toán Classification. Đảm bảo tỷ lệ các class đều nhau.
3. **GroupKFold:** Dùng khi có dữ liệu theo nhóm. VD: Trong dữ liệu y tế, có nhiều ảnh X-quang của CÙNG 1 bệnh nhân. Nếu chia random, bệnh nhân A vừa có mặt ở Train, vừa có mặt ở Test -> Leakage. Phải dùng GroupKFold để bệnh nhân A chỉ ở Train hoặc chỉ ở Test.
4. **TimeSeriesSplit:** Dùng khi có yếu tố thời gian (Dự đoán chứng khoán). Không được dự đoán quá khứ bằng tương lai.

## 4. Failure modes (Lỗi thường gặp)

1. **Target Leakage:** Dùng thông tin tương lai để dự đoán hiện tại. Vd: Đề yêu cầu dự đoán sinh viên có đỗ đại học không, mà features lại chứa cột "Điểm thi đại học".
2. **Overfitting Public Leaderboard:** Tinh chỉnh mô hình (hyperparameters) hàng trăm lần dựa trên điểm Public LB. Đến khi Private LB mở ra, mô hình fail hoàn toàn. Lại câu thần chú: _Trust your CV_.

## 5. Phân bổ thời gian (Contest)

- Bạn phải tốn 20-30 phút đầu tiên của vòng Chung kết chỉ để viết file Python sinh ra các Fold ID (vd: Thêm 1 cột `fold` vào file `train.csv`). Toàn bộ thành viên trong đội phải DÙNG CHUNG file `train_folds.csv` này để đảm bảo khi Ensemble không bị rác.
