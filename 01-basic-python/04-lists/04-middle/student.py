# Write your code here
# function middle(xs)
# {
#     // Look up how to find a list's length in Python
#     const index = Math.floor(xs.length / 2);
#
#     return xs[index];
# }
import math


def middle(xs):
    index = math.floor(len(xs)/2)
    return xs[index];