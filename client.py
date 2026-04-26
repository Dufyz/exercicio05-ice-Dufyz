import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base = communicator.stringToProxy("SimplePrinter:default -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy for Printer")

print("=== Testing Printer Functions ===")
printer.printString("Hello World!")

printer.printReverse("Hello World!")
printer.printUpper("Hello World!")
length = printer.getStringLength("Hello World!")
print(f"String length: {length}")

calc_base = communicator.stringToProxy("SimpleCalculator:default -p 11000")
calculator = Demo.CalculatorPrx.checkedCast(calc_base)
if not calculator:
    raise RuntimeError("Invalid proxy for Calculator")

print("\n=== Testing Calculator Functions ===")
result_add = calculator.add(10, 5)
print(f"10 + 5 = {result_add}")

result_subtract = calculator.subtract(10, 5)
print(f"10 - 5 = {result_subtract}")

result_multiply = calculator.multiply(10, 5)
print(f"10 * 5 = {result_multiply}")

result_divide = calculator.divide(10, 5)
print(f"10 / 5 = {result_divide}")

communicator.destroy()
