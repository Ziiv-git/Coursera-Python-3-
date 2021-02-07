import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched
print("------")
x = page.json() # turn page.text into a python object
print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2)) # pretty print the results


# NOTE: requests-6-1: How would you request the URL http://bar.com/goodstuff?greet=hi+there&frosted=no using the requests module?
# requests.get("http://bar.com/goodstuff", params = {'greet': 'hi there', 'frosted':'no'})
# The ? and & are added automatically, and the space in hi there is automatically encoded as %3A.

import requests

# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
kval_pairs = {'rel_rhy': 'funny'}
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched

d = {'q': '"violins and guitars"', 'tbm': 'isch'}
results = requests.get("https://google.com/search", params=d)
print(results.url)

import requests

def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["rel_rhy"] = word
    params_diction["max"] = "3" # get at most 3 results
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    word_ds = resp.json()
    return [d['word'] for d in word_ds]
    return resp.json() # Return a python object (a list of dictionaries in this case)

print(get_rhymes("funny"))

# NOTE: request with caching
import requests_with_caching
# it's not found in the permanent cache
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="datamuse_cache.txt")
print(res.text[:100])
# this time it will be found in the temporary cache
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="datamuse_cache.txt")
# This one is in the permanent cache.
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=funny", permanent_cache_file="datamuse_cache.txt")

import requests
import json

PERMANENT_CACHE_FNAME = "permanent_cache.txt"
TEMP_CACHE_FNAME = "this_page_cache.txt"

def _write_to_file(cache, fname):
    with open(fname, 'w') as outfile:
        outfile.write(json.dumps(cache, indent=2))

def _read_from_file(fname):
    try:
        with open(fname, 'r') as infile:
            res = infile.read()
            return json.loads(res)
    except:
        return {}

def add_to_cache(cache_file, cache_key, cache_value):
    temp_cache = _read_from_file(cache_file)
    temp_cache[cache_key] = cache_value
    _write_to_file(temp_cache, cache_file)

def clear_cache(cache_file=TEMP_CACHE_FNAME):
    _write_to_file({}, cache_file)

def make_cache_key(baseurl, params_d, private_keys=["api_key"]):
    """Makes a long string representing the query.
    Alphabetize the keys from the params dictionary so we get the same order each time.
    Omit keys with private info."""
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)

def get(baseurl, params={}, private_keys_to_ignore=["api_key"], permanent_cache_file=PERMANENT_CACHE_FNAME, temp_cache_file=TEMP_CACHE_FNAME):
    full_url = requests.requestURL(baseurl, params)
    cache_key = make_cache_key(baseurl, params, private_keys_to_ignore)
    # Load the permanent and page-specific caches from files
    permanent_cache = _read_from_file(permanent_cache_file)
    temp_cache = _read_from_file(temp_cache_file)
    if cache_key in temp_cache:
        print("found in temp_cache")
        # make a Response object containing text from the change, and the full_url that would have been fetched
        return requests.Response(temp_cache[cache_key], full_url)
    elif cache_key in permanent_cache:
        print("found in permanent_cache")
        # make a Response object containing text from the change, and the full_url that would have been fetched
        return requests.Response(permanent_cache[cache_key], full_url)
    else:
        print("new; adding to cache")
        # actually request it
        resp = requests.get(baseurl, params)
        # save it
        add_to_cache(temp_cache_file, cache_key, resp.text)
        return resp


import requests_with_caching
import json

parameters = {"term": "Ann Arbor", "entity": "podcast"}
iTunes_response = requests_with_caching.get("https://itunes.apple.com/search", params = parameters, permanent_cache_file="itunes_cache.txt")

py_data = json.loads(iTunes_response.text)
for r in py_data['results']:
    print(r['trackName'])


import json
# import webbrowser

# apply for a flickr authentication key at http://www.flickr.com/services/apps/create/apply/?
# paste the key (not the secret) as the value of the variable flickr_key
flickr_key = 'yourkeyhere'

def get_flickr_data(tags_string):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = flickr_key # from the above global variable
    params_diction["tags"] = tags_string # must be a comma separated string to work correctly
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"] = 5
    params_diction["media"] = "photos"
    params_diction["format"] = "json"
    params_diction["nojsoncallback"] = 1
    flickr_resp = requests_with_caching.get(baseurl, params = params_diction, permanent_cache_file="flickr_cache.txt")
    # Useful for debugging: print the url! Uncomment the below line to do so.
    print(flickr_resp.url) # Paste the result into the browser to check it out...
    return flickr_resp.json()

result_river_mts = get_flickr_data("river,mountains")

# Some code to open up a few photos that are tagged with the mountains and river tags...

photos = result_river_mts['photos']['photo']
for photo in photos:
    owner = photo['owner']
    photo_id = photo['id']
    url = 'https://www.flickr.com/photos/{}/{}'.format(owner, photo_id)
    print(url)
    # webbrowser.open(url)
