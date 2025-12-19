# Given a list of numbers, use the reduce function and a lambda expression to calculate
# product of all the numbers in a list

from functools import reduce
num_lst=[1, 2, 3, 4, 5, 6, 7, 8,9,10]
num_prod=reduce(lambda x,y: x * y, num_lst)
print(f"The product of {num_lst} is {num_prod}")