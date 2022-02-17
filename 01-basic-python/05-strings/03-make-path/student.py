# Write your code here
def make_path(parts):
    new = ""
    for i in parts:
        if i != parts[-1]:
            new += i + "/"
        else :
            new += i
    return new


print(make_path(['a', 'b', 'c']))
