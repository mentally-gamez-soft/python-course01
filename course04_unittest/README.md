Example of (Test Driven Development) with a concrete example of a bank account management:

Requisites for a bank account
- When a new bank account is created, its balance is 0
- When a deposit is achieved, the new balance value becomes the current balance plus the added amount
- When a withdraw is achieved, the new balance is the current balance minus the withdrawn amount
- If the user tries to withdraw more than the value of the balance an exception will be raised.

Ateps:
1) Creation of Python packages (no carpetas, ya que unittest necesita los paquetes y los init.py)
2) Creation of the tests directory and the file test_new_account.py and implement our test
3) Creation of the core directory and the account.py file and implementation of the Account class (with a balance=0)
4) Executing the test with one of the following command line:
    - python -m unittest tests/test_new_account.py
    - python -m unittest tests/test_new_account.py -v
    - python -m unittest discover tests
    - python -m unittest discover tests -v
5) Creation in the directory tests of the file test_deposit_into_account.py and implement the corresponding test
6) Modification of the class Account to add the functionality defined in the test
7) Executing the test with one of the following command line:
    - python -m unittest tests/test_deposit_into_account.py
    - python -m unittest tests/test_deposit_into_account.py -v
    - python -m unittest discover tests 
    - python -m unittest discover tests -v
8) Do the same for the 3rd requisite (withdraw)
9) Modify the class to raise an exception when the user is trying to withdraw more than it's possible
10) Executing the test with one of the following command line:
    - python -m unittest tests/test_withdraw_from_account.py
    - python -m unittest tests/test_withdraw_from_account.py -v
    - python -m unittest discover tests 
    - python -m unittest discover tests -v