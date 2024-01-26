def partition(lst, fn):
    #Partition lst by predicate.
    # 
    # - lst: list of items
    # - fn: function that returns True or False
    # 
    # Returns new list: [a, b], where `a` are items that passed fn test,
    #and `b` are items that failed fn test.
    is_true = []
    is_false = []
    for x in lst:
        if fn(x):
            is_true.append(x)
        else: 
            is_false.append(x)  

    return [is_true, is_false]


def is_even(num):
    return num % 2 == 0

def is_string(el):
    return isinstance(el, str)

print(partition([1, 2, 3, 4], is_even))
#[[2, 4], [1, 3]]

print (partition(["hi", None, 6, "bye"], is_string))
#[['hi', 'bye'], [None, 6]]

