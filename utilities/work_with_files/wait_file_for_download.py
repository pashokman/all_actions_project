import os
import time


def wait_for_download(download_path, timeout):
    # Get the initial set of files in the directory
    initial_files = set(os.listdir(download_path))
    
    # Wait until a new file appears or until timeout is reached
    start_time = time.time()
    while time.time() - start_time < timeout:
        current_files = set(os.listdir(download_path))
        new_files = current_files - initial_files
        if new_files:
            return True
        time.sleep(1)  # Check every second
    return False