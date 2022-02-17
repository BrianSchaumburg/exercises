# Write your code here
def remove_duplicates(xs):
    result=[]
    found =set()
    for i in xs:
        if i not in found :
            result.append(i)
            found.add(i)

    print(result)

