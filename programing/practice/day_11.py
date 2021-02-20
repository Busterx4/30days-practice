# # # # def add_two_numbers():
# # # #     num_one=2
# # # #     num_two=3
# # # #     total= num_one+num_two
# # # #     return total
# # # # print(add_two_numbers())

# # # # def area_of_square(length):
# # # #     breath=5
# # # #     area= breath*length
# # # #     return area
# # # # print(area_of_square(10))

# # # def calculate_age(birthdate, current_year):
# # #     current_age= current_year-birthdate
# # #     return current_age
# # # print('Your current age is',calculate_age(2004, 2021) )

# # def find_number_divisible_by_three(x):
# #     if x/3:
# #      print('x is divisible by three')
# #      return True
# #     return False
# # print(find_number_divisible_by_three(105))
# def find_a_number_divisible_by_four(n):
#     divisble_by_four=[]
#     for i in range(n+3):
#         if n/4:
#             divisble_by_four.append(i)
#     return divisble_by_four
# print(find_a_number_divisible_by_four(9))

# def sum_of_numbers(z):
#     total=0
#     for i in range(z+1):
#         total=total+i
#     print(total)

#1 
# def sum_of_two_numbers(number_one, number_two):
#     sum_of_both_numbers= number_one+number_two
#     return sum_of_both_numbers
# print(sum_of_two_numbers(5,10))

#2 
# def calculate_area_of_circle(r):
#     Area_of_circle= 3.14*r*r
#     return Area_of_circle
# print(calculate_area_of_circle(5))
#4
# def convert_celcius_to_fahrenheit(cel):
#     fahrenheit=(cel*9/5)+32
#     return fahrenheit
# print(convert_celcius_to_fahrenheit(38))

#5
# def check_season(month):
#     if month in ['June', 'July', 'August']:
#         print('summer')
#     elif month in ['Januray', 'Febuary', 'March' 'April', 'May']:
#         print('spring')
#     elif month in ['September', 'October']:
#         print('authumn')
#     else:
#          print('winter')
#          return month
# (check_season('June'))
 #7
# def solve_quadratic_equation(a,b,c):
#     x=5
#     quadratic_equation=a*x**+b*x+c
#     return quadratic_equation
# print(solve_quadratic_equation(2,3,4))
# 8
# def print_list():
#     list=[]
#     for i  in range(0,11):
#         list.append(i)
#     return list
# a=print_list()
# print(a)
#9 
# def reverse_list(nums):
#     for i in range(len(nums)-1,-1,-1):
#         yield nums[i]
# print(reverse_list([1,2,3,4,5]))


# import mymodule
# print(mymodule.area_of_square(le=3, bre=10))

# from mymodule import area_of_square, calculate_age, sum_of_three_numbers
# print(area_of_square(5,2))
# print(sum_of_three_numbers(1,2,3))
# birth_year=2004
# print(calculate_age(2021))


