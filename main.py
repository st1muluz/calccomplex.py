from calculator import ComplexCalculator
from operations.add import AddOperation
from operations.multiply import MultiplyOperation
from operations.divide import DivideOperation
import logger

def main():
    log = logger.setup_logger()

    a = 2 + 3j
    b = 1 + 4j

    calc = ComplexCalculator(AddOperation())
    result = calc.execute(a, b)
    log.info(f"Adding {a} and {b}: {result}")

    calc.set_strategy(MultiplyOperation())
    result = calc.execute(a, b)
    log.info(f"Multiplying {a} and {b}: {result}")

    calc.set_strategy(DivideOperation())
    result = calc.execute(a, b)
    log.info(f"Dividing {a} by {b}: {result}")

if __name__ == "__main__":
    main()
