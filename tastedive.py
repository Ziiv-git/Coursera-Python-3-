import requests_with_caching
import json

def get_movies_from_tastedive(s):
    baseurl = "https://tastedive.com/read/api/similar"
    params_diction = {} # from the above global variable
    params_diction["tags"] = q, type, limit # must be a comma separated string to work correctly
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "tastedive.search"
    params_diction["per_page"] = 5
    params_diction["media"] = "photos"
    params_diction["format"] = "json"
    params_diction["nojsoncallback"] = 1
    tastedive_resp = requests_with_caching.get(baseurl, params = params_diction)
    # Useful for debugging: print the url! Uncomment the below line to do so.
    print(tastedive_resp.url) # Paste the result into the browser to check it out...
    return tastedive_resp.json()

result_river_mts = get_movies_from_tastedive("movies")


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")
