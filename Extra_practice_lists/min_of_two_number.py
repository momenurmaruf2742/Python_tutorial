from functools import reduce

class MinNumber():
    # Naiv aproch // statement
    def minimumNumberNaiv(a,k):
        if a > k:
            return k
        else:
            return a
    # Using Lamda functions
    def minimumNumberLamda(a,k):

        minimum = reduce(lambda x, y: x if x < y else y, [a, k])
        return minimum
    # using sorted function
    def minimumNumberSorted(a,b):

        # a = 2
        # b = 4
        return(sorted([a, b])[0])
    
final=MinNumber
print(final.minimumNumberNaiv(2,1))


