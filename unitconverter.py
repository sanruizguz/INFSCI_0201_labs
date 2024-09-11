# PROBLEM 3
import math
value=input("Enter distance or weight value")
unit=input("Enter distance or weight unit") # in, cm, yd, m, oz, g, kg, lb.
metric=(str(value)+" "+str(unit))
print("The value to convert is",metric)

if unit == "in":
    print(metric," = ",float(value)*2.54,'cm')
elif unit == "cm":
    print(metric," = ",float(value)/2.54,'in')
elif unit == "y":
    print(metric," = ",float(value)*0.9144,'m')
elif unit == "m":
    print(metric," = ",float(value)/0.9144,'y')  
elif unit == "oz":
    print(metric," = ",float(value)*28.349523125,'gr')
elif unit == "gr":
    print(metric," = ",float(value)/28.349523125,'oz')
elif unit == "lb":
    print(metric," = ",float(value)*0.45359237,'kg')
elif unit == "kg":
    print(metric," = ",float(value)/0.45359237,'lb')
else:
    print("The unit is not included")
