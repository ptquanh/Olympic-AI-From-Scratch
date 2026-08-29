# Hướng dẫn Tự học Hiệu quả: Olympic AI From Scratch

Chào mừng bạn đến với giáo trình **Olympic AI From Scratch**. Đây là một dự án mở, được thiết kế đặc biệt không chỉ giúp bạn hiểu sâu về bản chất các thuật toán AI mà còn trang bị kỹ năng thực chiến để tham gia các kỳ thi Olympic AI (OlpAI SV, Olympic AI PTIT, VOAI, IOAI, v.v.).

Để không bị ngợp trước khối lượng kiến thức lớn, hãy đọc kỹ hướng dẫn này trước khi bắt đầu!

---

## 🗺️ 1. Lộ trình học (Modules)

Giáo trình được chia làm 6 Modules, đi từ cơ bản đến nâng cao. Mỗi Module là một bước đệm cho Module tiếp theo:

- **Module 00: Foundation & Setup:** Cài đặt môi trường, ôn tập Toán (Linear Algebra, Calculus) và Python/NumPy cơ bản.
- **Module 01: Machine Learning Basics:** Các thuật toán ML kinh điển (Linear/Logistic Regression, Tree-based models), các kỹ thuật đánh giá (Metrics) và tinh chỉnh mô hình.
- **Module 02: Deep Learning Fundamentals:** Mạng Nơ-ron (Neural Networks), Backpropagation, Tối ưu hóa (Optimizers) và Regularization.
- **Module 03: Computer Vision (CV):** Xử lý ảnh, CNN, ResNet, Vision Transformer (ViT) và Object Detection.
- **Module 04: NLP & Audio:** Xử lý ngôn ngữ tự nhiên, Word Embeddings, Attention Mechanism, Transformer và xử lý Audio.
- **Module 05: Generative AI & LLM:** Language Modeling, Prompt Engineering, Fine-tuning (LoRA, QLoRA) và Multimodal.

> **💡 Lời khuyên:** Hãy học theo trình tự tuyến tính từ 00 -> 05. Tuyệt đối không nhảy cóc sang Module 03, 04, 05 nếu bạn chưa nắm vững Gradient Descent và Backprop ở Module 02.

---

## 📖 2. Hiểu đúng "Loại Bài Học" (Archetype)

Không phải bài nào cũng có cấu trúc giống nhau. Tùy vào độ phức tạp và tính ứng dụng, giáo trình chia các bài học thành 3 loại (Archetype):

1.  **Core Chapter (Bài cốt lõi):** Các thuật toán nền tảng (Linear Regression, Backprop, Attention...). Ở các bài này, bạn bắt buộc phải hiểu sâu toán học và _tự tay code lại từ đầu (from-scratch)_ không dùng thư viện.
2.  **Concept Lesson (Bài khái niệm):** Các khái niệm bổ trợ (Metrics, Optimizers, Prompt Engineering...). Trọng tâm là biết cách dùng đúng thư viện, hiểu rõ các tham số và biết cách debug.
3.  **Competition Lab (Bài thực hành thi đấu):** Các bài tập lớn mô phỏng đề thi thực tế. Trọng tâm là xây dựng Pipeline (Data -> Model -> Evaluate -> Submit) hoàn chỉnh.

---

## 🛠️ 3. Cấu trúc của một bài học

Một bài học tiêu chuẩn sẽ bao gồm các file sau. Bạn nên tiếp cận theo đúng thứ tự này:

1.  **`README.md` (Đọc đầu tiên):** Chứa lý thuyết, Toán học, Intuition (Trực giác) và Ví dụ minh họa tính tay.
2.  **`01_from_scratch.ipynb` (Chỉ có ở Core Chapter):** Hướng dẫn code thuật toán bằng Python/NumPy thuần. Không dùng thư viện Machine Learning.
3.  **`02_framework.ipynb` hoặc `lab.ipynb`:** Cách sử dụng thuật toán bằng các thư viện chuẩn (PyTorch, Scikit-learn).
4.  **`03_experiments.ipynb` (Tùy chọn):** Các thí nghiệm đánh giá mô hình, thay đổi tham số để rút ra kết luận.
5.  **`code_notes.md`:** Tóm tắt các đoạn code mẫu (Core Patterns), API Cheat Sheet và Flashcards để ôn tập nhanh.
6.  **`olympiad_transfer.md` (Rất quan trọng cho thi cử):** Hướng dẫn cách áp dụng kiến thức của bài này vào các đề thi Olympic (Baseline thế nào, Metric gì, Failure modes phổ biến).
7.  **`exercises.md` & `solutions.md`:** Hệ thống bài tập 5 tầng (Understand, Implement, Experiment, Transfer, Olympiad). File `solutions.md` chứa đáp án được ẩn đi.

---

## 🧠 4. Phương pháp Học 5 Bước (Quy tắc "Không nhìn tài liệu")

Cách học AI tốt nhất không phải là đọc code, mà là **viết lại code**. Hãy áp dụng chu trình 5 bước sau cho mỗi bài:

**Bước 1: Nắm bắt Lý thuyết (15 - 30 phút)**
Đọc file `README.md`. Hãy chắc chắn bạn trả lời được 3 câu hỏi:

- Thuật toán này sinh ra để giải quyết vấn đề gì? (Intuition)
- Toán học đằng sau nó là gì? (Viết ra nháp)
- Nếu cho bộ số liệu cực nhỏ (VD: 3 điểm dữ liệu), bạn có tính tay được 1 vòng lặp không? (Worked Example)

**Bước 2: Hiểu cách Code (30 - 45 phút)**
Đọc và chạy từng cell trong các file notebook (`.ipynb`). Ở mỗi cell, hãy đoán xem output sẽ là gì _trước khi_ nhấn Shift+Enter. Đọc kỹ các comment `# WHY:` để hiểu dụng ý của tác giả.

**Bước 3: Ghi nhớ (10 phút)**
Mở file `code_notes.md`. Đọc qua các "Core Patterns". Review lướt qua bảng "Flashcards".

**Bước 4: Luyện Code Tay (Bắt buộc!)**
Trong file `code_notes.md` sẽ có mục **🏋️ Bài Luyện Code Tay**.
_Quy tắc:_

1. Tắt hết các file hướng dẫn, kể cả file bạn vừa học.
2. Mở một notebook trống.
3. Hẹn giờ (ví dụ 10 phút) và tự gõ lại thuật toán/pipeline từ trí nhớ.
   _(Nếu bí, hãy lật ra xem lại, sau đó đóng lại và gõ tiếp, TUYỆT ĐỐI không copy-paste)._

**Bước 5: Làm Bài Tập & Đối chiếu (60 phút)**
Hoàn thành các bài tập trong file `exercises.md`. Đảm bảo làm đủ 5 tầng (nếu có). Sau khi làm xong, hãy mở file `solutions.md` để so sánh cách giải.

---

## 🏆 5. Bí kíp dành riêng cho Đội tuyển (Olympic Transfer)

Nếu mục tiêu của bạn là đi thi Olympic AI, đừng bao giờ bỏ qua file **`olympiad_transfer.md`** trong các Core Chapter.

Khi đi thi, thời gian rất có hạn (thường là 4h - 6h). File này sẽ cung cấp cho bạn:

1.  **Dấu hiệu nhận biết:** Đọc đề thi, thấy keyword gì thì dùng mô hình gì.
2.  **Baseline nhanh nhất:** Đoạn code giúp bạn có kết quả submit ngay trong 30 phút đầu tiên.
3.  **Chiến lược tăng điểm:** Khi baseline đã xong, làm gì tiếp theo để tăng điểm (Hyperparameter tuning, Data Augmentation, Ensembling...).
4.  **Các lỗi dễ tạch (Failure Modes):** Những cái bẫy thường gặp khiến mô hình train mãi không hội tụ.

---

## 💻 6. Môi trường Thực hành

- **Offline:** Xem file `SETUP.md` để cài đặt môi trường bằng Conda (`environment.yml`). Bạn nên có một GPU (NVIDIA) để chạy mượt mà Module 3, 4, 5.
- **Online (Khuyên dùng):** Nếu máy tính không đủ mạnh, hãy upload các file `.ipynb` lên [Google Colab](https://colab.research.google.com/) hoặc [Kaggle Notebooks](https://www.kaggle.com/code). Các file notebook trong giáo trình đều đã được chuẩn hóa để chạy trực tiếp trên các nền tảng này!

> **Chúc bạn học tốt và đạt thành tích cao trong các kỳ thi Olympic AI sắp tới!**
