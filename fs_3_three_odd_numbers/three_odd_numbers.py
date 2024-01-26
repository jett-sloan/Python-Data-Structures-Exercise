def three_odd_numbers(nums):
    result = 0
    for num in range(min(3, len(nums))):
        result += nums[num]
    return result % 2 == 1
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
print(three_odd_numbers([1,2,4,12,54,76]))