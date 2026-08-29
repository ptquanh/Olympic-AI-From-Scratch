# 📖 Tài Liệu Tham Khảo

> [← Quay lại Tổng Quan](00_tong_quan.md)

---

## Nguồn Chính Thức Từ Cuộc Thi

| Nguồn                        | Link                                                       | Ghi chú                            |
| ---------------------------- | ---------------------------------------------------------- | ---------------------------------- |
| **Cẩm nang Olympic AI 2026** | File PDF local                                             | Quy chế, đề cương, chiến thuật thi |
| **AI Challenge PTIT**        | [aichallenge.ptit.edu.vn](https://aichallenge.ptit.edu.vn) | Nền tảng luyện thi chính thức      |
| **IOAI Official**            | [ioai-official.org](https://ioai-official.org)             | Syllabus + đề thi quốc tế          |
| **OlpAI Official**           | [olpai.vn](https://olpai.vn)                               | Thông tin OlpAI Sinh viên          |
| **VOAI**                     | Bộ GD&ĐT                                                   | Olympic AI học sinh                |

---

## Textbooks & Courses

| Sách/Khoá                           | Tác giả            | Dùng cho module           | Link                                                                                               |
| ----------------------------------- | ------------------ | ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Dive into Deep Learning (D2L)**   | Aston Zhang et al. | 00-04 (toàn bộ)           | [d2l.ai](https://d2l.ai)                                                                           |
| **Neural Networks: Zero to Hero**   | Andrej Karpathy    | 02: Autograd, Backprop    | [YouTube playlist](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)       |
| **fast.ai Practical Deep Learning** | Jeremy Howard      | 02-04: DL, CV, NLP        | [course.fast.ai](https://course.fast.ai)                                                           |
| **Stanford CS231n**                 | Fei-Fei Li         | 03: Computer Vision       | [cs231n.stanford.edu](http://cs231n.stanford.edu)                                                  |
| **Stanford CS224n**                 | Chris Manning      | 04: NLP                   | [web.stanford.edu/class/cs224n](https://web.stanford.edu/class/cs224n/)                            |
| **Pattern Recognition (PRML)**      | Christopher Bishop | 01: ML theory sâu         | [Book](https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/) |
| **Hands-On ML (HOML)**              | Aurélien Géron     | 01-02: ML + DL thực hành  | O'Reilly                                                                                           |
| **The Illustrated Transformer**     | Jay Alammar        | 04: Transformer intuition | [jalammar.github.io](https://jalammar.github.io/illustrated-transformer/)                          |
| **3Blue1Brown Neural Networks**     | Grant Sanderson    | 02: Trực giác             | [YouTube](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)                |

---

## Repos Tham Khảo

| Repo                       | Mô tả                                                      | Dùng cho                              |
| -------------------------- | ---------------------------------------------------------- | ------------------------------------- |
| **OlimpiadaAI/szkolenia**  | Giáo trình Olympic AI Ba Lan — theory + practice notebooks | Cấu trúc chương, phong cách giảng dạy |
| **ML-From-Scratch**        | Implement ML algorithms from scratch                       | 01: From-scratch reference            |
| **micrograd** (Karpathy)   | Tiny autograd engine                                       | 02: Autograd chapter                  |
| **minGPT** (Karpathy)      | Minimal GPT implementation                                 | 04: Transformer chapter               |
| **IOAI 2025 Starter Kits** | Official IOAI starter notebooks                            | 07: Problem solving                   |
| **AI-Olympiad**            | Collection of AI olympiad problems                         | 07: Problem bank                      |
| **Kaggle Winners**         | Winning solutions và discussions                           | 06: Competition patterns              |

---

## Official Documentation (Thư viện được phép trong thi)

> Theo Cẩm nang Phần 08, đây là các thư viện cài sẵn trong môi trường thi.

### Học sâu

| Thư viện              | Docs                                                           | Đọc gì                                         |
| --------------------- | -------------------------------------------------------------- | ---------------------------------------------- |
| **PyTorch**           | [pytorch.org/docs](https://pytorch.org/docs/stable/)           | `nn.Module`, `autograd`, `DataLoader`, `optim` |
| **torchvision**       | [pytorch.org/vision](https://pytorch.org/vision/stable/)       | `transforms`, `models`, `datasets`             |
| **pytorch_lightning** | [lightning.ai/docs](https://lightning.ai/docs/pytorch/stable/) | `Trainer`, `LightningModule`                   |

### NLP & LLM

| Thư viện                  | Docs                                                                          | Đọc gì                             |
| ------------------------- | ----------------------------------------------------------------------------- | ---------------------------------- |
| **transformers**          | [huggingface.co/docs/transformers](https://huggingface.co/docs/transformers/) | `AutoModel`, `pipeline`, `Trainer` |
| **sentence_transformers** | [sbert.net](https://www.sbert.net/)                                           | Embedding, similarity              |
| **datasets**              | [huggingface.co/docs/datasets](https://huggingface.co/docs/datasets/)         | Loading, processing                |
| **spacy**                 | [spacy.io](https://spacy.io/)                                                 | NER, tokenization                  |
| **nltk**                  | [nltk.org](https://www.nltk.org/)                                             | Text processing                    |
| **gensim**                | [radimrehurek.com/gensim](https://radimrehurek.com/gensim/)                   | Word2Vec, topic models             |
| **rank_bm25**             | [GitHub](https://github.com/dorianbrown/rank_bm25)                            | BM25 retrieval                     |
| **faiss**                 | [GitHub](https://github.com/facebookresearch/faiss)                           | Vector search                      |

### CV

| Thư viện         | Docs                                                    | Đọc gì                              |
| ---------------- | ------------------------------------------------------- | ----------------------------------- |
| **OpenCV (cv2)** | [docs.opencv.org](https://docs.opencv.org/)             | Image I/O, color spaces, transforms |
| **PIL/Pillow**   | [pillow.readthedocs.io](https://pillow.readthedocs.io/) | Image loading                       |
| **skimage**      | [scikit-image.org](https://scikit-image.org/)           | Image processing                    |

### ML

| Thư viện         | Docs                                                        | Đọc gì                                   |
| ---------------- | ----------------------------------------------------------- | ---------------------------------------- |
| **scikit-learn** | [scikit-learn.org](https://scikit-learn.org/stable/)        | `pipeline`, `model_selection`, `metrics` |
| **XGBoost**      | [xgboost.readthedocs.io](https://xgboost.readthedocs.io/)   | `XGBClassifier`, `XGBRegressor`          |
| **LightGBM**     | [lightgbm.readthedocs.io](https://lightgbm.readthedocs.io/) | `LGBMClassifier`                         |
| **CatBoost**     | [catboost.ai](https://catboost.ai/)                         | `CatBoostClassifier`                     |

### Data & Visualization

| Thư viện       | Docs                                                 | Đọc gì                               |
| -------------- | ---------------------------------------------------- | ------------------------------------ |
| **NumPy**      | [numpy.org/doc](https://numpy.org/doc/stable/)       | Arrays, broadcasting, linear algebra |
| **Pandas**     | [pandas.pydata.org](https://pandas.pydata.org/docs/) | DataFrame, merge, groupby            |
| **Matplotlib** | [matplotlib.org](https://matplotlib.org/stable/)     | Plotting                             |
| **Seaborn**    | [seaborn.pydata.org](https://seaborn.pydata.org/)    | Statistical plots                    |
| **Plotly**     | [plotly.com/python](https://plotly.com/python/)      | Interactive plots                    |

### Tiện ích (Python stdlib được phép)

| Module                     | Dùng cho                                 |
| -------------------------- | ---------------------------------------- |
| `re`                       | **Regex** — tiền xử lý text, parse files |
| `os`, `pathlib`, `glob`    | File handling                            |
| `json`, `csv`, `pickle`    | Data I/O                                 |
| `collections`, `itertools` | Data structures                          |
| `random`, `math`           | Utilities                                |
| `tqdm`                     | Progress bars                            |
| `joblib`                   | Parallel processing                      |

---

## Tham Khảo Thêm Cho Từng Module

| Module           | Primary                  | Secondary                      | Problem Bank     |
| ---------------- | ------------------------ | ------------------------------ | ---------------- |
| 00 Python & Math | Python docs, NumPy docs  | Regex101.com                   | —                |
| 01 ML            | D2L ch.2-3, HOML         | sklearn docs, ML-From-Scratch  | Kaggle tabular   |
| 02 DL            | Karpathy nn-zero-to-hero | D2L ch.4-8, fast.ai            | —                |
| 03 CV            | D2L ch.7-8,13, CS231n    | OlimpiadaAI szkolenia          | IOAI CV tasks    |
| 04 NLP+Audio     | D2L ch.9-10,15, CS224n   | OlimpiadaAI szkolenia, HF docs | IOAI NLP tasks   |
| 05 GenAI         | HF transformers docs     | Original papers                | —                |
| 06 Pipeline      | Kaggle winning solutions | AI-Olympiad repo               | aichallenge.ptit |
| 07 Problems      | IOAI official, OlpAI     | Poland OAI                     | aichallenge.ptit |

---

## Reproducibility Requirements

```toml
# pyproject.toml
[project]
requires-python = ">=3.10,<3.13"

[project.optional-dependencies]
core = [
    "numpy>=1.24,<2.0",
    "pandas>=2.0",
    "scikit-learn>=1.3",
    "matplotlib>=3.7",
    "seaborn>=0.12",
]
dl = [
    "torch>=2.1",
    "torchvision>=0.16",
    "transformers>=4.35",
]
boosting = [
    "xgboost>=2.0",
    "lightgbm>=4.0",
    "catboost>=1.2",
]
```

### Quy tắc repo

- **Random seeds**: `seed = 42` ở cell đầu mỗi notebook
- **Dataset**: script `download_data.py` cho mỗi module, không commit data >10MB
- **Hardware note**: ghi rõ "cần GPU" hay "chạy CPU ok"
- **Runtime estimate**: ghi "~X phút trên Colab T4"
- **Không commit**: checkpoints, model weights, large datasets → `.gitignore`
