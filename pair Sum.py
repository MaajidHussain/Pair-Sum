def findPairs(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                continue
            elif arr[i]+arr[j]==target:
                print(i, j)
myList=[1,2,3,2,3,4,5,6]
findPairs(myList,6)