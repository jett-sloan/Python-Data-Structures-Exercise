def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    unique_nums = set(nums)
    print(unique_nums)
    current_most = 0
    current_mode = None
    for num in unique_nums:
        num_count = nums.count(num)
        print(num, num_count)
        if  num_count > current_most:
            current_most = num_count
            current_mode = num

    return current_mode
print(mode([2, 2, 3, 3, 2]))
print(mode([1, 2, 1]))
