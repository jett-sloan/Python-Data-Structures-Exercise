def has_truthy_element(lst):
    for item in lst:
        if not isinstance(item, list):
            return False
    return True

print(has_truthy_element([[1], "nope"]))