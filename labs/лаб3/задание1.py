#Выбор типа чтения
def read_file(read_type):
    if read_type == 'all':
         with open("C://Users//levaa//OneDrive//Рабочий стол//ввикт//лаб3//example.txt", 'r', encoding = 'UTF-8') as file:
              content = file.read()
              print(content)
    
    elif read_type == 'lbl':
         with open("C://Users//levaa//OneDrive//Рабочий стол//ввикт//лаб3//example.txt", 'r', encoding = 'UTF-8') as file:
              for line in file:
                   print(line)


read_file('lbl')


