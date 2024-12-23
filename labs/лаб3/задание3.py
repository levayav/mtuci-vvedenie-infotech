#Выбор типа чтения
def read_file(file_path, read_type):
    try:
        if read_type == 'all':
            with open(file_path, 'r', encoding = 'UTF-8') as file:
                content = file.read()
                print(content)
        
        elif read_type == 'lbl':
            with open(file_path, 'r', encoding = 'UTF-8') as file:
                for line in file:
                    print(line)
    except FileNotFoundError:
        print(f'Файл с путем {file_path} не найден!')



read_file("C://Users//levaa//OneDrive//Рабочий стол//ввикт//лаб3//exampl.txt", 'all')



