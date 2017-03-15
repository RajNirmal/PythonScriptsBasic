n = int( input() )
numList = list ( map(int, input().split(' ')))
#This is my Implemtation and this is inefficient as there are more number of variables
#invovled and it a loop which executes n times
# for index,value in enumerate(numList):
#     if( value <= minValue ):
#         minIndex = index
#         minValue = value
#     elif (value > maxValue):
#         maxIndex = index
#         maxValue = value

#This is the code I saw on SO so I am trying it
minIndex = numList.index(min(numList))
maxIndex = numList.index(max(numList))
numList[minIndex],numList[maxIndex] = numList[maxIndex],numList[minIndex]        
print(*numList)




