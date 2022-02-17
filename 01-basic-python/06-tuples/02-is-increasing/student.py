# Write your code here
def is_increasing(ns):
    lijst1= []
    lijst2= []
    for i in range (len(ns)-1):
        j = (ns[i], ns[i+1])
        if j[0]>j[1]:
            return False
    return True



print(is_increasing([1,2,4,5,6]))
