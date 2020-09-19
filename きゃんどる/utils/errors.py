class InvalidKyandle(BaseException):

    def __init__(self):
        super().__init__("Kyandle is invalid")