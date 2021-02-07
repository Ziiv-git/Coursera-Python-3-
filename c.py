s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
sentence = s.split(' ')
vowels = ['a','e','i','o','u']
num_vowels = 0
for word in sentence:
    a = word.count('a')
    e = word.count('e')
    i = word.count('i')
    o = word.count('o')
    u = word.count('u')
    num_vowels = num_vowels + a + e + i + o + u

print(num_vowels)
