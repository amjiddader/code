import dailymotion

API_KEY= '779ec11d28087c2825a1'
API_SECRET= '7110b4277e7e9f46e333c79114ead86c2f6e06aa'
USERNAME= 'mawiya@outlook.be'
PASSWORD= 'amigr8@16D'



d = dailymotion.Dailymotion()
d.set_grant_type('password', api_key=API_KEY, api_secret=API_SECRET,
    scope=['userinfo'], info={'username': USERNAME, 'password': PASSWORD})
url = d.upload('video.mp4')
d.post('/me/videos',
    {'url': url, 'title': 'MyTitle', 'published': 'false', 'channel': 'news'})
