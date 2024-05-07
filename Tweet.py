import json

class Tweet:
    id = 0
    authorId = 0
    userName = ""
    mediaKeys : list = []
    mediaObjects : list = []

    def __init__(self, json):
        print(json)
        self.id = None if 'id' not in json else json['id']
        self.authorId = None if 'author_id' not in json else json['author_id']
        self.mediaKeys = json['attachments']['media_keys']
        
        # media = j['includes']['media']

        # if self.mediaKeys is not None and media is not None:
        #     for key in self.mediaKeys:
        #         self.mediaUrls = media[key]
