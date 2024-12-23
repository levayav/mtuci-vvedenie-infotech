class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    
    def set_password(self, new_password):
        self.__password = new_password
        print('Пароль изменен')
        
    def check_password(self, password):
        return self.__password == password
        
    
user = UserAccount('user123', 'user@ex.com', 'initialpass')
user.set_password('newpass')
print(user.check_password('newpass'))
print(user.check_password('wrongpass'))

    