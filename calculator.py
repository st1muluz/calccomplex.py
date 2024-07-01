from operations.add import AddOperation
from operations.multiply import MultiplyOperation
from operations.divide import DivideOperation

class ComplexCalculator:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute(self, a, b):
        return self._strategy.execute(a, b)
