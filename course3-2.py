lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing = map(lambda fruit:'Fruit: ' + fruit, lst_check)
print(map_testing)


countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

b_countries = filter(lambda word: 'B' in word, countries)
print(b_countries)


people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

first_names = [name[1] for name in people]
print(first_names)

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

lst2 = [v*2 for v in lst]
print(lst2)


students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed = [name[0] for name in students if name[1] >= 70]
print(passed)


l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
l3 = zip(l1,l2)
opposites = list(filter(lambda s: len(s[0])>3 and len(s[1])>3, l3))
print(opposites)


species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

pop_info = zip(species,population)
print(pop_info)

endangered = [e[0] for e in pop_info if e[1]<2500]
print(endangered)
