import pyshorteners as sh
import json

# reading to sample.json
with open('sample.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)
    print(json_object)

# get the long url from user
# ==========================
long_url = input("please provide the long URL : ")

# checking for already exists in json file
# if exists return the created one
if long_url in json_object:
    short_url = json_object[long_url]
    print('already present')
    
# if not present create a new one and append to the file and then return the short url
else:
    print('created new one')
    # after checking with json if there is no link already in json create a short url
    s = sh.Shortener()
    short_url = s.tinyurl.short(long_url)

    # after creating the url append to the file
    json_object[long_url] = short_url
    with open("sample.json", "w") as outfile:
        json.dump(json_object, outfile)

print(short_url)






