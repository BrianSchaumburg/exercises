# Write your code here
def rotate(xs =[], n=int ):
    for i in range(0,n,1):
        element = xs[0]
        xs.remove(element)
        xs.append(element)
