import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL =  "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

        response = requests.get(URL)
        return response.content

    def load_json(self):
        occupation_list = []
        occupations = json.loads(self.get_response_body())
        for occupation in occupations:
            occupation_list.append(occupation)
        
        return occupation_list
    
occupations = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
occupation_list = occupations.load_json()

for occupation in occupation_list:
    print (occupation)

    