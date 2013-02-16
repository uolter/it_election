__author__ = 'uolter'


import settings
import twitter as tw

consumer_key = settings.consumer_key
consumer_secret = settings.consumer_secret
access_token = settings.access_token
access_token_secret = settings.access_token_secret


api = tw.Api(consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token_key=access_token,
            access_token_secret=access_token_secret,
            input_encoding=None,
            request_headers=None,
            cache=tw.DEFAULT_CACHE,
            shortner=None)
