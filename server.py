import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)
    
    def printReverse(self, s, current=None):
        print(s[::-1])
    
    def printUpper(self, s, current=None):
        print(s.upper())
    
    def getStringLength(self, s, current=None):
        return len(s)

class CalculatorI(Demo.Calculator):
    def add(self, a, b, current=None):
        return a + b
    
    def subtract(self, a, b, current=None):
        return a - b
    
    def multiply(self, a, b, current=None):
        return a * b
    
    def divide(self, a, b, current=None):
        if b == 0:
            return 0.0
        return float(a) / float(b)

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
printer_object = PrinterI()
calculator_object = CalculatorI()
adapter.add(printer_object, communicator.stringToIdentity("SimplePrinter"))
adapter.add(calculator_object, communicator.stringToIdentity("SimpleCalculator"))
adapter.activate()

communicator.waitForShutdown()