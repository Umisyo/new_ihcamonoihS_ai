import tweepy
from config import config

class AccessToApi:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(config['CONSUMER_KEY'], config['CONSUMER_SECRET'])
        self.auth.set_access_token(config['ACCESS_TOKEN'], config['ACCESS_TOKEN_SECRET'])
        
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
        