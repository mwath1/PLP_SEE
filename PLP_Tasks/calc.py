
x = int(input("enter your first number: "))
y = int(input("enter your second number: "))
# defining the arithmetic opperations
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print("select operation -\n" "1.Addition\n" "2.Subtraction\n" "3.Multiplication\n"  "4.Division\n")
while True: 
    select = int(input("select operation (1-4): "))

    if select == 1:
        print(add(x, y)) 
    elif select == 2:
        print(sub(x, y))
    elif select == 3:
        print(x, "*", y, "=", mul(x, y))
    elif select == 4:
        print(x, "/", y, "=", div(x, y))
        next_operation = input("More operation?")
    if next_operation == "stop":
            break
else:
        print("Invalid input")