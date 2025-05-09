# SONATA: Russian Book Genre Classification Dataset

Welcome to the **SONATA** dataset repository! This dataset is designed for genre classification tasks of Russian books, offering a rich collection of stylometric features and book genres. It was collected from **knigogo.net**, a popular Russian-language website for audiobooks and online literature.

The dataset is publicly available for research and academic purposes. If you use or reference this dataset, please cite the following paper:

> **Vanetik, Natalia**, **Tiamanova, Margarita**, **Kogan, Genady**, **Litvak, Marina**.  
> *Genre Classification of Books in Russian with Stylometric Features: A Case Study*.  
> *Information*, 15(6), 340, 2024.  


---

## Dataset Overview

- **Source**: knigogo.net (a Russian-language platform for books and audiobooks)
- **Genres Included**:  
  1. Science Fiction  
  2. Detective  
  3. Romance  
  4. Fantasy  
  5. Classic  
  6. Action  
  7. Non-fiction  
  8. Contemporary Literature  
  9. Adventure  
  10. Novel and Short Stories  
  11. Children's Books
  
- **Total Books**: 8189 original books
- **Total Instances**: 10444 book instances (some books belong to multiple genres)
- **Languages**: Russian
  
---

## Dataset Features

The dataset consists of the following:

- **Original Books**: Full books available in various formats (fb2, rtf, epub, txt).
- **Book Chunks**: Books split into chunks of 300 words to facilitate Large Language Model (LLM) processing.
- **Metadata**: Metadata extracted from the second line of the text (excluding authors' names).

---

## Data Collection Process

1. **Re-Encoding**: All files were re-encoded to UTF-8 for compatibility and consistency.
2. **Meta-Data Parsing**: The second line of each text containing meta-data (including author names) was removed.
3. **Text Chunking**: Books were split into smaller parts (chunks of 300 words) to make them suitable for LLM processing, which has a token limit.

---

## How to Access

You can access the full dataset, including complete books and their corresponding chunks, via the following Google Drive repository:

[SONATA Dataset on Google Drive](https://drive.google.com/drive/folders/1rnpMl39yOpsYTaE6ZGzk5nHQRU2dOASB?usp=sharing)

---

## Citation

If you use or reference this dataset, please cite the following paper:

```bibtex
@article{vanetik2024genre,
  title={Genre Classification of Books in Russian with Stylometric Features: A Case Study},
  author={Vanetik, Natalia and Tiamanova, Margarita and Kogan, Genady and Litvak, Marina},
  journal={Information},
  volume={15},
  number={6},
  pages={340},
  year={2024},
  publisher={Multidisciplinary Digital Publishing Institute}
}

