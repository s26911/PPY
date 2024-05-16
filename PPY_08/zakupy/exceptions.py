class BelowZero(Exception):
    def __init__(self, value):
        self.message = f"Wartość {value} powinna być większa niż zero!"
        super().__init__(self.message)