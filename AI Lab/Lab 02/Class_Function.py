class University:
    def __init__(self, _name, _reputation):
        self.name = _name
        self.reputation = _reputation
        
    def details(self):
        print(self.name, self.reputation)

# double under-score mean private... (__variable)
# single under-score mean protected... (_variable)

class Employee:
    def __init__(self, name, designation):
        self._name = name # single under-score mean protected...
        self.designation = designation

    def show_details(self):
        print("--Info--")
        print(self._name)
        print(self.designation)

class Admin(Employee): # inheritance
    def __init__(self, name, designation):
        super().__init__(name, designation)

class Faculty(Employee): # inheritance
    def __init__(self, name, designation, dept):
        super().__init__(name, designation)
        self.__dept = dept
    
    def show_details(self):
        # return super().show_details()
        print("Faculty Info")
        print(self._name)
        print(self.designation)
        print(self.__dept)


def main():
    obj = Employee("Din", "Student")
    obj.show_details()
    print(obj.designation)

    # will give error, can't access private variable directly...
    # print(obj._name)

    admin = Admin("Tarek", "CEO")
    admin.show_details()

    faculty = Faculty("Rahim", "Lecturer", "CSE")
    faculty.show_details()

if __name__ == "__main__":
    main()