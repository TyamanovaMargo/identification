# import re
# import os
# import shutil
# import charset_normalizer

# genre = "all_books_with_punctuation"

# # Base folder path (change this to your actual base folder)
# BASE_FOLDER = "/Users/margotiamanova/Desktop/identification/BOOK"

# # Output folder path after encoding
# AFTER_ENCODING = f"/Users/margotiamanova/Desktop/identification/result/after-encoding {genre}"

# # Output folder path
# WITHOUT_AUTHOR_NAME = f"/Users/margotiamanova/Desktop/identification/result/without-author-name-{genre}"

# # Output folder path for storing chunks in separate folders
# RESULT = f"/Users/margotiamanova/Desktop/identification/result/all-chunks-separate-folders-{genre}"



# #======================================================================================================
#    # step 1: encodeing files 
# #======================================================================================================
# # Function to detect encoding and rewrite files with UTF-8 encoding
# def rewrite_with_utf8_encoding(input_file, output_file):
#     with open(input_file, 'rb') as f:
#         content_bytes = f.read()

#     detected = charset_normalizer.detect(content_bytes)
#     encoding = detected['encoding']

#     try:
#         with open(input_file, 'r', encoding=encoding) as f:
#             content_text = f.read()

#         # Encode problematic characters in the output file path
#         output_file_encoded = output_file.encode('utf-8', errors='ignore').decode('utf-8')

#         # Ensure the directory structure exists
#         os.makedirs(os.path.dirname(output_file_encoded), exist_ok=True)

#         # Open the output file in 'utf-8' mode and prevent newline characters from being added
#         with open(output_file_encoded, 'w', encoding='utf-8', newline='') as f:
#             f.write(content_text)
#         #print(f"Rewritten: {input_file} to {output_file_encoded}")

#     except UnicodeDecodeError:
#         print(f"Error decoding {input_file}. Skipping...")


# def rename_folders(input_folder, prefixes):
#     for root, dirs, _ in os.walk(input_folder):
#         for dir_name in dirs:
#             for prefix in prefixes:
#                 if dir_name.startswith(prefix):
#                     original_path = os.path.join(root, dir_name)
#                     new_dir_name = dir_name[len(prefix):]  # Remove the prefix
#                     new_path = os.path.join(root, new_dir_name)
#                     os.rename(original_path, new_path)
#                     print(f"Renamed {dir_name} to {new_dir_name}")

# def copy_and_rewrite_txt_files(input_folder, after_encoding):
#     # First, remove the prefix from folder names
#     rename_folders(input_folder, ['download_books_', 'download_book_'])
    
#     total_files = 0  # To keep track of the total number of files processed
#     success_count = 0  # To count the successfully rewritten files
#     error_count = 0  # To count the files with decoding errors

#     for root, _, files in os.walk(input_folder):
#         for filename in files:
#             if filename.endswith(".txt"):
#                 input_file = os.path.join(root, filename)
#                 relative_path = os.path.relpath(input_file, input_folder)
#                 output_file = os.path.join(after_encoding, relative_path)

#                 # Copy and rewrite the file (or skip if there's a decoding error)
#                 try:
#                     rewrite_with_utf8_encoding(input_file, output_file)
#                     success_count += 1
#                 except UnicodeDecodeError:
#                     print(f"Error decoding {input_file}. Skipping...")
#                     error_count += 1

#                 total_files += 1

#     # Print summary information if needed
#     print(f"Finished rewriting files. Total files processed: {total_files}, Successfully rewritten: {success_count}, Files with decoding errors: {error_count}")




# #======================================================================================================
#     # step 2: remove author name 
# #======================================================================================================

# # Function to process a book file and extract author name
# def process_book(book_path):
#     with open(book_path, 'r', encoding='utf-8') as file:
#         # Initialize a line counter
#         line_count = 0
#         author_name = ''

#         # Iterate through each line in the file
#         for line in file:
#             # Increment the line counter
#             line_count += 1

#             # Check if this is the second line
#             if line_count == 2:
#                 # Extract author name from the second line
#                 author_name = line.strip()
#                 break

#         return author_name
# # Traverse the directory structure under the base folder
# def remove_author_name(after_encoding,without_author_name ):
#     for root, dirs, files in os.walk(after_encoding):
#         for file_name in files:
#             # Check if the file is a book (you can add more conditions if needed)
#             if file_name.endswith('.txt'):
#                 # Construct the full path to the book file
#                 book_path = os.path.join(root, file_name)

#                 # Process the book file and get the author name
#                 author_name = process_book(book_path)
                
#                 # Print the author's name
#                 print(f"Author of {file_name}: {author_name}")
#                 # Create the corresponding directory structure in the chunks folder
#                 relative_path = os.path.relpath(root, after_encoding)
#                 output_dir = os.path.join(without_author_name, relative_path)
#                 os.makedirs(output_dir, exist_ok=True)

#                 # Construct the path for the output file in the chunks folder
#                 output_file_path = os.path.join(output_dir, file_name)

#                 # Open the input file for reading and the output file for writing
#                 with open(book_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
#                     for line in infile:
#                         # Check if the line contains any of the specified words
#                         if not any(word in line for word in author_name.split()):
#                             # If none of the words are found, write the line to the output file
#                             outfile.write(line)

#                 print(f"Processed '{file_name}' and saved to '{output_file_path}'")



# #======================================================================================================
#     # step 3: create chunks for all txt (books) filesinput_folder 
# #======================================================================================================

# # Function to tokenize and split text into chunks

# def tokenize_and_split_text(text, target_words=400):
#     # Tokenize the text into sentences
#     sentences = re.split(r'(?<=[.!?]) +', text)

#     # Split into chunks based on target number of words per chunk
#     current_chunk = []
#     chunks = []

#     for sentence in sentences:
#         words = sentence.split()
#         current_chunk.extend(words)
#         if len(current_chunk) >= target_words:
#             chunks.append(current_chunk)
#             current_chunk = []
    
#     # Add any remaining words to the last chunk
#     if current_chunk:
#         chunks.append(current_chunk)

#     return chunks



# def split_to_chunks(without_author_name, result):
#     # Create the output folder if it doesn't exist
#     os.makedirs(result, exist_ok=True)
 
#     # Iterate through subfolders and files in the input folder
#     for root, dirs, files in os.walk(without_author_name):
#         for file_name in files:
#             if file_name.endswith('.txt'):
#                 # Construct the full path to the book file
#                 book_path = os.path.join(root, file_name)
               
#                 # Read the book's text content
#                 with open(book_path, 'r', encoding='utf-8') as file:
#                     text = file.read()

#                 # Tokenize and split the text into chunks
#                 chunks = tokenize_and_split_text(text) # тут с оригинальной функцией
                
#                 # Create a folder structure similar to "without_author_name" in "all_chunks_separate_folders"
#                 relative_path = os.path.relpath(root, without_author_name)
#                 output_subfolder = os.path.join(result, relative_path)

#                 # Ensure the corresponding subfolder structure exists in "all_chunks_separate_folders"
#                 os.makedirs(output_subfolder, exist_ok=True)

#                 # Create a dictionary to track chunks with the same name
#                 chunks_by_name = {}

#                 # remove .txt from file name
#                 file_name_without_extension = file_name.replace(".txt", "")
#                 #print(file_name_without_extension)

#                 # # Write chunks to separate files in the subfolder
#                 # for i, chunk in enumerate(chunks):
#                 #     chunk_name = f'{file_name_without_extension}_chunk_{i + 1}.txt'
#                 #     chunk_path = os.path.join(output_subfolder, chunk_name)
#                 # Write chunks to separate files in the subfolder
#                 for i, chunk in enumerate(chunks):
#                     chunk_word_count = len(chunk)  # Get the word count of the chunk
#                     chunk_name = f'{file_name_without_extension}_chunk_{i + 1}_words_{chunk_word_count}.txt'  # Add word count to the filename
#                     chunk_path = os.path.join(output_subfolder, chunk_name)

#                     # Write the chunk content to the file
#                     with open(chunk_path, 'w', encoding='utf-8') as chunk_file:
#                         chunk_file.write(' '.join(chunk))

#                     # Extract the base file name without extension
#                     base_file_name = os.path.splitext(file_name)[0]

#                     if base_file_name not in chunks_by_name:
#                         chunks_by_name[base_file_name] = []

#                     chunks_by_name[base_file_name].append(chunk_path)

#                     with open(chunk_path, 'w', encoding='utf-8') as chunk_file:
#                         chunk_file.write(' '.join(chunk))

#                 # Create a folder for each base file name and move the chunks there
#                 for base_file_name, chunk_paths in chunks_by_name.items():
#                     base_file_folder = os.path.join(output_subfolder, base_file_name)
#                     os.makedirs(base_file_folder, exist_ok=True)

#                     for chunk_path in chunk_paths:
#                         chunk_file_name = os.path.basename(chunk_path)
#                         dest_chunk_path = os.path.join(base_file_folder, chunk_file_name)

#                         # Move the chunk file to the folder named after the base file name
#                         shutil.move(chunk_path, dest_chunk_path)



# if __name__ == "__main__":
#     # step 1: encodeing files 
#     copy_and_rewrite_txt_files(BASE_FOLDER, AFTER_ENCODING)
#     # step 2: remove author name 
#     remove_author_name(AFTER_ENCODING,WITHOUT_AUTHOR_NAME)
#     # step 3: create chunks for all txt (books) filesinput_folder
#     split_to_chunks(WITHOUT_AUTHOR_NAME,RESULT)

import re
import os
import shutil
import charset_normalizer

genre = "all_genres_300"

# Base folder path (change this to your actual base folder)
BASE_FOLDER = "/Users/margotiamanova/Desktop/identification/BOOK"

# Output folder path after encoding
AFTER_ENCODING = f"/Users/margotiamanova/Desktop/identification/result/after-encoding {genre}"

# Output folder path
WITHOUT_AUTHOR_NAME = f"/Users/margotiamanova/Desktop/identification/result/without-author-name-{genre}"

# Output folder path for storing chunks in separate folders
RESULT = f"/Users/margotiamanova/Desktop/identification/result/all-chunks-separate-folders-{genre}"



#======================================================================================================
   # step 1: encodeing files 
#======================================================================================================
# Function to detect encoding and rewrite files with UTF-8 encoding
def rewrite_with_utf8_encoding(input_file, output_file):
    with open(input_file, 'rb') as f:
        content_bytes = f.read()

    detected = charset_normalizer.detect(content_bytes)
    encoding = detected['encoding']

    try:
        with open(input_file, 'r', encoding=encoding) as f:
            content_text = f.read()

        # Encode problematic characters in the output file path
        output_file_encoded = output_file.encode('utf-8', errors='ignore').decode('utf-8')

        # Ensure the directory structure exists
        os.makedirs(os.path.dirname(output_file_encoded), exist_ok=True)

        # Open the output file in 'utf-8' mode and prevent newline characters from being added
        with open(output_file_encoded, 'w', encoding='utf-8', newline='') as f:
            f.write(content_text)
        #print(f"Rewritten: {input_file} to {output_file_encoded}")

    except UnicodeDecodeError:
        print(f"Error decoding {input_file}. Skipping...")


def rename_folders(input_folder, prefixes):
    for root, dirs, _ in os.walk(input_folder):
        for dir_name in dirs:
            for prefix in prefixes:
                if dir_name.startswith(prefix):
                    original_path = os.path.join(root, dir_name)
                    new_dir_name = dir_name[len(prefix):]  # Remove the prefix
                    new_path = os.path.join(root, new_dir_name)
                    os.rename(original_path, new_path)
                    print(f"Renamed {dir_name} to {new_dir_name}")

def copy_and_rewrite_txt_files(input_folder, after_encoding):
    # First, remove the prefix from folder names
    rename_folders(input_folder, ['download_books_', 'download_book_'])
    
    total_files = 0  # To keep track of the total number of files processed
    success_count = 0  # To count the successfully rewritten files
    error_count = 0  # To count the files with decoding errors

    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.endswith(".txt"):
                input_file = os.path.join(root, filename)
                relative_path = os.path.relpath(input_file, input_folder)
                output_file = os.path.join(after_encoding, relative_path)

                # Copy and rewrite the file (or skip if there's a decoding error)
                try:
                    rewrite_with_utf8_encoding(input_file, output_file)
                    success_count += 1
                except UnicodeDecodeError:
                    print(f"Error decoding {input_file}. Skipping...")
                    error_count += 1

                total_files += 1

    # Print summary information if needed
    print(f"Finished rewriting files. Total files processed: {total_files}, Successfully rewritten: {success_count}, Files with decoding errors: {error_count}")




#======================================================================================================
    # step 2: remove author name 
#======================================================================================================

# Function to process a book file and extract author name
def process_book(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        # Initialize a line counter
        line_count = 0
        author_name = ''

        # Iterate through each line in the file
        for line in file:
            # Increment the line counter
            line_count += 1

            # Check if this is the second line
            if line_count == 2:
                # Extract author name from the second line
                author_name = line.strip()
                break

        return author_name
# Traverse the directory structure under the base folder
def remove_author_name(after_encoding,without_author_name ):
    for root, dirs, files in os.walk(after_encoding):
        for file_name in files:
            # Check if the file is a book (you can add more conditions if needed)
            if file_name.endswith('.txt'):
                # Construct the full path to the book file
                book_path = os.path.join(root, file_name)

                # Process the book file and get the author name
                author_name = process_book(book_path)
                
                # Print the author's name
                print(f"Author of {file_name}: {author_name}")
                # Create the corresponding directory structure in the chunks folder
                relative_path = os.path.relpath(root, after_encoding)
                output_dir = os.path.join(without_author_name, relative_path)
                os.makedirs(output_dir, exist_ok=True)

                # Construct the path for the output file in the chunks folder
                output_file_path = os.path.join(output_dir, file_name)

                # Open the input file for reading and the output file for writing
                with open(book_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
                    for line in infile:
                        # Check if the line contains any of the specified words
                        if not any(word in line for word in author_name.split()):
                            # If none of the words are found, write the line to the output file
                            outfile.write(line)

                print(f"Processed '{file_name}' and saved to '{output_file_path}'")



#======================================================================================================
    # step 3: create chunks for all txt (books) filesinput_folder 
#======================================================================================================

# Function to tokenize and split text into chunks

def tokenize_and_split_text(text, target_words=300):
    # Tokenize the text into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)

    # Split into chunks based on target number of words per chunk
    current_chunk = []
    chunks = []

    for sentence in sentences:
        # Remove punctuation from the sentence
        sentence = re.sub(r'[^\w\s]', '', sentence)
        words = sentence.split()
        current_chunk.extend(words)
        if len(current_chunk) >= target_words:
            chunks.append(current_chunk)
            current_chunk = []
    
    # Add any remaining words to the last chunk
    if current_chunk:
        chunks.append(current_chunk)

    return chunks



def split_to_chunks(without_author_name, result):
    # Create the output folder if it doesn't exist
    os.makedirs(result, exist_ok=True)
 
    # Iterate through subfolders and files in the input folder
    for root, dirs, files in os.walk(without_author_name):
        for file_name in files:
            if file_name.endswith('.txt'):
                # Construct the full path to the book file
                book_path = os.path.join(root, file_name)
               
                # Read the book's text content
                with open(book_path, 'r', encoding='utf-8') as file:
                    text = file.read()

                # Tokenize and split the text into chunks
                chunks = tokenize_and_split_text(text) # тут с оригинальной функцией
                
                # Create a folder structure similar to "without_author_name" in "all_chunks_separate_folders"
                relative_path = os.path.relpath(root, without_author_name)
                output_subfolder = os.path.join(result, relative_path)

                # Ensure the corresponding subfolder structure exists in "all_chunks_separate_folders"
                os.makedirs(output_subfolder, exist_ok=True)

                # Create a dictionary to track chunks with the same name
                chunks_by_name = {}

                # remove .txt from file name
                file_name_without_extension = file_name.replace(".txt", "")
                #print(file_name_without_extension)

                # # Write chunks to separate files in the subfolder
                # for i, chunk in enumerate(chunks):
                #     chunk_name = f'{file_name_without_extension}_chunk_{i + 1}.txt'
                #     chunk_path = os.path.join(output_subfolder, chunk_name)
                # Write chunks to separate files in the subfolder
                for i, chunk in enumerate(chunks):
                    chunk_word_count = len(chunk)  # Get the word count of the chunk
                    chunk_name = f'{file_name_without_extension}_chunk_{i + 1}_words_{chunk_word_count}.txt'  # Add word count to the filename
                    chunk_path = os.path.join(output_subfolder, chunk_name)

                    # Write the chunk content to the file
                    with open(chunk_path, 'w', encoding='utf-8') as chunk_file:
                        chunk_file.write(' '.join(chunk))

                    # Extract the base file name without extension
                    base_file_name = os.path.splitext(file_name)[0]

                    if base_file_name not in chunks_by_name:
                        chunks_by_name[base_file_name] = []

                    chunks_by_name[base_file_name].append(chunk_path)

                    with open(chunk_path, 'w', encoding='utf-8') as chunk_file:
                        chunk_file.write(' '.join(chunk))

                # Create a folder for each base file name and move the chunks there
                for base_file_name, chunk_paths in chunks_by_name.items():
                    base_file_folder = os.path.join(output_subfolder, base_file_name)
                    os.makedirs(base_file_folder, exist_ok=True)

                    for chunk_path in chunk_paths:
                        chunk_file_name = os.path.basename(chunk_path)
                        dest_chunk_path = os.path.join(base_file_folder, chunk_file_name)

                        # Move the chunk file to the folder named after the base file name
                        shutil.move(chunk_path, dest_chunk_path)



if __name__ == "__main__":
    # step 1: encodeing files 
    copy_and_rewrite_txt_files(BASE_FOLDER, AFTER_ENCODING)
    # step 2: remove author name 
    remove_author_name(AFTER_ENCODING,WITHOUT_AUTHOR_NAME)
    # step 3: create chunks for all txt (books) filesinput_folder
    split_to_chunks(WITHOUT_AUTHOR_NAME,RESULT)