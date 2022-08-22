class Person:
    
#initialize is for default settings
        def __init__ (self, name):
        self.name = name
        
    def talk (self):
        print (f"Hi! I am {self.name}")


 # quotes will tell this is the variable called name                
john = Person("John Smith")
john.talk()

# defining different objects 
bob = Person("Bob Smith")
bob.talk()
