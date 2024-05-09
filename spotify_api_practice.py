"""
Practice Restful APIs and JSON calls

Thought Process
-- Looked at example code presented, recreate own version for understanding
https://www.geeksforgeeks.org/python-api-tutorial-getting-started-with-apis/#making-api-requests-in-python
--How does enumerate work, what is in argument (only iterables) and datatype as output
--What is JSON, what does .dumps do? (Make python object into JSON)
      --Where is the python object from? request.get('article', []) as list
"""

import json
import requests


# Replace 'API_KEY' with your actual API key from NewsAPI
API_KEY = '3805f6bbabcb42b3a0c08a489baf603d'
API_url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"

#Output JSON format after requests
response = requests.get(API_url)
api_data = response.json()
# print(response.json() )


##Get Specific Key
# for key in api_data:
#     print(key)

##Print first article
# print(api_data['articles'][:1])

def print_article(api_url):
    if response.status_code == 200:
        #Then print our article
        #Get's a list datatype of articles for iteration, use dumps later
        articles = response.json().get('articles', [])
        for idx, article in enumerate(articles[0:4]): #Since list, can slice to shorten when enumerate
            json_article = json.dumps(article)
            print(json_article)
    else:
        return print('There is an error', response.status_code)

print_article(API_url)