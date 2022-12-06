# This is an example project for testing suits in python

## Installation of the packages for the project
1) Install pip-tools to the project: python -m pip install pip-tools
2) Generate requirements.txt via the command: pip-compile requirements.in
3) Install dependencies via: pip install requirements.txt

## Launch of test suits with coverage tool
- In case of tests suit with unittest:
  - coverage run -m unittest discover course*/tests/ -p 'test_*.py'
  - coverage run --source=./tests --cov=course05_unittest/ --cov=course04_unittest/ -m unittest discover 

- In case of tests suit with pytest
    - coverage run -m pytest arg1 arg2 arg3

coverage run  --rcfile=./.coveragerc -m unittest discover
coverage run -m unittest discover course05_unittest/tests/ -p 'test_*.py'