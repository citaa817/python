seconds = int(input("ثانیه را وارد "))
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")