This framework is about making different UI actions with WEB elements.
Framework based on a site - ```https://the-internet.herokuapp.com/```

## Tests that I implemented:
Classes - methods.
* TestAddRemoveElements
    + add 4 elements on a page and assert its count;
    + add 8 elements on a page and remove 5 of them (delete from last added element).
* TestUploadDownload
    + upload file and check header and file name on successful upload page;
    + download file and check if file exists on a disk, delete file and check if file disapired from a disk.
* TestBasicAuth
    + basic auth handling.
* TestBrokenImagesLinks
    + find broken images;
    + find broken links/
* TestCheckboxes
    + select checkboxes;
    + deselect checkboxes;
    + check if checkbox is checked.
* TestContextMenuAndAlert
    + right mouse button click;
    + get alert text;
    + accept alert.
* TestGeolocation
    + find geolocation and compate it vs expeced.
* TestHorizontalSlider
    + test_slide_to_the_right;
    + test_slide_to_the_left.
* TestHovers
    + test_click_on_hover_element.

## Actions that I trained to automate:
* open browser;
* navigate to the page;
* get an element;
* get a list of elements;
* click on element;
* get element text;
* upload file; 
<details>

To make this action, we should use method ```send_keys``` and put into this method ```file_path```, and before it we should specify the absolute file path.
```
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_UPLOAD_PATH = os.path.join(BASE_DIR, 'files', 'file_to_upload.txt')

element.send_keys(FILE_UPLOAD_PATH)
```
</details>

* download file; 
<details>

To make this action, we should add options to the driver for download files:
```
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as COptions
from selenium.webdriver.firefox.options import Options as FOptions
from selenium.webdriver.edge.options import Options as EOptions

if request.param == "chrome":
    chrome_options = COptions()
    chrome_options.add_experimental_option('prefs', {'download.default_directory': FILES_FOLDER_PATH})
    driver = webdriver.Chrome(options=chrome_options)
elif request.param == "firefox":
    firefox_options = FOptions()
    firefox_options.set_preference('browser.download.folderList', 2)
    firefox_options.set_preference('browser.download.manager.showWhenStarting', False)
    firefox_options.set_preference('browser.download.dir', FILES_FOLDER_PATH)
    firefox_options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')
    driver = webdriver.Firefox(options=firefox_options)
elif request.param == "edge":
    edge_options = EOptions()
    edge_options.add_experimental_option('prefs', {'download.default_directory': FILES_FOLDER_PATH})
    driver = webdriver.Edge(options=edge_options)
```
</details>

* wait file for download;  
<details>

To make this action we should create the untility and use it after clicking on file download button:
```
import os
import time

def wait_for_download(download_path, file_name, timeout):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if os.path.exists(os.path.join(download_path, file_name)):
            return True
        time.sleep(1)
    return False
```
</details>

* get file name from a path;  
<details>

To make this action we should get full path to the file (from root project folder) and ```split``` full path and get last item:
```
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def get_file_name_from_path(path):
    return path.split('\\')[-1]
```
</details>

* check if file exists on a disk;  
<details>

To make this action we should get full path to the file (from root project folder) and use function ```os.path.exists(path)``` to check if file or path exists:
```
import os

def get_full_path(*path_from_base_folder):
    # should pass path like this - 'files', 'file.py'
    return os.path.join(BASE_DIR, *path_from_base_folder)

def is_file_path_exist(*file_path):
    path = get_full_path(*file_path)
    if os.path.exists(path):
        return True
    else:
        return False
```
</details>

* delete file from a disk;  
<details>

To make this action we should check if file exists and if it's true, we should remove it using function ```os.remove(path)```:
```
def delete_file(*file_path):
    path = get_full_path(*file_path)
    if os.path.exists(path):
        os.remove(path)
        return True
    else:
        return False
```
</details>

* basic auth in window pop-up;  
To make this action we should add login and password before the url, like - ```https://{login}:{pwd}@{url}``` and go to this URL.

* check for broken images/links;  
To make this action we should get a list of all images/likns on the page and use requests.get() method to access to these objects, if we got for example status_code >= 404, it is a broken image/link.

* selects/deselect checkboxes or radio buttons;  
To make these action we should check if checkbox/redao button is checked, using method - ```element.is_selected()``` and then make necessary action (click/pass).

* right click and alert handling;  
<details>

To make these actions we should create an instances of ActionChain and Alert and work with these instances:
```
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

def open_context_menu(self):
    self.actionChains.context_click(self.get_element('MENU_AREA_ID', self.MENU_AREA_ID)).perform()
    CONTEXT_MENU.debug('')

def get_alert_message(self):
    return self.alert.text

def accept_the_alert(self):
    self.alert.accept()
```
</details>

* geolocation handling;  
<details>

To work with geolocation we should add additional options for our drivers in ```conftest.py``` and accept promts.
```
if request.param == "chrome":
    chrome_options = COptions()
    chrome_options.add_argument("--disable-infobars")
    # Pass the argument 1 to allow and 2 to block
    chrome_options.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.geolocation": 1, 
    })
    driver = webdriver.Chrome(options=chrome_options)
elif request.param == "firefox":
    # Set the preference to allow geolocation
    firefox_options.set_preference("geo.enabled", True)
    firefox_options.set_preference("geo.prompt.testing", True)
    firefox_options.set_preference("geo.prompt.testing.allow", True)
    # SET COORDINATES MANUALLY
    firefox_options.set_preference('geo.provider.network.url',
        'data:application/json,{"location": {"lat": 48.699, "lng": 26.584}, "accuracy": 100.0}')
    driver = webdriver.Firefox(options=firefox_options)
elif request.param == "edge":
    edge_options = EOptions()
    edge_options.add_argument("--enable-features=AllowGeolocationOnInsecureOrigins")
    driver = webdriver.Edge(options=edge_options)
else:
    raise ValueError(f"Unsupported browser: {request.param}")
```
</details>

* slider handling;  
<details>

To work with sliders we should use ```ActionChains - drag_and_drop_by_offset``` method.
!!!IMPORTANT!!! In firefox browser we should pick up different coordinates than in chrome and edge.
```
ActionChains(driver)\
    .drag_and_drop_by_offset(element, Xpixels, Ypixels)\
    .perform()
```
</details>

* hovers handling;  
<details>

To work with hovers we should use ```ActionChains - move_to_element``` method. First things first we should move to main element, than we should find next element and move to it... 
```
actions = ActionChains(driver)
actions.move_to_element(users[user_number-1]).perform()
```
</details>

## Run
To run tests and make an allure report, run first command in VSCode terminal and second in ```cmd``` from root project folder.
```
python -m pytest -m add_remove_elements -v -n 3 --alluredir="./Reports"
allure serve "./Reports"
```