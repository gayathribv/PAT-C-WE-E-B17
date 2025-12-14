# Find the number of ways in which Rs 1, rs 2 Rs 5 Rs 10 can add upto 10 rs
# 1 10rs
# 2 5 Rs
# 5 2 Rs
# 10 1 Rs

# Fix 1 5 and iterate through 1rs and 2rs to see how many are needed to make rs 10
# 5 2 2 1
# 5 2 1 1 1

rs5 = 5
rs2= 2
rs1 = 1
sum = 0
hitlst=[]
while sum < 11:
    sum = 0
    sum += 5
    # print(rs5)
    # print("hello, ", sum)
    i=0
    j=0
    k=0

    while sum < 11:
        sum = 0
        sum += rs2
        # print(rs2)
        # print("hello, ", sum)
        while sum < 11:
            sum += rs1
            print(sum)
            if sum < 10:
                continue
            else:
                if sum == 10:
                    print("hello, ", sum)

