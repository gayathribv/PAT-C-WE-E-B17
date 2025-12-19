# Generating fibonacci sequence for n numbers
n=int(input("Enter the number upto which you want to find the sum of fibonacci sequence: "))
f = lambda x: 1 if x in (1,2) else f(x-1) + f(x-2)
fibi=(f(n))
print(fibi)