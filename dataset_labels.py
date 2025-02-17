import os
import pandas as pd

# Путь к папкам с жанрами
path_to_genres = '/Users/margotiamanova/Desktop/identification/Multilabel_dataset/first_chunk'

# Словарь с жанрами и их лейблами
genres_labels = {
    'action': 0,
    'adventure': 1,
    'detective': 2,
    'fantasy': 3,
    'SF': 4,
    'shortStories': 5,
    'romance': 6,
    'classic': 7,
    'childrens': 8,
    'nonFiction': 9,
    'contemporary': 10
}

# Список для хранения данных
data = []

# Итерация по папкам и сбор данных
for genre, label in genres_labels.items():
    genre_path = os.path.join(path_to_genres, genre)
    for filename in os.listdir(genre_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(genre_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                data.append({'text': content, 'label': label})

# Создание DataFrame и сохранение его в CSV
df = pd.DataFrame(data)
df.to_csv('dataset_all_pos_dir_multiclass_first_chunk.csv', index=False, encoding='utf-8')

