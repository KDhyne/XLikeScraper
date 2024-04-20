import os
import requests
import oauth2
import json

print('aasdfdsfa')
bearerToken = os.environ.get("BEARER_TOKEN")


def createUrl(id):
    tweetFields = 'tweet.fields=lang,author_id'
    url = "https://api.twitter.com/2/users/{}/liked_tweets".format(id)
    return url, tweetFields

def bearerOauth(r):
    r.headers['Authorization'] = f'Bearer {bearerToken}'
    r.headers['User-Agent'] = 'XLikeScraper'
    return r

def createRequest(url, tweetFields):
    response = requests.request("GET", url, auth = bearerOauth, params=tweetFields)
    print(response.status_code)
    if  response.status_code != 200:
        raise Exception(
            'Request returned an error: {} {}'.format(
                response.status_code, response.text
            )
        )
    return response.json()

def main():
    url, tweetFields = createUrl('3496145955')
    jsonResponse = createRequest(url, tweetFields)
    print(json.dumps(jsonResponse, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()