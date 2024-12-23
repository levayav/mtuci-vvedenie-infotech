import math as m
import datetime as dt

def f_sqrt(n):
    return m.sqrt(n)

def dt_now():
    return dt.datetime.now()

n = int(input('Введите число: '))

print(f_sqrt(n))
print(dt_now())