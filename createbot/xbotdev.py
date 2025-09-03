import tweepy

auth = tweepy.OAuth1UserHandler(

)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.get_user(screen_name="Twitter")

print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)
