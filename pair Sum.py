def findPairs(List,target):
    for i in range(len(List)):
        for j in range(i+1,len(List)):
            if List[i]==List[j]:
                continue
            elif List[i]+List[j]==target:
                print(i, j)
myList=[1,2,3,2,3,4,5,6]
findPairs(myList,6)
