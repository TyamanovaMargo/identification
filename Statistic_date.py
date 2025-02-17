# import os
# import pandas as pd

# # Set the directory path
# directory_path = '/Users/margotiamanova/Desktop/identification/all-chunks-separate-folders-all_books_400'
# # Set the file name for the output XLSX file
# output_file_name = 'all_full_chunks_info.xlsx'

# # Initialize an empty list to store data
# data = []

# # Walk through the directory and subdirectories
# for root, dirs, files in os.walk(directory_path):

#     # Get the current directory name as genre
#     genre = os.path.basename(root)

#     # Loop through the files in the current directory
#     for file_name in files:
#         if file_name.endswith(".txt"):
#             # Append genre and file_name as tuple to the data list
#             data.append((genre, file_name))

# # Create DataFrame from data list
# df = pd.DataFrame(data, columns=["Genre", "File Name"])

# # Save the DataFrame to an XLSX file
# df.to_excel(output_file_name, index=False, engine='openpyxl')



import os
import pandas as pd

# Set the directory path
directory_path = '/Users/margotiamanova/Desktop/identification/all-chunks-separate-folders-all_genres_300'
# Set the file name for the output XLSX file
output_file_name = 'all_full_chunks_info_300.xlsx'

# Initialize an empty list to store data
data = []

# Walk through the directory and subdirectories
for genre_folder in os.listdir(directory_path):
    genre_path = os.path.join(directory_path, genre_folder)
    if os.path.isdir(genre_path):
        for book_folder in os.listdir(genre_path):
            book_path = os.path.join(genre_path, book_folder)
            if os.path.isdir(book_path):
                for file_name in os.listdir(book_path):
                    if file_name.endswith(".txt"):
                        # Append genre, book name, and file name as tuple to the data list
                        data.append((genre_folder, book_folder, file_name))

# Create DataFrame from data list
df = pd.DataFrame(data, columns=["Genre", "Book Name", "File Name"])

# Save the DataFrame to an XLSX file
df.to_excel(output_file_name, index=False, engine='openpyxl')
