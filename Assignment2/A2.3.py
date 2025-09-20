seconds = int(input("please enter seconds:"))

hour = 0
minute = 0
second = 0

while seconds >= 3600:
    hour += 1
    seconds -= 3600

while seconds >= 60:
    minute += 1
    seconds -= 60

second = seconds

print(f"{hour} hour, {minute} minute {second} second")