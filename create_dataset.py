import os
import shutil
import random

genre = "without_classic"

def dataset_one_chunk(input_folder, output_folder=f'dataset_one_chunk_{genre}'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    visited_folders = set()  # Для отслеживания посещенных папок

    for root, dirs, files in os.walk(input_folder):
        if root not in visited_folders:
            visited_folders.add(root)  # Добавляем текущую папку в посещенные
            txt_files = [file for file in files if file.endswith('.txt')]

            if txt_files:
                # Берем только первый .txt файл из текущей папки
                file_name = txt_files[0]
                file_path = os.path.join(root, file_name)

                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read()

                # Создаем папку для текущего файла
                output_subfolder = os.path.join(output_folder, os.path.basename(root))
                os.makedirs(output_subfolder, exist_ok=True)

                # Записываем один чанк текста в файл
                output_file_path = os.path.join(output_subfolder, f'{file_name}_chunk_1.txt')
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(text)


def extractFiles(input_folder=f'dataset_one_chunk_{genre}', output_folder=f'extract_files_{genre}'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    copied_files = []  # Для хранения путей скопированных файлов

    for foldername, subfolders, filenames in os.walk(input_folder):
        for filename in filenames:
            if filename.endswith('.txt'):
                source_path = os.path.join(foldername, filename)
                destination_path = os.path.join(output_folder, filename)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)  # Добавляем путь скопированного файла в список

    return copied_files  # Возвращаем список скопированных файлов


def selectFiles(input_folder, num_files):
    output_folder = f'selected_files_{genre}'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]
    selected_files = random.sample(files, min(num_files, len(files)))  # Обработка случая, когда num_files больше доступных файлов

    for file_name in selected_files:
        source_path = os.path.join(input_folder, file_name)
        shutil.copy(source_path, output_folder)


def splitFiles(input_folder, output_train=f'train_{genre}', output_test=f'test_{genre}', split_ratio=0.8):
    if not os.path.exists(output_train):
        os.makedirs(output_train)
    if not os.path.exists(output_test):
        os.makedirs(output_test)

    files = []
    for foldername, subfolders, filenames in os.walk(input_folder):
        for filename in filenames:
            if filename.endswith('.txt'):
                files.append(os.path.join(foldername, filename))

    random.shuffle(files)
    num_train = int(len(files) * split_ratio)

    for i, file_path in enumerate(files):
        if i < num_train:
            destination_folder = output_train
        else:
            destination_folder = output_test
        shutil.copy(file_path, destination_folder)

# Пример использования
root_folder_path = "/Users/margotiamanova/Desktop/identification/result/all-chunks-separate-folders-all_books"
dataset_one_chunk(root_folder_path)
extracted_files = extractFiles(f"dataset_one_chunk_{genre}")

# Запрос у пользователя на количество файлов для выборки
num_files_to_select = int(input("Введите количество файлов для выборки: "))
selectFiles(f"extract_files_{genre}", num_files_to_select)
splitFiles(f"selected_files_{genre}")
