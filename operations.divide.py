class DivideOperation:
    def execute(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Division by zero is not allowed"
