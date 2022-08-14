# # Logical operator are either "true or false "
# # equal to                ==
# # not equal to            !=
# # less then               <
# # greater then            >
# # greater then and equal to >=
# # less then and equal to  <=

# # print(2==2)
# # print (3!=3)6
# # print(4<5)
# # print(4>5)
# # print(5<=3)
# # print(5>=4)
# age_at_school = 6
# your_age=int(input("how old are you?"))
# print(age_at_school==your_age)


# # Practice challenge
# # Write code that the user to input a number between 1 and 5 inclusive.
# # The code will take the integer value and print out string value. 
# # so far example if the user inputs 2 the code will print two. 
# # Reject any input that is not a number in the range.
 
# num = int(input("Enter your number between 1 and 5 "))
# if(num==1):
#     print("One")
# elif(num==2):
#     print("Two")
# elif(num==3):
#     print("Three")
# elif(num==4):
#     print("Four")
# elif(num==5):
#     print("Five")
# else:
#     print("You enter  number out of range ")


# Practice challenge #2
# Repeat the previous task but this time the user will input a string and the code will output the integer value.
# Convert the string to lowercase first. 
# st = input("Enter your number between one and five: ")
# st = st.lower()

# if(st=="one"):
#     print("One")
# elif(st=="two"):
#     print("Two")
# elif(st=="three"):
#     print("Three")
# elif(st=="four"):
#     print("Four")
# elif(st=="five"):
#     print("Five")
# else:
#     print("You enter  String out of range ")


# Practice challenge #3
# Create a variable containing an integer between 1 and 10 inclusive.
# Ask the user to guess the number. 
# If they guess too high or too low, tell them they have not won.
# Tell them they win if they guess the correct number.
# s_num = 6
# user_input = int(input("Enter your guess number between 1 and 10: "))
# if user_input == s_num:
#     print("you win")
# elif user_input > s_num:
#     print("you enter a higher number")
# else:
#     print("you enter lower number")


# Practice challenge # 4
# Ask the user to input their name. check the length of the name .
# if it is greater than 5 characters long, wirte a message telling them how many character
# otherwise write a message saying the length of their name is a secret.
# user_name = input("enter your name : ")
# L_name = len(user_name)
# if  L_name > 5 :
#     print("your name contains ",L_name,"character")
# else:
#     print("I/'m not telling youthe length of your name")

# Practice challenge # 5
# Ask the user for two integers between 1 and 20 . If they are both greater than
# 15 return their product. If only one is greater than 15 return their sum, if 
# neither are greater than 15 return zero.
# int_1 = int(input("Enter your 1st number between 1 and 20: "))
# int_2 = int(input("Enter your 2nd number between 1 and 20: "))
# if int_1 > 15 and int_2 > 15:
#     print("Product of two Number: ",int_1 * int_2)
# elif int_1 > 15 or int_2 > 15:
#     print("Sum of two Number: ",int_1 + int_2)
# else:
#     print(0)

# Practice challenge # 6
# Ask the user for two integers, then swap the contents of the variable.
# so if var_1 =1 and var_2 =2 initially, once the code has run var_1 should equal 2
# and var_2 should equal 1.
var_1 =int(input("Enter your 1st number:  "))
var_2 =int(input("Enter your 2nd number: "))
print("before swapping int_1=",var_1,"and int_2",var_2)
var_1,var_2 = var_2,var_1
print("After swapping int_1=",var_1,"and int_2",var_2)

