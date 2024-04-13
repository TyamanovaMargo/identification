import os
import pandas as pd

# Set the directory path
directory_path = '/Users/margotiamanova/Desktop/identification/BOOK/Action'

# Set the file name for the output XLSX file
output_file_name = 'output.xlsx'

# Initialize an empty list to store data
data = []

# Walk through the directory and subdirectories
for root, dirs, files in os.walk(directory_path):

    # Get the current directory name as genre
    genre = os.path.basename(root)

    # Loop through the files in the current directory
    for file_name in files:
        if file_name.endswith(".txt"):
            # Append genre and file_name as tuple to the data list
            data.append((genre, file_name))

# Create DataFrame from data list
df = pd.DataFrame(data, columns=["Genre", "File Name"])

# Save the DataFrame to an XLSX file
df.to_excel(output_file_name, index=False, engine='openpyxl')
