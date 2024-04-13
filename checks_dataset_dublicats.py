import os

def delete_matching_files(test_folder, train_folder):
    deleted_files_count = 0
    for test_type in os.listdir(test_folder):  # Проверяем и для test/pos и для test/neg
        if test_type.startswith('.'):  # Пропускаем скрытые файлы
            continue
        test_type_folder = os.path.join(test_folder, test_type)
        if not os.path.isdir(test_type_folder):
            continue
        for test_file_name in os.listdir(test_type_folder):
            if test_file_name.endswith('.txt'):
                test_file_path = os.path.join(test_type_folder, test_file_name)
                for train_type in os.listdir(train_folder):  # Проверяем и для train/pos и для train/neg
                    if train_type.startswith('.'):  # Пропускаем скрытые файлы
                        continue
                    train_type_folder = os.path.join(train_folder, train_type)
                    if not os.path.isdir(train_type_folder):
                        continue
                    for train_file_name in os.listdir(train_type_folder):
                        if train_file_name.endswith('.txt'):
                            train_file_path = os.path.join(train_type_folder, train_file_name)
                            # Сравниваем содержимое файлов
                            if are_files_identical(test_file_path, train_file_path):
                                os.remove(train_file_path)
                                deleted_files_count += 1
                                print(f"Удален файл {train_file_name} из папки train/{train_type}.")
    return deleted_files_count

def are_files_identical(file_path1, file_path2):
    with open(file_path1, 'r', encoding='utf-8') as file1, open(file_path2, 'r', encoding='utf-8') as file2:
        return file1.read() == file2.read()

def main(data_folder):
    # Папка test
    test_folder = os.path.join(data_folder, 'test')
    # Папка train
    train_folder = os.path.join(data_folder, 'train')

    # Удаление совпадающих файлов
    deleted_files_count = delete_matching_files(test_folder, train_folder)

    print(f"Удалено {deleted_files_count} файлов из папок train.")

if __name__ == "__main__":
    data_folder = input("Введите путь к папке, содержащей папки train и test: ")
    main(data_folder)
