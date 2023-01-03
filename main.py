class Employee:
    # class variables
    company_name = 'ECMA Company'

    # constructor to initialize the object
    def __init__(self, name, salary, code):
        # instance variables
        self.name = name
        self.salary = salary
        self.code = code

    # instance method
    def show(self):
        print('Employee:', self.name, self.salary, self.code, self.company_name)

# create first object
emp1 = Employee("Harry", 12000, "A2023")
emp1.show()

# create second object
emp2 = Employee("Emma1", 10000, "A2254")
emp2.show()
