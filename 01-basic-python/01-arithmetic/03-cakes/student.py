# Write your code here
import math


def cakes(eggs, butter,flour):
    maxByEggs =math.floor(eggs/5)
    maxByButter= math.floor(butter/250)
    maxByFlour = math.floor(flour/5)
    return min(maxByEggs,maxByButter,maxByFlour)