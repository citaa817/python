import random
computer_number= random.randint(10 , 100)

while True:
    user_number = int(input())
    if computer_number == user_number:
        print("barikala")
        break
    elif computer_number>user_number:
        print("boro bala")
        
    elif computer_number < user_number:
        print("bia peen")