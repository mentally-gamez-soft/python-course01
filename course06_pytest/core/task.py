class Task():

    def __init__(self, task_id:int, description:str, status:bool=False, category=None):
        self.task_id = task_id
        self.description = description
        if status is None:
            status = False
        self.status = status

    @classmethod
    def verification(cls):
        return True

    def done(self):
        self.status = True

    def undone(self):
        self.status = False