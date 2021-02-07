try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception as e:
    print("got an error")
    print(e)

print("continuing")



gold = {"US":46, "Fiji":1, "Great Britain":27, "Cuba":5, "Thailand":2, "China":26, "France":10}
country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
country_gold = []
for x in country:
    try:
        x in gold.keys()
        country_gold.append(gold[x])
    except KeyError:
        country_gold.append("Did not get gold")

print(country_gold)


di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        diction.keys() == "Puppies"
        total = total + diction['Puppies']
    except:
        pass

print("Total number of puppies:", total)
print("Total number of puppies:", total)


numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

remainder = []
for i in numb:
    if (i == 0):
        remainder.append("Error")
    elif (36 % i):
        remainder.append(36 % i)
    elif (36 % i == 0):
        remainder.append(0)
print(remainder)



lst = [2,4,10,42,12,0,4,7,21,4,83,8,5,6,8,234,5,6,523,42,34,0,234,1,435,465,56,7,3,43,23]

lst_three = []

for num in lst:
    try:
        if 3 % num == 0:
            lst_three.append(num)
    except:
        pass


full_lst = ["ab", 'cde', 'fgh', 'i', 'jkml', 'nop', 'qr', 's', 'tv', 'wxy', 'z']

attempt = []

for elem in full_lst:
    try:
        attempt.append(elem[1])
    except IndexError:
        attempt.append("Error")
print(attempt)




conts = [['Spain', 'France', 'Greece', 'Portugal', 'Romania', 'Germany'], ['USA', 'Mexico', 'Canada'], ['Japan', 'China', 'Korea', 'Vietnam', 'Cambodia'], ['Argentina', 'Chile', 'Brazil', 'Ecuador', 'Uruguay', 'Venezuela'], ['Australia'], ['Zimbabwe', 'Morocco', 'Kenya', 'Ethiopa', 'South Africa'], ['Antarctica']]

third_countries = []

for c in conts:
    try:
        third_countries.append(c[2])
    except IndexError:
        third_countries.append("Continent does not have 3 countries")
print(third_countries)



sport = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]

ppl_play = {"hockey":4, "soccer": 10, "football": 15, "tennis": 8}

for x in sport:
    try:
        print(ppl_play[x])
    except KeyError:
        ppl_play[x] = 1



di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        diction.keys() == "Puppies"
        total = total + diction['Puppies']
    except:
        pass
    if("Puppies" not in diction.keys()):
        diction["Puppies"] = 0

print("Total number of puppies:", total)
