def lcs(s1,s2,l1,l2):
    L=[[0 for i in range(l2+1)] for j in range(l1+1)]

    length=0
    row=0
    col=0

    for i in range(l1+1):
        for j in range(l2+1):
            if i==0 or j==0:
                L[i][j]=0
            elif s1[i-1]==s2[j-1]:
                L[i][j] = L[i-1][j-1]+1
                if length < L[i][j]:
                    length = L[i][j]
                    row=i
                    col=j
            else:
                L[i][j] = 0


    result=""

    if length==0:
        print("No Common Substring")
        return

    while L[row][col] !=0:
        length-=1
        result+=s1[row-1]

        row-=1
        col-=1

    print("Longest common substring is: "+ result[::-1])

input_1=input("Enter string 1: ")
input_2=input("Enter string 2: ")
l1=len(input_1)
l2=len(input_2)
lcs(input_1,input_2,l1,l2)
