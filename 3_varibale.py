# # varibales: object containing specific values
# x=7
# print(x)
# y="i m talha akbar"
# print(y)
# #type of variables
# type(x)
# print(type(x))
# #Rule to assign a variable
# # 1- The varibale should contain letter, number or underscores.
# # 2- Do not start with number .
# # 3- Space are not allowed.
# # 4- Do not use keywords used in function (break , mean ,median,type etc). 
# # 5- Short and descriptive 
# # 6- Case senstivity (Lowercase, uppercase leater lower case letters should be used ).
# names = "talha akbar"
# print(names)

# # Ask the user for the radius of a circle and then print the area 
# radius = input("Enter your Radius")
# radius = float(radius)
# area = 3.14159 * radius**2
# print("Area of the circle is",area)

# # convert fahrenheit to celsius
# fahrenheit = float(input("Enter your temperature in Fahrenheit"))
# celsius = (fahrenheit - 32) * 5/9
# print(fahrenheit,"Fahrenheit in Celsius is ",celsius)

# # obtain the product of two integers
# num_1 = int(input("Enter your 1st number:"))
# num_2 = int(input("Enter your 2nd number:"))
# num =num_1 * num_2
# print("Product of your to number:",num)

# # Ali,Ahmad , Kamal and Hamid want to order pizza - they will each eat
# # 4 slices of pizza, The local pizza shop sells pizzas of only 6 slices 
# # What is the minimum number of pizzas needed - use floor division
t_s = 4 * 4 
number_of_pizzas =(t_s + 5)//6
s_left = number_of_pizzas*6 - t_s
print("The numbers of pizzas required :",number_of_pizzas,"The number of Slices left: ",s_left)
