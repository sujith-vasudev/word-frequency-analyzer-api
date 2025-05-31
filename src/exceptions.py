class ValidationError(Exception):
    status_code = 400
    ERROR_CODE = 4200

    def __init__(self, message):
        self.message = message


class AccessExpired(Exception):
    status_code = 401
    ERROR_CODE = 4201

    def __init__(self, message):
        self.message = message
