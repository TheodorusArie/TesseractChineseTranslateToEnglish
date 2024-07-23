import os

def rename_files_in_directory(directory_path, page_number):
    # List all files in the directory
    files = os.listdir(directory_path)
    
    # Sort the files in ascending order
    files.sort()

    for i, filename in enumerate(files):
        current_page = page_number
        old_file_path = os.path.join(directory_path, filename)
        new_file_name = f"{current_page}{os.path.splitext(filename)[1]}"
        
        new_file_path = os.path.join(directory_path, new_file_name)
        
        os.rename(old_file_path, new_file_path)
        
        print(f"Renamed: {old_file_path} to {new_file_path}")
        page_number += 1


directory_path = "image/lastChap"
page_number = 100255
rename_files_in_directory(directory_path, page_number)
