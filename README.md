# 📚 Genre Classification of Books in Russian

A machine learning project for automatic classification of Russian-language literary texts into genres using NLP techniques.

## 🔍 Overview

This research aims to build an automated system that classifies Russian books into genres using advanced natural language processing methods and deep learning models. A custom dataset, **ROBYN (Russian bOoks BY geNre)**, was collected and processed, enabling binary and multi-class classification tasks.

## 📁 Dataset

The dataset was built by scraping texts from [knigogo.net](https://knigogo.net), covering **11 genres**:

- Science Fiction
- Detective
- Romance
- Fantasy
- Classic
- Action
- Non-Fiction
- Contemporary Literature
- Adventure
- Novel and Short Stories
- Children’s Books

**Key Stats:**
- 📄 10,419 books (8,189 unique)
- 🧩 507,351 text chunks (400 words each)
- 📏 Average book length: ~20,000 words

## ⚙️ Preprocessing

Text was preprocessed using Python scripts to:
- Convert to UTF-8
- Remove author names
- Segment texts into 400-word chunks
- Apply lowercase transformation (optional)
- Preserve punctuation (boosts performance)

## 🧠 Models Used

Two transformer-based models were evaluated:
- **DeepPavlov (RuBERT)**
- **Multilingual BERT (mBERT)**

**Vectorization:** WordPiece Tokenization  
**Embedding Visualization:** t-SNE plots to analyze clustering by genre

## 🧪 Experiments

- **Binary Classification**: Genre vs. non-genre
- **Multiclass Classification**: Classify text into one of the 11 genres
- **Evaluated using**:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Hamming Loss (for multilabel tasks)

## 📈 Results

DeepPavlov with preserved punctuation performed best, achieving:
- Strong genre separation in t-SNE plots
- Higher accuracy than mBERT in most experiments

🚀 Applications

    Automatic genre tagging in digital libraries

    Enhancing book recommendation systems

    Linguistic research in Russian literary studies

