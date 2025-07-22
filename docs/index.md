# 📊 Luxor Reviewer's Dashboard – Walkthrough Guide

Welcome to the documentation site for the **Luxor TripAdvisor Reviews Dashboard**. This tool uses **Python**, **Streamlit**, and **NLP libraries** to analyze and visualize traveler sentiments and topic patterns from user reviews.

> ✅ Built by [@aakinolaj](https://github.com/aakinolaj) | [View on GitHub](https://github.com/aakinolaj/reviewers-dashboard)

---

## 📋 1. System Requirements

- Python 3.8 or higher (recommended: 3.10)
- VS Code or any code editor
- Git (optional)
- Internet access for downloading packages

---

## 📁 2. Project Structure

```
luxor_dashboard_app.py   # Main Streamlit app script
luxor_reviews_only.csv   # Sample review data
requirements.txt         # Python dependencies
README.md                # Project documentation
.gitignore               # File exclusions for Git
```

---

## 🧰 3. Step-by-Step Setup

### ➤ Step 1: Open your terminal or command prompt

### ➤ Step 2: Navigate to your workspace

```bash
cd ~/Desktop              # macOS/Linux
cd D:\Projects            # Windows
```

### ➤ Step 3: Create and enter a project folder

```bash
mkdir luxor_dashboard && cd luxor_dashboard
```

### ➤ Step 4: Place the following files into the folder:

- `luxor_dashboard_app.py`
- `requirements.txt`
- `luxor_reviews_only.csv`
- `README.md`

### ➤ Step 5: Create a virtual environment

```bash
python -m venv venv
```

### ➤ Step 6: Activate the virtual environment

```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### ➤ Step 7: Install dependencies

```bash
pip install -r requirements.txt
```

### ➤ Step 8: (Optional) Download TextBlob corpora

```bash
python -m textblob.download_corpora
```

---

## ▶️ 4. Run the Dashboard

Run the Streamlit app:

```bash
streamlit run luxor_dashboard_app.py
```

Then open your browser and go to:  
📍 http://localhost:8501

---

## 🧪 5. Using the Dashboard

- Upload a CSV with a `review` column
- Run topic modeling (LDA) and sentiment analysis
- Search reviews by keyword (e.g., “guide”, “room”)
- View results as interactive t-SNE plots and tables
- Export analyzed data as a downloadable CSV

---

## 🧯 6. Troubleshooting

- ❗ `ModuleNotFoundError`?  
  → Activate virtual environment and run:
  ```bash
  pip install -r requirements.txt
  ```

- 🛑 Streamlit not launching?  
  → Try:
  ```bash
  pip install --upgrade streamlit
  ```

- ⚠️ CSV errors?  
  → Ensure the uploaded file has a valid `review` column.

---

## ⚙️ 7. Customization Tips

- Change the number of topics:
  ```python
  num_topics = 4
  ```

- Edit topic labels to suit your dataset:
  ```python
  topic_labels = {0: "X", 1: "Y", ...}
  ```

- Use `VADER`, `spaCy`, or `transformers` for more advanced sentiment analysis.

- Deploy to **Streamlit Cloud** for free online access.

---

## 📜 8. License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute with proper attribution.
