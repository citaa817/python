import math

print("welcome to my calculator")
print("please enter your choice:")
op=input()

if op =="+" or op =="-" or op=="*" or op=="/":
    a= float(input("enter first number"))
    b= float(input("enter second number"))
else: 
    a= float(input("enter first number"))

if op== "+":
    result = a+ b

elif op =="-":
    result = a - b

elif op =="*":
    result = a * b

elif op =="/":
    result = a / b
    
elif op =="sin":
    result= math.sin(a)

elif op =="cos":
    result = math.cos(a)

elif op =="tan":
    result = math.tan(a)

elif op =="cot":
    result = math.cot(a)

elif op =="sqrt":
    result = math.sqrt(a)

elif op =="factorial":
    result = math.factorial(a)

    print(result)


