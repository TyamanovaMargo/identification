import os
import shutil

def extract_txt_files(src_dir, dest_dir):
    # Создаем папку назначения, если ее нет
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Проходим по всем подпапкам в исходной папке
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.txt'):
                # Полный путь к исходному файлу
                file_path = os.path.join(root, file)
                # Полный путь к файлу назначения
                dest_path = os.path.join(dest_dir, file)
                # Перемещаем файл
                shutil.move(file_path, dest_path)
                print(f"Файл {file_path} перемещен в {dest_path}")

# Укажите путь к исходной папке и папке назначения
src_directory = '/Users/margotiamanova/Desktop/identification/BOOK/Romance novel/roman_history_love_roman'
dest_directory = '/Users/margotiamanova/Desktop/identification/BOOK/Romance novel'

extract_txt_files(src_directory, dest_directory)


# import os
# import shutil

# def move_folders_up_one_level(root_directory):
#     # Перебираем все элементы в корневой папке
#     for item in os.listdir(root_directory):
#         item_path = os.path.join(root_directory, item)
#         if os.path.isdir(item_path):
#             # Перебираем все подкаталоги в текущем элементе
#             for sub_item in os.listdir(item_path):
#                 sub_item_path = os.path.join(item_path, sub_item)
#                 if os.path.isdir(sub_item_path):
#                     # Перемещаем подкаталог и его содержимое на уровень выше
#                     new_path = os.path.join(root_directory, sub_item)
#                     # Проверяем, не существует ли уже такая папка на уровне выше
#                     if os.path.exists(new_path):
#                         print(f"Skipping {sub_item_path} as {new_path} already exists.")
#                         continue
#                     shutil.move(sub_item_path, new_path)
                    
#             # Удаляем текущий пустой подкаталог
#             if not os.listdir(item_path):
#                 os.rmdir(item_path)

# # Замените '/path/to/your/root/directory' на путь к вашей корневой директории
# root_directory = '/Users/margotiamanova/Desktop/identification/BOOK/Action/action_other'
# move_folders_up_one_level(root_directory)

# # Выводим сообщение об успешном завершении работы скрипта
# print(f"Все папки успешно перемещены на уровень выше в {root_directory}")


