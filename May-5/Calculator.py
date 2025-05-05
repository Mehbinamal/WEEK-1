
def calculator(num_1,num_2,op):
    if op == '+':
        return num_1 + num_2
    elif op == '-':
        return num_1 - num_2
    elif op == '*':
        return num_1*num_2
    elif op == '/':
        return num_1/num_2


numbers = int(input("How many numbers need to be calculated : "))
num_1 = float(input("Enter Number 1 :"))
operator = input("Select Operator(+,-,*,/) :")
num_2 = float(input("Enter Number 2 :"))
result = calculator(num_1,num_2,operator)
for i in range(2,numbers):
    operator = input("Select Operator(+,-,*,/) :")
    num = float(input(f"Enter Number {i+1} :")) 
    result = calculator(result,num,operator)
print("result :",result)