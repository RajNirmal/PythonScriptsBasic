n = int(input())
myList = []
for i in range(1, n+1):
    myList.append(i)
    if i%2 is 1:
        print ("*"+"".join( str(item) for item in myList))
    else:
        myList.reverse()
        print("".join( str(item) for item in myList)+"*")
        myList.reverse()