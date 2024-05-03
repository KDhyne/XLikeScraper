import json

class Tweet:
    id = 0
    authorId = 0
    userName = ""
    mediaKeys : list = []
    mediaUrls : list = []

    def __init__(self, json_def):
        j = json.load(json_def)
        s = j['data']
        self.id = None if 'id' not in s else s['id']
        self.authorId = None if 'author_id' not in s else s['author_id']
        self.mediaKeys = [] if 'media_keys' not in s else s['attachments']['media_keys']
        
        media = j['includes']['media']

        if self.mediaKeys is not None and media is not None:
            for key in self.mediaKeys:
                self.mediaUrls = media[key]

        if len(media) > 0:
            count = 0
            for m in media:
                if len(self.mediaUrls) < count:
                    if self.mediaKeys.count(m['media_key']):
                        self.mediaUrls.append(m['url'])
                        count += 1
