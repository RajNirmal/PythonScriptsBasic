#!/bin/python3

import sys


def max_and(n, k):
    r = 0
    b = 1
    while b < k:
        b <<= 1
    while b:
        # Can we set bit b in the result?
        # We can't if r|b >= k.
        # Otherwise, are there two numbers greater than or equal to r,
        # and less than n, both with bit b set?
        # The two smallest numbers greater than or equal to r with
        # bit b set are r|b and ((r|b) + 1) | (r|b). We need only
        # test the latter against n.
        if (r | b) | ((r | b) + 1) < n and r|b < k:
            r |= b
        b >>= 1
    return r

t = int(input().strip())
for a0 in range(t):
    maxValue = 0
    n,k1 = input().strip().split(' ')
    n,k1 = [int(n),int(k1)]
    x = max_and(n,k1)
    print(str(x))
    
# #!/bin/python3

# import sys


# t = int(input().strip())
# for a0 in range(t):
#     maxValue = 0
#     n,k1 = input().strip().split(' ')
#     n,k1 = [int(n),int(k1)]
#     for j in range (1,n):
#         for k in range (j+1,n):
#             jkValue = j&k
#             if jkValue > maxValue and jkValue < k1:
#                 maxValue = jkValue
#     print(maxValue)