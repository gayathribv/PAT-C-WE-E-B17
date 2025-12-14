# Given list [10, 501. 22, 37, 100, 999, 87, 351]
# create a list with only prime numbers
# A number is prime if it is not divisble by any other number
# than 1 and itself
# if its divisible by its squareroot + 1 then n is non prime
# if divisible, then not a prime. discard
Full_List=[10, 501, 22, 37, 100, 999, 87, 351]
Prime_List=[]
List_length=len(Full_List)
for i in range(0,List_length):
    sqrt=int(Full_List[i]**0.5) + 1
    if (Full_List[i] % 2 == 0):
        continue
    elif (Full_List[i] % sqrt == 0):
        continue
    else:
        list.append(Prime_List, Full_List[i])
print(f"Full list is {Full_List}")
print(f"Prime Number list is {Prime_List}")