def FindTarget(L,Target):
    temp_list=[]
    for i in L:
        temp=Target-i
        if temp in temp_list:
            res=(i,temp)
            return res
        temp_list.append(i)

    return ()

L=[int(x) for x in input("Enter list of integers: ").split()]
Target=int(input("Enter target value: "))

print(FindTarget(L,Target))
