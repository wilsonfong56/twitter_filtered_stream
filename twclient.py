import tweepy
import hidden

passwords = hidden.oauth()
auth = tweepy.OAuthHandler(passwords["consumer_key"], passwords["consumer_key_secret"])
auth.set_access_token(passwords["access_token"], passwords["access_token_secret"])
c = tweepy.Client(auth)
c.get_user("RogerTheKangroo")