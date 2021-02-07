weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

sorted_weather = sorted(weather, key=lambda w: (w, weather[w]['temp']))

print(sorted_weather)

sorted_weather1 = sorted(weather, key=lambda w: (w, -weather[w]['temp']), reverse=True)
print(sorted_weather1)

sorted_weather2 = sorted(weather)
print(sorted_weather2)

sorted_weather3 = sorted(weather, key = lambda w: (-weather[w]['temp']))
print(sorted_weather3)
