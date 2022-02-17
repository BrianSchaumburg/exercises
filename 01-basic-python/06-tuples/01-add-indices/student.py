# Write your code here
def add_indices(xs):
    result = []
    indices=[]
    for i in range(len(xs)):
        indices.append(i)
    result= list(zip(indices,xs))
    return result




