class Details:
    def __init__(self):
        self.__name = None

    def setDetails(self, name):
        self.__name = name

    def showDetails(self):
        return self.__name


class Employee(Details):
    def __init__(self):
        super().__init__()
        self.__company_name = None

    def setEmployee(self, company_name):
        self.__company_name = company_name

    def showEmployee(self):
        return self.__company_name


print(Employee().showEmployee())
emp1 = Employee()
emp1.setDetails("John")
emp1.setEmployee("ABC Crop.")
print(emp1.showDetails())
print(emp1.showEmployee())
