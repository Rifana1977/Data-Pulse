from twitter_collection import authenticate_twitter_v2, collect_tweets
from tweet_storage import save_tweets_to_csv

# Replace with your own Bearer Token for Twitter API v2
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAOHpvgEAAAAAFAtaZgKwCJ1OGxIByyens%2FxXRY0%3Diq9BevETOLDwbFaTgOErO0NGO7ISsb2pOnWHUTFRPiFxY3eqmG'

if __name__ == "__main__":
    # Step 1: Authenticate with Twitter API v2
    client = authenticate_twitter_v2(BEARER_TOKEN)
    
    # Step 2: Collect Tweets
    if client:
        disaster_keywords = "flood OR earthquake OR hurricane OR need help"
        tweets = collect_tweets(client, disaster_keywords, count=100)
    
        # Step 3: Save Tweets to CSV
        if tweets:
            save_tweets_to_csv(tweets)
        else:
            print("No tweets collected.")
