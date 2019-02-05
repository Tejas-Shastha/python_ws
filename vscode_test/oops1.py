class Employee:

    # accessible as the same variable to all instances. Similar to a static attribute
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@gmail.com"

        Employee.num_of_emps += 1

    def dispFullName(self):
        print(self.first+" "+self.last)

    def fullname(self):
        return self.first + " " + self.last

    def apply_raise(self, ):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)

emp1 = Employee("Tejas", "Shastha", 50000)
emp2 = Employee("Ram", "Lakhan", 2500000)


# print(Employee.raise_amount)
# emp1.apply_raise()
# print(emp1.pay)

# print(emp1.__dict__)
# Employee.raise_amount = 1.05
# emp1.raise_amount = 1.06
# print(emp1.__dict__)
# print(Employee.__dict__)


print(Employee.num_of_emps)
