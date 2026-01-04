print("=========================== Calculator ===========================")

a= float(input("Enter first number : "))
sign = input("Enter sign/(+,-,*,/,) : ")
b = float(input("Enter second number : "))

if b==0:
    print("Please keep b non-zero")

else:
    
    def add(a,b):
        print("Addition of two numbers is",end = " ")
        return a+b

    def sub(a,b):
        print("Subtraction of two numbers is",end = " ")
        return a-b

    def mult(a,b):
        print("Multiplication of two numbers is",end = " ")
        return a*b
    def div(a,b):
        print("Division of two number is ",end = " ")
        return a/b

    dict = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
    }

    print(dict[sign](a,b))
    
