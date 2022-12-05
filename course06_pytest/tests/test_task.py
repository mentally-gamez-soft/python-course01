import pytest
from core.task import Task

#def test_example():
#    assert 10 == 10


class TestTask():

    def setup_method(self):
        print("Method setup is executed before each test")
        self.task_id = 1
        self.description = "Learn pytest"
        self.status = True
        self.task1 = Task(task_id=self.task_id, 
                            description=self.description, 
                            status=self.status) 

    def teardown_method(self):
        print("Method teardown is executed after each test")
        del self.task1

    @classmethod
    def setup_class(cls):
        print("Method setup general is launched before all tests")
        # import csv
        # csv_filename = "./course06_pytest/list_of_tasks.csv"
        # cls.list_of_tasks = []
        
        # with open(csv_filename) as f:
        #     reader = csv.reader(f)
        #     for line in reader:
        #         line[0] = int(line[0])
        #         line[2] = bool(line[2])
        #         # Transform list to tuple
        #         cls.list_of_tasks.append(tuple(line))

    @classmethod
    def teardown_class(cls):
        print("Method teardown general is launched after all tests")


    def test_check_description_task(self):
         assert self.description == self.task1.description, "Sorry but the description for the task is different"

    #Implement markers
    @pytest.mark.tests_id_task
    def test_check_id_task_is_number(self):
        assert isinstance(self.task1.task_id, (int,float)) == True

    @pytest.mark.tests_id_task
    @pytest.mark.news
    def test_check_id_task_is_positive(self):
        assert self.task1.task_id > 0

    # Implement markers skip and skipif
    @pytest.mark.skip(reason="We dont need this test for the moment")
    def test_skip(self):
        assert 2 == 2

    @pytest.mark.skipif(Task.verification(), reason="We dont need this test for the moment")
    def test_skip_if(self):
        assert 4 == 4

    # Implement parameters in tests
    @pytest.mark.parametrize(
         "task_id, description, status",
          [
             (1, "Learn pytest", True),
             (2, "Learn unittest", False),
             (3, "le python c est la vie", False),
             (5, "tout va bien", True),
             (0, "on teste avec un id nul", True),
             (-1, "on teste avec un id negatif", True),
             (6, "0k", True),
             (7, "Booleen non indique ca donne quoi ?", None),
         ]
    )
    def test_check_data_task(self, task_id, description, status):
        self.task1 = Task(task_id=task_id, 
                          description=description, 
                          status=status)
        assert self.task1.task_id > 0 
        assert len(self.task1.description) > 3
        assert isinstance(self.task1.status, bool) == True

    # read from files the parameters
    import csv
    # csv_filename = "./course06_pytest/list_of_tasks.csv"
    csv_filename = "./list_of_tasks.csv"
    list_of_tasks = []
    
    with open(csv_filename) as f:
       reader = csv.reader(f)
       for line in reader:
           line[0] = int(line[0])
           line[2] = bool(line[2])
           # Transform list to tuple
           list_of_tasks.append(tuple(line))

    @pytest.mark.parametrize(
        "task_id, description, status",
       list_of_tasks
    )
    def test_check_data_task_from_properties_file(self, task_id, description, status):
        self.task1 = Task(task_id=task_id, 
                          description=description, 
                          status=status)
        assert self.task1.task_id > 0 
        assert len(self.task1.description) > 3
        assert isinstance(self.task1.status, bool) == True