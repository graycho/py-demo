import os

# folder path
folder_path = 'files'

# loop all files
for file_name in os.listdir(folder_path):

    # only markdown
    if file_name.endswith('.md') or file_name.endswith('.markdown'):
        # prind file name
        print(file_name)
