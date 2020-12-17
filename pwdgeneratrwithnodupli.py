import random

x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^&*()_+-=[]{}\|<>/"

pwd_len = random.randint(6, 20)
a = random.sample(x, pwd_len)
pwd = ''.join(a)

print(pwd)
