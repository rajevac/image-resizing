import os
from PIL import Image

path = './assets/'


def print_directory_tree(folder_path):
    """
    Print the names of all directories and subdirectories in a folder.

    Args:
        folder_path (str): The path of the folder to traverse.
    """
    print(folder_path)
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            print_directory_tree(item_path)
        else:
            if not item_path.endswith('.DS_Store'):
                # Split the path into directory path and file name
                end_path, file_name = os.path.split(item_path)
                # Print the directory path and file name
                print("Directory path:", end_path)
                print("File name:", file_name)


print_directory_tree(path)
