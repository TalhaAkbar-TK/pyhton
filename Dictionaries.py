'''
Practice challenge # 1
Can you remember how to check if a key exists in a dictionary?
using the capitals dictionary below write some code to ask the user to input 
a country, then check to see if that country is in the dictionary and if it is
print the capital .If not tell the user it's not there.
'''
# capitals={'Pakistan':'Islamabad','India':'New Delhi','Spain':'Madrid',
# 'United Kingdom':'London','United States':'Washington DC',
# 'Italy':'Rome','Denmark':'Copenhagen','Germany':'Berlin',
# 'Greece':'Athens','Ireland':'Dublin'
# }
# U_input = input("Which country would you like to check?:>")

# U_input = U_input.lower()

# while('united kindom'not in U_input and not U_input.isalpha()):
#     if U_input == "united states":
#         break
#     print("you must input a string")
#     U_input = input("which country would you like to check?:>")
# U_input = U_input.title()
# if U_input in capitals:
#     print(f'The capital of {U_input} is {capitals[U_input]}')
# else:
#     print("No data available")

'''
Practice challenge # 2
write code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e{1:0,2:1,3:1,4:2,5:3 etc}
'''
# n =12 
# a = 0
# b = 1
# fib_num ={}
# for i in range (1,n+1):
#     fib_num[i]=a
#     a,b=b,a+b
# print(fib_num)

'''
Practice challenge # 3
Create a dictionary to represent the open , high, low ,close share price data
for 4 imaginary companies. 'Python DS','PythonSoft','Pythazon' and 'Pybook'
the 4 sets of data are [12.87,13.23,11.42,13.10],[23.54,25.76,21.87,22.33]
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24] 
'''
# companies = ['Python DS','PythonSoft','Pythazon' , 'Pybook']
# key_names = ['Open' , 'High', 'Low' ,'Close']
# price = [[12.87,13.23,11.42,13.10],[23.54,25.76,21.87,22.33],
# [98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24] ]
# d_1 = {}
# for i in range(len(key_names)):
#     d_1[companies[i]] = dict(zip(key_names,price[i]))
# print(d_1)

'''
Practice challenge # 4
Go to the python module web page and find a module that you like.Play with it,
read the documentation and try to implement it.
'''

import datetime
today = datetime.date.today()
print(f"Today's date is{today}")
holiday = datetime.date(2022,12,25)
delta = holiday - today
print(f'just {delta.days} days until the holiday!')
