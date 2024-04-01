
import os

from utilities.work_with_files.get_specific_path import get_full_path

def is_file_path_exist(*file_path):
    path = get_full_path(*file_path)
    if os.path.exists(path):
        return True
    else:
        return False