import os
import shutil

def process_file(source_path, destination_path):
    with open(source_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    lower_content = content.lower()
    
    with open(destination_path, 'w', encoding='utf-8') as file:
        file.write(lower_content)

def process_directory(source_directory, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    for root, _, files in os.walk(source_directory):
        relative_path = os.path.relpath(root, source_directory)
        dest_dir = os.path.join(destination_directory, relative_path)
        
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        for file in files:
            if file.endswith('.txt'):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(dest_dir, file)
                process_file(source_path, destination_path)

# Укажите пути к вашей исходной и целевой папкам
source_directory = '/Users/margotiamanova/Desktop/identification/DATASET_ACTUAL _With_punctuation/romance_dataset_new'
destination_directory = '/Users/margotiamanova/Desktop/identification/romanc_lowcase_punctuation'

process_directory(source_directory, destination_directory)
#lowcase2
