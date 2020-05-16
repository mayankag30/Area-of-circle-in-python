from math import pi 
r = float(input("Input the radius of the circle : "))
area = pi*r*r
print("The area of the circle with radius ",r," is: ",area)

extent = input("Input the filename: ")
res = extent.split(".")
print ("The extension of the file is : " + repr(res[-1]))