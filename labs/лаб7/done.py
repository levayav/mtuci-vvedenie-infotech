class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def get_info(self):
        return f'Имя сотрудника: {self.name}, его идентификационный номер: {self.id}'
    

class Manager(Employee):
    def __init__(self, name, id, departament):
        Employee.__init__(self, name, id)
        self.departament = departament

    def manage_project(self, project_name):
        return f'Сотрудник {self.name} управляет проектом {project_name} в {self.departament} в отделе)'
    

class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self, equipment):
        return f'Сотрудник {self.name} со специализацией {self.specialization} выполняет техническое обслуживание {equipment}'
    
class TechManager(Manager, Technician):
    def __init__(self, name, id, departament, specialization):
        Manager.__init__(self, name, id, departament)
        Technician.__init__(self, name, id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        if not self.team:
            return f'У {self.name} еще нет подчиненных'
        team_info = [employee.get_info() for employee in self.team]
        return f'Команда {self.name}:\n' + '\n'.join(team_info)
    

if __name__ == '__main__':
    employee = Employee('Икром', 1)
    manager = Manager('Егор', 2, 'Акции')
    technician = Technician('Матвей', 3, 'Электрика')
    tech_manager = TechManager('Владос', 4, 'Продажи', 'Механик')
    
    print(employee.get_info())
    print(manager.get_info())
    print(technician.get_info())
    print(tech_manager.get_info())
    
    print(manager.manage_project('Увеличение продаж'))
    print(technician.perform_maintenance('Компьютера'))

    tech_manager.add_employee(employee)
    tech_manager.add_employee(manager)
    tech_manager.add_employee(technician)

    print(tech_manager.get_team_info())
    
        

        


