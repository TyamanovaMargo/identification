import os
import pandas as pd

# Укажите путь к папке с жанрами
base_path = '/Users/margotiamanova/Desktop/identification/all-chunks-separate-folders-all_genres_300/Romance novel'

# Словарь для хранения названия жанра и среднего количества символов
genre_data = {}

# Пройдемся по каждой папке в base_path
for genre_folder in os.listdir(base_path):
    genre_path = os.path.join(base_path, genre_folder)
    if os.path.isdir(genre_path):
        char_counts = []
        # Пройдемся по каждому файлу в папке жанра
        for txt_file in os.listdir(genre_path):
            if txt_file.endswith('.txt'):
                file_path = os.path.join(genre_path, txt_file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    char_counts.append(len(text))
        
        if char_counts:
            average_chars = sum(char_counts) / len(char_counts)
            genre_data[genre_folder] = average_chars

# Создадим DataFrame из собранных данных
df = pd.DataFrame(list(genre_data.items()), columns=['Genre', 'Average Character Count'])

# Запишем DataFrame в Excel
df.to_excel('genre_character_counts_romance_300.xlsx', index=False)

print("Данные успешно записаны в genre_character_counts.xlsx")
