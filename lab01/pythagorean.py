# PROBLEM 1
import math

side_one=input("Enter side one")
side_one=str(side_one)
side_two=input("Enter side two")
side_two=str(side_two)
side_one=int(side_one)
side_two=int(side_two)

hypo=math.sqrt((side_one**2)+(side_two**2))
hypo = round(hypo, 2)
print('The hypotenuse of the triangle is',hypo)