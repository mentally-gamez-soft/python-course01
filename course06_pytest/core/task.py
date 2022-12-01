class Task():

    def __init__(self, task_id:int, description:str, status:bool=False):
        self.task_id = task_id
        self.description = description
        if status is None:
            status = False
        self.status = status

    @classmethod
    def verification(cls):
        return True