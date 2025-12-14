# accept input as a string
# take the first and the last characters
#convert to int, add, display

inp_Num=list(input("Enter the Number for which you need to find the sum of first and last number: "))
Inp_length=len(inp_Num)-1
while Inp_length != 0:
    sum_First_Last=int(inp_Num[0]) + int(inp_Num[Inp_length])
    print(f"Sum of first digit {inp_Num[0]} and last digit {inp_Num[Inp_length]} is {sum_First_Last}")
    inp_Num = list(input("Enter Another Number for which you need to find the sum of first and last number: "))
    Inp_length = len(inp_Num) - 1


