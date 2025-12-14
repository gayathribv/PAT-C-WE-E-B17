# Happy numbers - sum of squares of digits progressively reaches 1

# Given the python list [10, 501, 22, 37, 100, 999, 87, 351] display happy numbers
# 10 1 + 0 = 1


def numSquareSum(n):
    squareSum = 0
    while (n != 0):
        squareSum += (n % 10) * (n % 10)
        n = n // 10
    return squareSum

# Function to return true if n is a Happy Number
def isHappyNumber(n):
    st = set()
    while (1):
        n = numSquareSum(n)
        if (n == 1):
            return True
        if n in st:
            return False
        st.add(n)

lst=[10,501,22,37,100,999,87,351]
for i in lst:
    if isHappyNumber(i):
        print(i, "is a Happy Number")
    else:
        print(i, "is not a Happy Number")