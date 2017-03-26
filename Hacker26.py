Date1 = list(map(int,input().split(' ')))
Date2 = list(map(int,input().split(' ')))
#Date2 is the date they are actually expecting the book
#Date1 is the date the book is returned
fine = 0;
if Date1[2] > Date2[2]:
    print(10000)
elif Date1[1] > Date2[1]:
    # print(str(Date2[1])+" is less than "+str(Date1[1])+"Month")
    if(Date1[2]<Date2[2]):
        print("0")
    else:
        x = abs(500 * (Date2[1]-Date1[1]))
        print(str(x))
elif Date1[0] > Date2[0]:
    # print(str(Date2[0])+" is less than "+str(Date1[0])+"Date")
    # print(str(Date1[2])+" The year is less than  "+str(Date1[2]))
    if(Date1[2] < Date2[2]):
        print("0")
    else:
        x = abs(15 * (Date2[0]-Date1[0]))
        print(str(x))
else:
    print("0")
    




# Date1 = list(map(int,input().split(' ')))
# Date2 = list(map(int,input().split(' ')))
# fine = 0
# if Date2[2] < Date1[2]:
#     print(10000)
# elif Date2[1] < Date1[1]:
#     x = abs(500 * (Date2[1]-Date1[1]))
#     print(str(x))
# elif Date2[0] < Date1[0]:
#     x = abs(15 * (Date2[0]-Date1[0]))
#     print(str(x))
# else:
#     print("0")
    