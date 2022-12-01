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