def greet(name):
    print('Привет,', name + '!')


name = input('Введите Ваше имя: ')
greet(name)


def square(number):
    return number**2


number = int(input('Введите число: '))
print(square(number))


def max_of_two(x, y):
    if x > y:
        return 'Большее число равно: ' + str(x) 
    elif y > x:
        return 'Большее число равно: ' + str(y)
    else:
        return 'Числа равны: ' + str(x)


x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
print(max_of_two(x, y))
