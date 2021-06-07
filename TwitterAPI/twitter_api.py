import tweepy
from os import getenv
from dotenv import load_dotenv

class TwitterAPI(object):
  consumer_key = None
  consumer_secret = None
  access_token = None
  access_token_secret = None

  api = None

  def __init__(self) -> None:
    load_dotenv()

    self.consumer_key = getenv('CONSUME_KEY')
    self.consumer_secret = getenv('CONSUMER_SECRET')
    self.access_token = getenv('ACCESS_TOKEN')
    self.access_token_secret = getenv('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
    auth.set_access_token(self.access_token, self.access_token_secret)

    self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

  def get_user_timeline(self, user_name):
    tweet_list = []
    for tweet in tweepy.Cursor(self.api.user_timeline, screen_name=user_name, tweet_mode="extended").items(10):
      tweet_list.append(tweet._json["full_text"])

    return tweet_list