class animal: #parent class
    location = "austrila" #parent class attribute

    def __init__(self,name):  #constructor in parent class
        self.name = name

    def speak(self): #this is the parent class method
        print("general animal sound")

class dog(animal):      #child class and passed with parent class(animal)
    def speaks(self):    #this is called method over riding (making a new verson of the same method in child class)
        super().speak()  #to call the instance or parent class's methods
        print("the dog says woof!!")

# d = dog("oreo")  #it is the object for child class 
# d.speak()
a = dog("oreo")
a.speaks()
# print(a.location)

