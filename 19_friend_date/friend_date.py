def friend_date(a, b):
    hobby_1 = set(a[2])
    hobby_2 = set(a[2])
    common_hobby = hobby_1.intersection(hobby_2)
    if common_hobby:
        return common_hobby



elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

result = friend_date(elmo, sauron)
print(result)