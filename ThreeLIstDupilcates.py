# Create 3 lists
# for each element in lists see if it is repeated in the other, then add the duplicate to dup list and print dup list
list1=[11, 22, 33, 88]
list2=[33, 44, 55]
list3=[55, 66, 77, 88]
for i in range(0, len(list1)):
    # print("Over Over")
    for j in range(0, len(list2)):
        if list1[i] == list2[j]:
            print("found a duplicate between list1 and list2,", list1[i])
        for k in range(0, len(list3)):
            if list2[j] == list3[k]:
                print("found a duplicate between list2 and list3,", list2[j])
            if list3[k] == list1[i]:
                print("found a duplicate between list1 and list3,", list3[k])
            # print(list3[k], list2[j], list1[i])
