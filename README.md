# Reviewer's Dashboard

A Streamlit-based NLP dashboard for analyzing and visualizing user reviews (e.g., TripAdvisor) through **topic modeling**, **sentiment analysis**, and **interactive charts**. Built with Python, Gensim, TextBlob, and Plotly.

---

## 🚀 Features

- 📁 Upload a CSV file with a `review` column
- 🧠 Topic modeling using **Gensim LDA**
- 💬 Sentiment analysis via **TextBlob**
- 📊 Interactive visualization using **Plotly**
- 🔎 Filter and explore keywords by theme
- 📥 Download annotated results as CSV

---

## 🧱 Architecture

![Architecture Diagram](assets/aakinolaj_lda.png)

---

## 🛠️ Local Setup

For a step-by-step guide on running the dashboard locally, refer to:  
📄 [Luxor Dashboard Walkthrough Guide](docs/guide.md)

### Quickstart

```bash
# Clone the repository
git clone https://github.com/aakinolaj/reviewers-dashboard.git
cd reviewers-dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Download corpora used by TextBlob
python -m textblob.download_corpora

# Run the app
streamlit run luxor_dashboard_app.py
