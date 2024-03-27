This framework is about making different UI actions with WEB elements.
Framework based on a site - ```https://the-internet.herokuapp.com/```

## Tests that I implemented:
Classes - methods.
* TestAddRemoveElements
    + add 4 elements on a page and assert its count;
    + add 8 elements on a page and remove 5 of them (delete from last added element).
* TestUploadDownload
    + upload file and check header and file name on successful upload page;
    + 

## Actions that I trained to automate:
* open browser;
* navigate to the page;
* get an element;
* get a list of elements;
* click on element;
* upload file;
* get element text;


## Run
To run tests and make an allure report, run first command in VSCode terminal and second in ```cmd``` from root project folder.
```
python -m pytest -m add_remove_elements -v -n 3 --alluredir="./Reports"
allure serve "./Reports"
```