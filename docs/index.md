# Luxor Dashboard Walkthrough Guide

This guide helps you set up and run the **Luxor TripAdvisor Reviews Dashboard** locally on your machine. It uses **Python**, **Streamlit**, and **NLP libraries** to analyze and visualize traveler sentiments and themes from reviews.

---

## 1. System Requirements

- Python 3.8 or higher
- VS Code or any preferred code editor
- Git (optional)
- Internet connection for package installation

---

## 2. Project Structure

```
luxor_dashboard_app.py   # Main Streamlit app script
luxor_reviews_only.csv   # Sample review data
requirements.txt         # Python dependencies
README.md                # Project documentation
.gitignore               # File exclusions for Git
```

---

## 3. Step-by-Step Setup Instructions

### Step 1: Open terminal or command prompt.

### Step 2: Navigate to your workspace

```bash
cd ~/Desktop             # On macOS/Linux
D:\Projects              # On Windows
```

### Step 3: Create and enter a project folder

```bash
mkdir luxor_dashboard && cd luxor_dashboard
```

### Step 4: Place the following files into this folder:

- `luxor_dashboard_app.py`
- `requirements.txt`
- `luxor_reviews_only.csv`
- `README.md`

### Step 5: Create a virtual environment

```bash
python -m venv venv
```

### Step 6: Activate the environment

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Step 7: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 8: Download TextBlob corpora (optional)

```bash
python -m textblob.download_corpora
```

---

## 4. Run the App

Once setup is complete, run:

```bash
streamlit run luxor_dashboard_app.py
```

This will launch the app in your default browser at:

```
http://localhost:8501
```

---

## 5. Using the Dashboard

- Upload the provided `luxor_reviews_only.csv` or any CSV file with a `review` column
- Visualize clusters of reviews by **topic** and **sentiment**
- Use the keyword search bar to filter specific themes (e.g., `"guide"`, `"room"`)
- View results as **interactive charts** and **tables**
- Download the annotated results as a CSV for external analysis

---

## 6. Troubleshooting

- 🔴 `ModuleNotFoundError`? → Recheck your virtual environment and run:
  ```bash
  pip install -r requirements.txt
  ```

- 🛑 Streamlit not launching? → Try upgrading:
  ```bash
  pip install --upgrade streamlit
  ```

- ⚠️ Upload Error? → Ensure your file has a `review` column with text entries

---

## 7. Customization Tips

- Change number of LDA topics:
  ```python
  num_topics = 4
  ```

- Edit topic labels in the script to match your new themes.

- Replace **TextBlob** with **VADER**, **spaCy**, or **transformers** for sentiment analysis.

- Deploy to **Streamlit Cloud** for easy online sharing.

---

## 8. License

This project is licensed under the **MIT License**.

You may use, modify, and distribute it with proper attribution.
