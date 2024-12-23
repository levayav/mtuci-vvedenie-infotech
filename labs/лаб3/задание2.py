text = input('Введите текст для записи в файл: ')

with open("C://Users//levaa//OneDrive//Рабочий стол//ввикт//лаб3//user_input.txt", 'a+', encoding = 'UTF-8') as file:
    file.write(text)
    content = file.read()

with open("C://Users//levaa//OneDrive//Рабочий стол//ввикт//лаб3//user_input.txt", 'r', encoding = 'UTF-8') as file:
    content = file.read()
    print(content)


