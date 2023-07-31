#program make a simple calculator
#this function adds two numbers
def add(x, y):
    return x+y
#this function subtracts two numbers
def sub(x, y):
    return x-y
#this function multiplies two numbers
def mul(x, y):
    return x*y
#this function divides two numbers
def div(x, y):
    return x/y

print("select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    #take input from the user
    choice = input("enter choice(1/2/3/4):")
    #choice if the choice is one of the four options
    if choice in('1','2','3','4'):
        num1 = float(input("enter first number:"))
        num2 = float(input("enter second number:"))
    if choice =='1':
        print(num1,"+", num2,"=",add(num1, num2))
    elif choice == '2':
        print(num1,"-", num2,"=",sub(num1, num2))
    elif choice == '3':
        print(num1,"*", num2,"=",mul(num1, num2))
    elif choice == '4':
        print(num1,"/", num2,"=",div(num1, num2))
        break
    else:
        print("invalid output")

