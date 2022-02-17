# Write your code here
import math


def median(ns):
    sortedNs = ns.copy()
    sortedNs.sort()
    i = math.floor(len(ns)/2)
    if len(sortedNs)%2 == 0 :
        return (sortedNs[i-1]+sortedNs[i])/2
    else :
        return sortedNs[i]

