MAX_STUDENTS_NUM = 'Max number of students reached'


class MaxStudentsReachedError(Exception):
    def __init__(self, message="Max number of students reached"):
        self.message = message
        super().__init__(self.message)

