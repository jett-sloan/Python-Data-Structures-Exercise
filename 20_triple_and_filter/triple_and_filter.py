def triple_and_filter(nums):
    new_list = []

    for num in nums:
        if num % 4 == 0:
            new_list.append(num * 3)
    
    return new_list

print(triple_and_filter([1, 12, 8, 4]))