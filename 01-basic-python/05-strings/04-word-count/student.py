# Write your code here
def word_count(string):
    count = 1
    for i in string:
        if i == ' ':
            count += 1
    return count



