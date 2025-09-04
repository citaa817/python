time = input("(ساعت را وارد کن)")
h, m, s = time.split(":")
h = int(h)
m = int(m)
s = int(s)
total_seconds = h * 3600 + m * 60 + s
print("تعداد ثانیه", total_seconds)