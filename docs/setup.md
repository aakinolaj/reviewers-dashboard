---
title: Local Setup
nav_order: 2
---

# 🛠️ Local Setup Guide for Reviewer's Dashboard

This guide helps you clone and run the Reviewer's Dashboard locally using Python and Streamlit.

...

## 🚀 Prerequisites

Make sure the following are installed on your system:

- [Python 3.10](https://www.python.org/downloads/release/python-3109/)
- [Git](https://git-scm.com/downloads)
- A terminal or command prompt (Windows Terminal, PowerShell, CMD, or macOS/Linux Terminal)

---

## 📦 Step-by-Step Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/aakinolaj/reviewers-dashboard.git
cd reviewers-dashboard
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

---

### 3. Activate the Environment

#### On Windows:

```bash
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. (Optional) Download TextBlob Corpora

```bash
python -m textblob.download_corpora
```

---

### 6. Run the Streamlit App

```bash
streamlit run luxor_dashboard_app.py
```

Open your browser and go to:

📍 http://localhost:8501

---

## 🛠 Troubleshooting

- `ModuleNotFoundError`: Activate the virtual environment first.
- `streamlit` not recognized? Run `pip install streamlit` again.
- Need help? Reach out via the repository’s Issues tab.

---

## 🙌 You're Done!

Enjoy exploring and customizing the **Reviewer's Dashboard** locally!
