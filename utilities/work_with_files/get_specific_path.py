import os

from utilities.work_with_files.base_folder_path import BASE_DIR


def get_full_path(*path_from_base_folder):
    # should pass path like this - 'files', 'file.py'
    return os.path.join(BASE_DIR, *path_from_base_folder)