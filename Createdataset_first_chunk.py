import os
import shutil
import random
import re

genre = "without_novelStory"


# def dataset_one_chunk(input_folder, output_folder=f'dataset_one_chunk_{genre}'):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     visited_folders = set()  # Для отслеживания посещенных папок

#     for root, dirs, files in os.walk(input_folder):

#         if root not in visited_folders:
#             visited_folders.add(root)  # Добавляем текущую папку в посещенные
#             txt_files = [file for file in files if file.endswith('.txt')]
            
#             if txt_files:
#                 # Берем только первый .txt файл из текущей папки
#                 file_name = txt_files[0]
#                 file_path = os.path.join(root, file_name)

#                 with open(file_path, 'r', encoding='utf-8') as file:
#                     text = file.read()

#                 # Создаем папку для текущего файла
#                 output_subfolder = os.path.join(output_folder, os.path.basename(root))
#                 os.makedirs(output_subfolder, exist_ok=True)

#                 # Записываем один чанк текста в файл
#                 output_file_path = os.path.join(output_subfolder, file_name)
#                 with open(output_file_path, 'w', encoding='utf-8') as output_file:
#                     output_file.write(text)


def extractFiles(input_folder=f"First_Chunks_{genre}", output_folder=f'extract_files_{genre}'):
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

# random chunks
def selectFiles(input_folder, num_files):
    output_folder = f'selected_files_{genre}'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]

    selected_files = random.sample(files, min(num_files, len(files)))  # Обработка случая, когда num_files больше доступных файлов
    print(selected_files)
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
# root_folder_path = "Action"
# dataset_one_chunk(root_folder_path)
# extracted_files = extractFiles(f"dataset_one_chunk_{genre}")
#
# # Запрос у пользователя на количество файлов для выборки
# num_files_to_select = int(input("Введите количество файлов для выборки: "))
# test = selectFiles(f"extract_files_{genre}", num_files_to_select)
#
# splitFiles(f"selected_files_{genre}")


def get_first_and_last_chunks(action_folder):
    folder_info = {}

    # Iterate over each folder in the action folder
    for root, dirs, files in os.walk(action_folder):
        folder_name = os.path.basename(root)  # Get the name of the current folder
        txt_files = [file for file in files if file.endswith('.txt')]
        if txt_files:
            total_chunks = len(txt_files)
            first_chunk_name = f"{folder_name}_chunk_{1}_"

            last_chunk_name = f"{folder_name}_chunk_{total_chunks}"

            # Find the paths of the first and last chunks based on their names
            first_chunk_path = None
            last_chunk_path = None
            for file in txt_files:
                if first_chunk_name in file:
                    first_chunk_path = os.path.join(root, file)
                elif last_chunk_name in file:
                    last_chunk_path = os.path.join(root, file)

            folder_info[folder_name] = {
                'count': total_chunks,
                'first_chunk_path': first_chunk_path,
                'last_chunk_path': last_chunk_path
            }

    return folder_info




def save_first_chunks(action_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate over each folder in the action folder
    for root, dirs, files in os.walk(action_folder):
        folder_name = os.path.basename(root)  # Get the name of the current folder
        txt_files = [file for file in files if file.endswith('.txt')]
        if txt_files:
            total_chunks = len(txt_files)
            first_chunk_name = f"{folder_name}_chunk_1_"

            # Find the path of the first chunk based on its name
            first_chunk_path = None
            for file in txt_files:
                if first_chunk_name in file:
                    first_chunk_path = os.path.join(root, file)
                    break  # Exit loop once the first chunk is found

            # Save the first chunk to the destination folder
            if first_chunk_path:
                destination_folder_for_chunk = os.path.join(destination_folder, folder_name)
                if not os.path.exists(destination_folder_for_chunk):
                    os.makedirs(destination_folder_for_chunk)
                shutil.copy(first_chunk_path, destination_folder_for_chunk)


# Example usage:
root_folder_path = "/Users/margotiamanova/Desktop/identification/result/all-chunks-separate-folders-all_books"
destination_folder_path = f"First_Chunks_{genre}"
save_first_chunks(root_folder_path, destination_folder_path)
# print("First chunks saved to the destination folder.")
extracted_files = extractFiles(f"First_Chunks_{genre}")

# Запрос у пользователя на количество файлов для выборки
num_files_to_select = int(input("Введите количество файлов для выборки: "))
selectFiles(f"extract_files_{genre}", num_files_to_select)
splitFiles(f"selected_files_{genre}")


