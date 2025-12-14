# Create a list with [10, 501, 22, 37, 100, 999, 87, 351]
# add even no.s to a list and odd no.s to another list
Full_List=[10, 501, 22, 37, 100, 999, 87, 351]
Even_List= list(filter(lambda x: x% 2 == 0, Full_List))
Odd_List=list(filter(lambda x: x% 2 == 1, Full_List))

print(f"The Original set of Numbers, {Full_List}")
print(f"Even Numbers from the Original List are {Even_List}")
print(f"Odd Numbers from the Original List are {Odd_List}")