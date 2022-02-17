# Write your code here
def frequencies(xs):
    count={}
    for element in xs:
        if element in count:
           count[element] +=1
        else :
            count[element] = 1
    return count;
print(frequencies([1,3,4,5,6,6]))