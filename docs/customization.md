---
title: Customization
nav_order: 3
---

# ⚙️ Dashboard Customization Guide

This guide explains how to customize various aspects of the Luxor Reviewer's Dashboard, including topic modeling, sentiment analysis, and the user interface.

---

## 🔢 Change Number of Topics

Open `luxor_dashboard_app.py` and find:

```python
lda_model = models.LdaModel(..., num_topics=4, ...)
```

Change `num_topics=4` to any number (e.g., `5`, `6`, `10`) to adjust the number of LDA topics.

---

## 🏷️ Rename Topic Labels

Modify the `topic_labels` dictionary to match your dataset:

```python
topic_labels = {
    0: "Hospitality & Service",
    1: "Tour & Experience",
    2: "Hotel Comfort",
    3: "Cultural Appreciation"
}
```

You can also load labels dynamically from a config file.

---

## 💬 Replace Sentiment Analyzer

The app uses **TextBlob** by default:

```python
from textblob import TextBlob
```

To improve sentiment analysis:
- Use `vaderSentiment` for social media-style tone
- Use HuggingFace Transformers (e.g., BERT) for deep contextual sentiment

---

## 🎨 Change Visualization Settings

Edit this part for `t-SNE` and `Plotly` visualization:

```python
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
fig = px.scatter(..., color="Topic_Label", ...)
```

You can:
- Adjust `perplexity`, `learning_rate`, or `n_components`
- Switch axes or change color mapping to use sentiment instead

---

## 🧪 Add More Filters

You can add filters to:
- Filter reviews by date, rating, or length
- Add dropdowns or sliders with `st.slider()`, `st.multiselect()`, etc.

---

## 🌐 Deploy Custom Version

To deploy a modified version:
- Push changes to your GitHub repo
- Re-deploy on [Streamlit Cloud](https://streamlit.io/cloud)

Or:
- Use Docker / Streamlit Sharing / HuggingFace Spaces

---

## 📘 Want More Help?

Open an issue or contribute directly at:  
👉 [https://github.com/aakinolaj/reviewers-dashboard](https://github.com/aakinolaj/reviewers-dashboard)
