
class Error(Exception):
    pass


class RateLimitHere(Error):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.code = 503
        self.message = message

    def __str__(self):
        return repr(self.message)
