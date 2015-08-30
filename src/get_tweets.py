import twitterconfig
import tweepy

auth = tweepy.OAuthHandler(twitterconfig.CONSUMER_KEY, twitterconfig.CONSUMER_SECRET)
auth.set_access_token(twitterconfig.ACCESS_KEY, twitterconfig.ACCESS_SECRET)
api = tweepy.API(auth)

tweets = api.home_timeline(count = 10)
for i,tweet in enumerate(tweets):
	print str(i+1) + "   " + tweet.text.encode('utf-8')