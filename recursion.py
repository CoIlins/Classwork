# def fib(n):
#     if n == 1:
#         return 1
#     if n== 2:
#         return 1
#     elif n> 2 :
#         return fib(n-1) + fib(n-2)
#
#
#
# # for number in range(5): # too many recursive calls
# #     print(f"{number}: {fib(number)}")
#
# f_cache = {}#memoization
# value  = 0
# def fib2(n):
#    if n in f_cache:
#         return f_cache[n]
#
#    if n  == 1:
#         value = 1
#    elif n == 2:
#         value = 1
#    elif n > 2:
#         value = fib2(n-1) + fib2(n-2)
#
#    f_cache[n] = value
#    return value
#
# # for n in range (1, 1000):
# #     print(n, ":", fib2(n))
# ## print (f"{n} : {fib2(n)}")
#
from functools import lru_cache
# # least recently used cache

@lru_cache(maxsize = 1000)
def fib3(k):

    if k == 1:
        return 1
    if k == 2:
        return 1
    elif k > 2:
        return fib3(k - 1) + fib3(k-2)

for i in range (1000):
    print (f"{i } : {fib3(i)}")



