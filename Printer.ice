module Demo
{
    interface Printer
    {
        void printString(string s);
        void printReverse(string s);
        void printUpper(string s);
        int getStringLength(string s);
    }
    
    interface Calculator
    {
        int add(int a, int b);
        int subtract(int a, int b);
        int multiply(int a, int b);
        double divide(int a, int b);
    }
}
