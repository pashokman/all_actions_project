import os
import time


def wait_for_download(download_path, file_name, timeout):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if os.path.exists(os.path.join(download_path, file_name)):
            return True
        time.sleep(1)
    return False