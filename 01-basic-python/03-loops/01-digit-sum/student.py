# Write your code here
import math


def digit_sum(n):
    result = 0
    while n > 0 :
        result += n %10
        n = math.floor(n/10)
    return result