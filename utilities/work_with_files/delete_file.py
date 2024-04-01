import os

from utilities.work_with_files.get_specific_path import get_full_path


def delete_file(*file_path):
    path = get_full_path(*file_path)
    if os.path.exists(path):
        os.remove(path)
        return True
    else:
        return False