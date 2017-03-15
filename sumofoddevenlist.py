numList = list( map( int, input().split(" ")))
evenList = [x for x in numList if x % 2 is 0]
oddList = [x for x in numList if x % 2 is 1]
print(sum(oddList)-sum(evenList))