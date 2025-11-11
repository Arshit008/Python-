def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        print("Cannot divide by zero")
    else:
        return x/y
print("Selected operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.history")
print("6.Exit")
history=[]
while True:
    choice=input("Enter choice(1/2/3/4/5/6):")

    if choice=="1":
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        print(f"{num1}+{num2}={add(num1,num2)}")
        history.append(f"{num1}+{num2}={add(num1,num2)}")
    elif choice=='2':
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        print(f"{num1}-{num2}={sub(num1,num2)}")
        history.append(f"{num1}-{num2}={sub(num1,num2)}")
    elif choice=='3':
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        print(f"{num1}*{num2}={mul(num1,num2)}")
        history.append(f"{num1}*{num2}={mul(num1,num2)}")
    elif choice=='4':
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        print(f"{num1}/{num2}={div(num1,num2)}")
    elif choice=='5':
        print(f"History of calculations:{history}")
    elif choice=='6':
        print("Exiting the calculator....")
        break
    elif choice not in ['1','2','3','4','5','6']:
        print("Invalid input type again")



