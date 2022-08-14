# while loop
# x=0
# while (x<5):
#     print(x)
#     x=x+1
# for loop
# for x in range(2,13):
#     print(x)

# array
# days=["mon","tue","wed","thu","fri","sat","sun"]

# for d in days:
#     if (d=="wed"): continue
#     if (d=="sat"): break
#     print(d)

# Practice challenge # 1

# Ask the user for two numbers between 1 and 100. Then count from the 
# lower number to the higher number. print the results to the screen.
# user_input_1 =int(input("Enter a number between 1-100: "))
# user_input_2 = int(input("Enter a number between 1-100: "))
# while user_input_1 < 0 or user_input_2 < 0 or user_input_1 > 100 or user_input_2 > 100 or user_input_1 == user_input_2:
#     print("Number must be in range of 1 to 100 try again: ")
#     user_input_1 =int(input("Enter a number between 1-100: "))
#     user_input_2 = int(input("Enter a number between 1-100: "))
# if user_input_1 < user_input_2:
#     for i in range(user_input_1,user_input_2+1):
#         print(i,end=" ")
# else:
#     for i in range(user_input_2 ,user_input_1+1):
#         print(i,end=" ")

# Practice challenge # 2
# Ask the user to input a string and then print it out to the screen in reverse order(use a for loop)
# u_input = input("Enter your string : ")
# r_stirng = ""
# for char in u_input:
#     r_stirng = char + r_stirng

# print(r_stirng)

# Practice challenge # 3
# Ask the user for a number between 1 and 12 and the display a times table for that number.

# u_input =input("Enter your value between 1 to 12: ")
 
# while(not u_input.isdigit()) or (int(u_input) < 1 or int(u_input) > 12 ):
#     print("your value must be in between 1 and 12:")
#     u_input = input("Enter your value again : ")
# u_input=int(u_input)
# print("---------------------------------")
# print()
# print(f"This is {u_input} times table")
# for i in range (1,13):
#     print(f"{i} x {u_input} = {i*u_input}")


# Practice challenge # 4
# can you amend the solution to question 3 so that it just prints out a time table between 1 and 12 (no need to ask user for input)
# for i in range (1,13):
#     print("---------------------------------")
#     print()
#     print(f"This is {i} times table")
#     for j in range (1,13):
#         print(f"{j} x {i} = {i*j}")

# Practice challenge # 5
# Ask the user to input a sequence of numbers. Then calculate the mean and print the result.
# u_input = input("Enter a number type exit to stop:> ")
# numbers= []
# while(u_input.lower() != 'exit'):
#     while not u_input.isdigit():
#         print('That is not a number! Number only please:>')
#         u_input = input("try again:> ")
#     numbers.append(int(u_input))
#     u_input =input('Please enter next number or type exit to stop :>')
# total = 0
# for number in numbers:  
#     total = total + number
# print(f"Mean is {total/len(numbers)}")

# Practice challenge # 6 
# Write code that will calculate 15 factorial.(factorial is product of positive ints up to a given number.)
# n =int(input("Enter your number for factorial: "))
# num = 1
# for i in range(1,n+1):
#     num = i*num
# print(num)

# Practice challenge # 7
#write code to calculate fabonacci number.Create list containing 
# frist 20 fibonacci number, (fib numbers made sum of preceeding two. series starts 0 1 1 2 3 5 8 13 ....)
# n =20
# a = 0
# b = 1
# fib_num =[]
# for i in range (n):
#     fib_num.append(a)
#     a,b = b,a+b
# print(fib_num)

# # Practice challenge # 8
# *****
# *
# ****
# *
# *
# *
# can you draw this using python?

# star ="*"
# for i in range(1,7):
#     for j in range(1,6):
#         if i==1 and j<6:
#             print(star,end='')
#         elif i == 2 and j == 1:
#             print()
#             print(star)
#         elif i == 3 and j<5:
#             print(star,end='')
#         elif i==4 and j == 1:
#             print()
#             print(star)
#         elif i==5 and j == 1:
#             print(star)
#         elif i == 6 and j == 1:
#             print(star)

# Practice challenge # 9
# write some code that will determine all odd and even numbers between 1 and 100.put the odds 
# in a list named odd and the evens in a list name even.

odd=[]
even=[]
for i in range(1,101):
    if (i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("odd number list",odd)
print("even number list",even)