n = int (input("تعداد دنباله  فیبوناچی رو وارد کن"))
a=1
b=1

print (a, end=",")

for i in range(1, n):
    print(b, end=",")
    a, b = b, a + b