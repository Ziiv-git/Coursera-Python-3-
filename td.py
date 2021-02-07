import requests_with_caching
import json

# NOTE: defining and setting the connection
def get_movies_from_tastedive(title):
    url = 'https://tastedive.com/api/similar'
    param_dict = {}
    param_dict['q']= title
    param_dict['type']= 'movies'
    param_dict['limit']= 5
    tastedive_cache = requests_with_caching.get(url, params=param_dict)
    print(json.loads(tastedive_cache.text))
    return json.loads(tastedive_cache.text)
# NOTE: (output of the above code) found in permanent_cache
# {'Similar': {'Info': [{'Name': 'Black Panther', 'Type': 'movie'}], 'Results': [{'Name': 'Captain Marvel', 'Type': 'movie'}, {'Name': 'Avengers: Infinity War', 'Type': 'movie'}, {'Name': 'Ant-Man And The Wasp', 'Type': 'movie'}, {'Name': 'The Fate Of The Furious', 'Type': 'movie'}, {'Name': 'Deadpool 2', 'Type': 'movie'}]}}
# ['Captain Marvel', 'Avengers: Infinity War', 'Ant-Man And The Wasp', 'The Fate Of The Furious', 'Deadpool 2']

# NOTE: extracting the titles from the above function
def extract_movie_titles(titles):
    return ([i['Name'] for i in titles['Similar']['Results']])
# NOTE: output:
# {'Similar': {'Info': [{'Name': 'Tony Bennett', 'Type': 'music'}], 'Results': [{'Name': 'The Startup Kids', 'Type': 'movie'}, {'Name': 'Charlie Chaplin', 'Type': 'movie'}, {'Name': 'Venus In Fur', 'Type': 'movie'}, {'Name': 'Loving', 'Type': 'movie'}, {'Name': 'The African Queen', 'Type': 'movie'}]}}

# NOTE: Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input.
#It gets five related movies for each from TasteDive, extracts the titles
#for all of them, and combines them all into a single list. Don’t include the same movie twice.
def get_related_titles(movie_list):
    lst = []
    for movie in movie_list:
        lst.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(lst))

print(get_related_titles(["Black Panther", "Captain Marvel"]))
# NOTE: output:
# NOTE: ['Captain Marvel', 'Avengers: Infinity War', 'Ant-Man And The Wasp', 'The Fate Of The Furious', 'Deadpool 2', 'Inhumans', 'Venom', 'American Assassin', 'Black Panther']


def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param_dict1 = {}
    param_dict1['t'] = title
    param_dict1['r'] = 'json'
    omdb_cache = requests_with_caching.get(endpoint, params=param_dict1)
    return json.loads(omdb_cache.text)

print(get_movie_data("Venom"))
# NOTE: output:
# NOTE: {'Type': 'movie', 'Response': 'True', 'Title': 'Venom', 'Year': '2018', 'Rated': 'N/A', 'Released': '05 Oct 2018', 'Runtime': '112 min', 'Genre': 'Action, Sci-Fi', 'Director': 'Ruben Fleischer', 'Writer': "Jeff Pinkner (screenplay by), Scott Rosenberg (screenplay by), Kelly Marcel (screenplay by), Jeff Pinkner (screen story by), Scott Rosenberg (screen story by), Todd McFarlane (Marvel's Venom Character created by), David Michelinie (Marvel's Venom Character created by)", 'Actors': 'Tom Hardy, Michelle Williams, Riz Ahmed, Scott Haze', 'Plot': 'When Eddie Brock acquires the powers of a symbiote, he will have to release his alter-ego "Venom" to save his life.', 'Language': 'English', 'Country': 'USA, China', 'Awards': 'N/A', 'Poster': 'https://m.media-amazon.com/images/M/MV5BNzAwNzUzNjY4MV5BMl5BanBnXkFtZTgwMTQ5MzM0NjM@._V1_SX300.jpg', 'Ratings': [{'Source': 'Internet Movie Database', 'Value': '6.9/10'}, {'Source': 'Metacritic', 'Value': '35/100'}], 'Metascore': '35', 'imdbRating': '6.9', 'imdbVotes': '154,911', 'imdbID': 'tt1270797', 'DVD': '18 Jun 2013', 'BoxOffice': 'N/A', 'Production': 'Vis', 'Website': 'N/A'}
def get_movie_rating(dic):
    ranking = dic['Ratings']
    for dic_item in ranking:
        if dic_item['Source'] == 'Rotten Tomatoes':
            return int(dic_item['Value'][:-1])
    return 0

def get_sorted_recommendations(list):
    new_list = get_related_titles(list)
    new_dict = {}
    for i in new_list:
        rating = get_movie_rating(get_movie_data(i))
        new_dict[i] = rating
    print(new_dict)
    #print(sorted(new_dict, reverse=True))
    return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]

# NOTE: {'Baby Mama': 64, 'The Five-Year Engagement': 63, 'Bachelorette': 56, 'The Heat': 65, 'Date Night': 67, 'Sherlock Holmes: A Game Of Shadows': 60, 'Yahşi Batı': 0, 'Eyyvah Eyvah': 0, 'Pirates Of The Caribbean: On Stranger Tides': 32, 'Prince Of Persia: The Sands Of Time': 36}
