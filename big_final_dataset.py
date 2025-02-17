# import os
# import shutil

# def collect_pos_files(root_dir, output_dir):
#     # Проверка существования выходной директории, создание, если не существует
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     # Проход по всем папкам в корневом каталоге
#     for folder in os.listdir(root_dir):
#         folder_path = os.path.join(root_dir, folder)

#         # Проверка, является ли это папкой
#         if os.path.isdir(folder_path):
#             test_pos_dir = os.path.join(folder_path, 'test', 'pos')

#             # Проверка существования директории pos в папке test
#             if os.path.exists(test_pos_dir):
#                 for filename in os.listdir(test_pos_dir):
#                     file_path = os.path.join(test_pos_dir, filename)

#                     # Проверка, является ли это файлом
#                     if os.path.isfile(file_path):
#                         shutil.copy(file_path, output_dir)
#                         print(f'Скопирован файл: {file_path}')

# # Укажите корневую директорию, содержащую 11 папок
# root_dir = '/Users/margotiamanova/Desktop/identification/DATASET_ACTUAL _With_punctuation/detective_dataset_new2'

# # Укажите директорию для сохранения всех pos файлов
# output_dir = '/Users/margotiamanova/Desktop/identification/FINAL_dataset_punctuation'

# collect_pos_files(root_dir, output_dir)




# import os
# import shutil

# def collect_pos_files(root_dir, output_dir):
#     # Проверка существования выходной директории, создание, если не существует
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     # Словарь для хранения количества скопированных файлов для каждой папки
#     copied_files_count = {}

#     # Проход по всем папкам в корневом каталоге
#     for folder in os.listdir(root_dir):
#         folder_path = os.path.join(root_dir, folder)

#         # Проверка, является ли это папкой
#         if os.path.isdir(folder_path):
#             test_pos_dir = os.path.join(folder_path, 'test', 'pos')

#             # Проверка существования директории pos в папке test
#             if os.path.exists(test_pos_dir):
#                 files_copied = 0
#                 for filename in os.listdir(test_pos_dir):
#                     file_path = os.path.join(test_pos_dir, filename)

#                     # Проверка, является ли это файлом
#                     if os.path.isfile(file_path):
#                         shutil.copy(file_path, output_dir)
#                         files_copied += 1
#                         print(f'Скопирован файл: {file_path}')

#                 # Сохранение количества скопированных файлов для текущей папки
#                 copied_files_count[folder] = files_copied

#     # Печать информации о количестве скопированных файлов из каждой папки
#     print("\nРезультаты копирования:")
#     for folder, count in copied_files_count.items():
#         print(f'Из папки {folder} скопировано {count} файлов')

# # Укажите корневую директорию, содержащую 11 папок
# root_dir = '/Users/margotiamanova/Desktop/identification/DATASET_ACTUAL _With_punctuation'

# # Укажите директорию для сохранения всех pos файлов
# output_dir = '/Users/margotiamanova/Desktop/identification/FINAL_dataset_punctuation'

# collect_pos_files(root_dir, output_dir)


import os
import shutil

def collect_pos_files(root_dir, output_dir):
    # Проверка существования выходной директории, создание, если не существует
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Словарь для хранения количества скопированных файлов для каждой папки
    copied_files_count = {}
    total_files_copied = 0

    # Проход по всем папкам в корневом каталоге
    for folder in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder)

        # Проверка, является ли это папкой
        if os.path.isdir(folder_path):
            test_pos_dir = os.path.join(folder_path, 'test', 'pos')

            # Проверка существования директории pos в папке test
            if os.path.exists(test_pos_dir):
                files_copied = 0
                for filename in os.listdir(test_pos_dir):
                    file_path = os.path.join(test_pos_dir, filename)

                    # Проверка, является ли это файлом
                    if os.path.isfile(file_path):
                        shutil.copy(file_path, output_dir)
                        files_copied += 1
                        total_files_copied += 1
                        print(f'Скопирован файл: {file_path}')
                    else:
                        print(f'Пропущен (не файл): {file_path}')

                # Сохранение количества скопированных файлов для текущей папки
                copied_files_count[folder] = files_copied
            else:
                print(f'Папка {test_pos_dir} не существует')
        else:
            print(f'{folder_path} не является папкой')

    # Печать информации о количестве скопированных файлов из каждой папки
    print("\nРезультаты копирования:")
    for folder, count in copied_files_count.items():
        print(f'Из папки {folder} скопировано {count} файлов')

    # Печать общего количества скопированных файлов
    print(f'\nОбщее количество скопированных файлов: {total_files_copied}')

# Укажите корневую директорию, содержащую 11 папок
root_dir = '/Users/margotiamanova/Desktop/identification/Dataset_without_punctuation_noDouble/Dataset_action'

# Укажите директорию для сохранения всех pos файлов
output_dir = '/Users/margotiamanova/Desktop/identification/Multilabel_dataset/action'

collect_pos_files(root_dir, output_dir)
