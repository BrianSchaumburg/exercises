# Write your code here
def from_lists(keys,values):
    returnlist = {}
    for i in range(len(keys)):
        returnlist[keys[i]] = values[i]
    return returnlist
print(from_lists([1,2,3],['un','deux','trois']))