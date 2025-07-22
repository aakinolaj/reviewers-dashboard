
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from gensim import corpora, models
from gensim.utils import simple_preprocess
from sklearn.manifold import TSNE
from textblob import TextBlob

# --- Streamlit App Setup ---
st.title("🕌 Luxor TripAdvisor Reviews Analysis")
st.markdown("Visualize topics, sentiments, and key patterns from visitor reviews")

# --- Upload Section ---
uploaded_file = st.file_uploader("📤 Upload your reviews CSV (must contain 'review' column)", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    reviews = df['review'].dropna().astype(str)

    # Preprocessing
    stopwords = set(["the", "and", "is", "in", "to", "of", "a", "for", "on", "was", "it", "with", "had"])
    processed_reviews = reviews.apply(lambda x: [w for w in simple_preprocess(x) if w not in stopwords])

    # LDA Topic Modeling
    dictionary = corpora.Dictionary(processed_reviews)
    corpus = [dictionary.doc2bow(text) for text in processed_reviews]
    lda_model = models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=4, passes=10, random_state=42)

    # Topic Distribution
    topic_vectors = []
    for doc in corpus:
        topic_dist = lda_model.get_document_topics(doc, minimum_probability=0)
        topic_vec = [prob for _, prob in topic_dist]
        topic_vectors.append(topic_vec)

    topic_array = np.array(topic_vectors)
    dominant_topic = [np.argmax(tv) for tv in topic_vectors]

    # Sentiment Analysis
    def get_sentiment(text):
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0.1:
            return "Positive"
        elif polarity < -0.1:
            return "Negative"
        else:
            return "Neutral"

    sentiments = reviews.apply(get_sentiment)

    # Dimensionality Reduction
    tsne = TSNE(n_components=2, perplexity=30, random_state=42)
    tsne_results = tsne.fit_transform(topic_array)

    # Topic Labels
    topic_labels = {
        0: "Hospitality & Service",
        1: "Tour & Experience",
        2: "Hotel Comfort",
        3: "Cultural Appreciation"
    }

    # DataFrame
    tsne_df = pd.DataFrame({
        'Review': reviews.values,
        'Topic': dominant_topic,
        'tSNE-1': tsne_results[:, 0],
        'tSNE-2': tsne_results[:, 1],
        'Sentiment': sentiments
    })
    tsne_df["Topic_Label"] = tsne_df["Topic"].map(topic_labels)

    # Keyword Filter
    keyword = st.text_input("🔍 Search for a keyword in reviews")
    if keyword:
        tsne_df = tsne_df[tsne_df['Review'].str.contains(keyword, case=False)]

    # Visualization
    color_by = st.selectbox("🎨 Color by", ["Topic_Label", "Sentiment"])
    fig = px.scatter(
        tsne_df, x="tSNE-1", y="tSNE-2", color=color_by,
        hover_data=["Review", "Topic_Label", "Sentiment"],
        title="t-SNE Visualization of Luxor Reviews"
    )
    st.plotly_chart(fig)

    # Display Table
    st.subheader("📋 Review Table")
    st.dataframe(tsne_df[['Review', 'Topic_Label', 'Sentiment']])

    # Download
    st.download_button(
        label="📥 Download Analyzed Reviews as CSV",
        data=tsne_df.to_csv(index=False),
        file_name="luxor_reviews_analyzed.csv",
        mime="text/csv"
    )
