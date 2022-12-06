1) creation of file test_task.py in the package tests
2) implement the method example
3) Executer les tests a travers la commande:
 - pytest o pytest -v

4) Create the class (prefixed Test) test_check_description_task:
   - Package core + file task.py
  
5) To execute a precise test with pytest:
   - pytest -v tests/test_task.py::TestTask::test_check_description_task

6) Implement the setup and teardown methods
7) Default: no display of messages from setup and teardown except if launched with the command:
   - pytest -v -s
8) Implement the methods etup_class and teardown_class
9) Let´s add some marcadores(catgorize or marcar the tests). 1 marcador se puede asignar a 1 o varias pruebas.
10) Execute the tests of the marked ones test_id_task:
    - pytest -v tests/test_task.py -m tests_id_task
    - pytest -v -s -m tests_id_task
11) What to do with the warnings ? Can be corrected by creating a config file pytest.ini in the root directory of the project
12) Implement tests with skip and skipif and execute:
    - pytest -v -s
13) Parameters in tests



# Test Reporting

14) How to export these tests ?
15) Use of the library Excel reporting  (pip install pytest-excel)
   - py.test --excelreport=test_reporting.xls --verbose
16) Use of library HTML reporter (pip install pytest-html-reporter):
   - pytest -v tests/ --html-report=reports/test_reporting.html --title="course testing"  
17) others: Allure framework - https://docs.qameta.io/allure/



# Coverage
18) nstallation of library coverage to analyze the source code and its test covering
19) Check the source code for task.py over coverage:
   - coverage run -m pytest tests
   - coverage run -m unittest discover -v
20) Generate a file in the project directory named .coverage and we have to read it with the command:
   - coverage report
   - coverage report -m
21) implement the method done and undone to the Task object and the coverage will diminish (no need to relaunch the run)
22) Display the report in an html file:
   - coverage html