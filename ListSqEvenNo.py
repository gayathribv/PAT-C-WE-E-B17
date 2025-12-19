# Given a list of numbers, create a list comprehension and use lambda function create generate squares of even numbers

# allnumlst=[]
# for i in range(0,15):
#     allnumlst.append(i)
# print(allnumlst)
# evenNums=[x for x in allnumlst if x % 2 == 0]
# print(evenNums)

num_lst=[1,2,3,4,5,6,7,8,9,10]
num_even_lst=list(filter(lambda val:val%2 == 0, num_lst))
num_even_sqr_lst=[x**2 for x in num_lst if x % 2 == 0]
print(num_even_sqr_lst)