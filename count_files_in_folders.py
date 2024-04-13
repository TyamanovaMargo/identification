import os

def count_txt_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                count += 1
    return count

# Specify the path to your main folder
main_folder_path = "/Users/margotiamanova/Desktop/identification/classic_dataset_new"
# Concatenate the main folder path with "train" and "test" folders
train_folder_path = os.path.join(main_folder_path, "train")
test_folder_path = os.path.join(main_folder_path, "test")

# Call the function for "train" and "test" folders
train_count = count_txt_files(train_folder_path)
test_count = count_txt_files(test_folder_path)

# Display the counts
print("Total number of .txt files in 'train' folder:", train_count)
print("Total number of .txt files in 'test' folder:", test_count)
