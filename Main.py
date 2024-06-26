import os
import requests
import oauth2
import json
import urllib.request
from PIL import Image
from Tweet import Tweet
from TweetMedia import TweetMedia

bearerToken = os.environ.get("BEARER_TOKEN")

def createUrl(id):
    tweetFields = 'tweet.fields=id,author_id&expansions=attachments.media_keys&media.fields=url,type'
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
    print('Begin')
    #url, tweetFields = createUrl('3496145955')
    #jsonResponse = createRequest(url, tweetFields)

    #with open('data.json', 'w', encoding='utf-8') as f:
    #    json.dump(jsonResponse, f, ensure_ascii=False, indent=4)

    #print(json.dumps(jsonResponse, indent=4, sort_keys=True))
    #urllib.request.urlretrieve('https://pbs.twimg.com/media/GLxf-LGbUAAQV4E.jpg', '../XLikeScraper/images/asdf.jpg')
    #img = Image.open('../XLikeScraper/images/asdf.jpg')
    #img.show()

    tweets = []
    tweetMediaObjects = []

    with open('data.json', 'r', encoding='utf-8') as f:
        fs = json.load(f)

        for t in fs['data']:
            tweet = Tweet(t)
            tweets.append(tweet)
            if len(tweets) > 14:
                break

        for m in fs['includes']['media']:
            media = TweetMedia(m)
            print('running {}'.format(media.mediaKey))
            tweetMediaObjects.append(media)

        tweet: Tweet
        for tweet in tweets:
            for key in tweet.mediaKeys:
                m = list(filter(lambda x: x.mediaKey == key, tweetMediaObjects))[0]
                tweet.mediaObjects.append(m)

        t : Tweet
        m : TweetMedia
        for t in tweets:
            for m in t.mediaObjects:
                urllib.request.urlretrieve(m.url, '../XLikeScraper/images/{}.jpg'.format(m.mediaKey))

if __name__ == "__main__":
    main()

    #curl --request GET 'https://api.twitter.com/2/tweets?ids=1263145271946551300&expansions=attachments.media_keys&media.fields=duration_ms,height,media_key,preview_image_url,public_metrics,type,url,width,alt_text' --header 'Authorization: Bearer $BEARER_TOKEN'