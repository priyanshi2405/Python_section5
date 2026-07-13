class employee:
    company = "HP"

    def get_salary(self):  #self is imp and compulsary 1st parameter as it is a refference to the object that is being created
        return 340000

e1 = employee() # an object of class is being created
print(e1.get_salary()) # employee e1's salary method is called 
e2 = employee()
print(e2.get_salary())
print(employee())
print(e2.company)