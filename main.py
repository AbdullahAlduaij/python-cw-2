
my_name = input("enter your name:")
my_age = input("enter your age:")
print(f"my name is {my_name} and I am {my_age} years old ")

f_num = complex(float(int(input("enter a number:"))))
s_num = complex(float(int(input("enter another number:"))))
opp = input("enter your operation:")
if opp == "+":
     print(f_num + s_num)
elif opp == "-":
     print(f_num - s_num)
elif opp == "*":
     print(f_num * s_num)
else: 
     print(f_num / s_num)

if opp != "+" or "-" or "*" or "/":
    print("This operation is not valid")


bus_capacity = 30 
bus_capacity = int(input("people in the bus:"))
people_inbus = int(input("how many people in the bus:"))

empty_seats = bus_capacity - people_inbus
if bus_capacity > people_inbus:
     print(f"There is {empty_seats} available")
else:
     print("The bus is full")

