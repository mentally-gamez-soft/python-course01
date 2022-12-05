
from core.task import Task
import pytest

class TestTaskCategory():

    def test_check_category_is_none(self):
        self.t1 = Task(1,"aprender pytheon", False)
        assert self.t1.category == None