from twitter_collection import authenticate_twitter_v2, collect_tweets
from tweet_storage import save_tweets_to_csv
l
BEARER_TOKEN = 'your bearer token'

if __name__ == "__main__":
    client = authenticate_twitter_v2(BEARER_TOKEN)
    
    if client:
        disaster_keywords = "flood OR earthquake OR hurricane OR need help"
        tweets = collect_tweets(client, disaster_keywords, count=100)
    
        if tweets:
            save_tweets_to_csv(tweets)
        else:
            print("No tweets collected.")
