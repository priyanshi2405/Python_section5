class employee:
    company = "tesla" #this is the class attribute

    def __init__(self,company,name,salary):
        self.company = company #this is the instance attribute of an object
        self.name = name
        self.salary = salary

    def get_info(self):
        print(f"the {self.company} gives {self.name} {self.salary} per month.")

e = employee("reliance","raju",350000)
e.get_info()
print(e.company)
print(employee.company)#prints
