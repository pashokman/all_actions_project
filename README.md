This framework is a base for a new UI test project  
Framework based on a site - ```https://the-internet.herokuapp.com/```

## Tests that I implemented:
Classes - methods.
* TestAddRemoveElements
    + add 4 elements on a page and assert its count;
    + add 8 elements on a page and remove 5 of them (delete from last added element).

## Steps to develop a base for a UI framework:
* created test functions;
* put test functions in a test class;
* created ```conftest.py``` file and configured a fixture to run tests in multiple browsers - ```chrome, firefox, edge```;
* used this fixture in a base test class and in every test class methods;
* moved application URL and browsers list from fixture into a configuration file - ```config.ini```;
* run tests in parallel;
```
python -m pytest -v -n 3
```
* added custom markers on test classes, to run test vs custom marker;
```
python -m pytest -m add_remove_elements -v -n 3
```
* created page objects for tests;
* added screenshot on failure functionality into allure report:
    + added fixture and hookimpl into ```conftest.py``` file,
    + made driver global in the main fixture (to get acces to it from another fixtures),
    + used log_on_failure fixture to the base test class (to capture screenshot on failure on all child test classes);
* added logging functionality:
    + created logger utility,
    + used it in child page object files (for every page method),
    + added logging of browser name before every test in main fixture,
    + created fixture for every test which will add a row in logs like - Test start, Test completed.
IMPORTANT! Logging works fine only if tests run in single mode (not in paralel).

## Run
To run tests and make an allure report, run first command in VSCode terminal and second in ```cmd``` from root project folder.
```
python -m pytest -m add_remove_elements -v -n 3 --alluredir="./Reports"
allure serve "./Reports"
```