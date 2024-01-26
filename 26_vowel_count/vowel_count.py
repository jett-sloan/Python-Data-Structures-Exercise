def vowel_count(phrase):
    vowels = "aeiou"
    phrase = phrase.lower()
    count_map = {}
    for char in phrase:
        if char in vowels:
            count_map[char] =  count_map.get(char, 0) + 1
    return count_map




result1 = vowel_count('water bottle and a polar pop')
print(result1)









