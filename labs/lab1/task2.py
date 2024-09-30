num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
if num1 > num2:
    print('Большее число:', num1)
elif num2 > num1:
    print('Большее число:', num2)
else:
    print('Они оба равны:', num1)

print('Большее число:', max(num1, num2))
