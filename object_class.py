class Computer:
  
  def config(self):
    print("i5, 16gb ,1TB")
    
com1 = Computer()
com2 = Computer()

com1.config()
com2.config()

class Me:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Me("Pranay", 20)
p1.myfunc()
