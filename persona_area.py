#Imported math for pi(π)
import math
#Taking float as input so we can use decimal values also
r=float(input("Enter the radius of the circle:"))
#Defining a function so that it can be use multiple times
def area_circle():
    area=math.pi*r**2
    return(print("Area of the circle is:",area))
#Calling the defined function
area_circle()