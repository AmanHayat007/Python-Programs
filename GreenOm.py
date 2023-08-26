# diameter=float(8.0)
# for i in range(2):
#  Volume=float(input("Please enter the volume of the fuel required in meter cube : "))
#  Height=round(float(Volume/((3.14)*((diameter/2)**2))),3)
# print("The required height of the external tank is",Height,"to accomodate",Volume,"meter cube of fuel.")

    

# diameter = float(8.0)

# for i in range(2):
#     Volume = float(input("Please enter the volume of the fuel required in meter cube: "))
#     normal_Height = round(float(Volume / (3.14 * ((diameter / 2) ** 2))), 3)
#     updated_Height = normal_Height* Volume # Initialize updated height with normal height
    
#     print("Normal height to accommodate", Volume, "meter cube of fuel:", normal_Height)
    
   
    
#     print("Updated height to accommodate", Volume, "meter cube of fuel:", updated_Height)
     
diameter = float(8.0)

for i in range(2):
    Volume = float(input("Please enter the volume of the fuel required in meter cube: "))
    Height = round(float(Volume / (3.14 * ((diameter / 2) ** 2))), 3)
    
    if i == 0:
        print("Normal height to accommodate", Volume, "meter cube of fuel:", Height)
        normal_Height = Height  
    else:
        updated_Height = Height  
        print("Updated height to accommodate", Volume, "meter cube of fuel:", Height)

print("The required height of the external tank is", updated_Height, "to accommodate", Volume, "meter cube of fuel.")
