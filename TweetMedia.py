import json

class TweetMedia:
    mediaKey = ""
    type = ""
    url = ""

    def __init__(self, json):
        self.mediaKey = json['media_key']
        self.type = json['type']
        if self.type == 'photo':
            self.url = json['url']