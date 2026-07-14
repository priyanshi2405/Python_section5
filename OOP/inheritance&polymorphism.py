class animal: #parent class
    location = "austrila" #parent class attribute

    def __init__(self,name):  #constructor in parent class
        self.name = name

    def speak(self): #this is the parent class method
        print("general animal sound")

class dog(animal):      #child class and passed with parent class(animal)
    def speak(slef):
        print("the dog says woof!!")

# d = dog("oreo")  #it is the object for child class 
# d.speak()
a = animal("oreo")
a.speak()
print(a.location)

