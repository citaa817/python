vazn=float(input())
ghad=float(input())

BMI=vazn/(ghad*ghad)
print(BMI)
 
if BMI ==22:
    print("normal")
elif BMI <22:
    print("kambod vazn")
elif BMI >25:
    print("ezafeh vazn")
