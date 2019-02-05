import datetime


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

    @classmethod
    def set_raise_method(the_class, amount):
        the_class.raise_amount = amount

# Additional constructors
    @classmethod
    def from_string(the_class, emp_str):
        first, last, pay = emp_str.split("-")
        return the_class(first, last, pay)

# Static methods
    @staticmethod
    def isWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee("Tejas", "Shastha", 50000)
emp2 = Employee("Ram", "Lakhan", 2500000)

print(Employee.raise_amount)
print(emp1.raise_amount)

Employee.set_raise_method(1.05)
# This not usually done since makes no logical sense
emp1.set_raise_method(1.06)

print(Employee.raise_amount)
print(emp1.raise_amount)

emp_str1 = "First1-last1-123"
emp_str2 = "First2-last2-456"
emp_str3 = "First3-last4-789"

first, last, pay = emp_str1.split("-")
new_emp1 = Employee(first, last, pay)
print(new_emp1.email)

new_emp2 = Employee.from_string(emp_str2)
print(new_emp2.email)


my_date = datetime.date(2016, 7, 10)
print(Employee.isWorkDay(my_date))
