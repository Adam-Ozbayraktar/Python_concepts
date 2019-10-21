my_list = [1,9,8,3,4,5,2,4,5,7,4,2]

# sorted = returns new list (works on anything)
# sort = modifies original list (only works on list)(my_list.sort)
# decending order : sorted(my_list, reverse=True)

# Dictionary
di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os':'Mac'}
# by default sorts only keys
s_di = sorted(di)
print('Dict\t', s_di)

# Sort by absolute value
li = [-6,-5,-4,1,2,4]
s_li = sorted(li, key=abs)
print(s_li)

class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    # to String
    def __repr__(self):
        return f"{self.name}, {self.age}, ${self.salary}"

from operator import attrgetter

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]

def e_sort(emp):
    return emp.age

# s_employees = sorted(employees, key=e_sort, reverse=True)
# s_employees = sorted(employees, key=lambda e: e.name)
s_employees = sorted(employees, key=attrgetter('age'))
print(s_employees)
