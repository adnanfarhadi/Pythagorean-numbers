

x = int(input("Please Enter a Number (x) = "))
y = int(input("Please Enter a Number (y) = "))
z = int(input("Please a number greater than x , y (z) = "))
power_x = x ** 2
power_y = y ** 2
power_z = z ** 2

print("power_x = ", power_x)
print("power_y = ", power_y)
print("power_z = ", power_z)


# if (power_x+power_y == power_z) or (power_x+power_z == power_y) or (power_y+power_z == power_x):
#     print("Yes")

if power_z == (power_x + power_y):
    print("Yes")
else:
    print("No")
