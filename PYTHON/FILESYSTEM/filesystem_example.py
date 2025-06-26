import os

def list_files_in_directory(path):
    if not os.path.exists(path):
        return []
    return os.listdir(path)
