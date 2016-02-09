class ApiHelperException(Exception):
    details = None
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class ValidationErrorsException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
