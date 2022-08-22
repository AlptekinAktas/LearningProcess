class Point:
    def move (self):
        print ("move")

    def draw (self):
        print ("draw")
    
    


print("I created a ", type(Point()))


# I assigned the class to a variable.
#this is the way to create a new object
#most languages need to mention the type of the object you are creating but python can understand basics like int, str or float.
# the assignment we are doing here is the same: we are telling the system that accept the object called point1 as a Point type

point1 = Point()


# I assigned some attributes to the object I created    

point1.x = 10
point1.y = 20

print (point1.x)



#this is a method I created for the class named Point and I am using it in the object called point1

point1.draw()

# I assigned another object as a Point class

point2 = Point()
point2.x = 15

print("Point2.x = ", point2.x)
print("Point1.x = ", point1.x)