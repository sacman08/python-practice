import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
passlen = int(input("Please enter the minimum required password length[e.g. 8]:"))
p = "".join(random.sample(s, passlen))
print(p)
