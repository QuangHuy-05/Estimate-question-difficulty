# 🎓 Estimate Question Difficulty

An AI-powered system that predicts and classifies the difficulty level of exam questions using NLP and machine learning.

---

## Features


- AI-driven difficulty estimation using Random Forest and embeddings  
- Automatic text processing and tokenization  
- Question categorization based on Bloom's taxonomy  
- Feature extraction from linguistic and semantic properties  
- Interactive model training and evaluation (Jupyter Notebooks)  
- Data persistence with CSV and JSON exports  
- Multi-subject support: Literature, Geography, English, etc.
---

## 🧰 Tech Stack

**Backend / ML:**
- Python 3.10+
- scikit-learn, pandas, numpy
- nltk, underthesea (Vietnamese NLP)
- joblib, tqdm, imbalanced-learn

**Environment:**
- Jupyter Notebook / Google Colab
- Virtual Environment (venv / conda)

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/QuangHuy-05/Estimate-question-difficulty.git
cd Estimate-question-difficulty

# Create and activate virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

```
---
```bash
## Project Structure
estimate-question-difficulty/
├── crawl_data/
│   ├── crawl_Van.ipynb
│   ├── crawl_SuDiaAnh.ipynb
├── data_processed/
│   ├── Van_hoc_processed.txt
│   ├── Dia_processed.txt
│   ├── Anh_processed.txt
│   └── Su_processed.txt
├── Embedding/
│   ├── Output_features/
│   │   ├── question_features.csv
│   │   └── noise_features.csv
│   ├── Output_ws/
│   │   ├── questions.json
│   │   ├── ori_questions.json
│   │   └── qa_processed_ws.txt
│   └── word_segment.ipynb
├── training/
│   ├── training.ipynb
│   ├── check_model.ipynb
│   ├── random_forest_best.pkl
│   └── data_for_training/
│       ├── cau_hoi_bloom.csv
│       ├── van_with_bloom_out.csv
│       └── merged.csv
├── pipeline_data.ipynb
├── data_process.ipynb
├── merged.csv
├── requirements.txt
├── README.md
└── .env

