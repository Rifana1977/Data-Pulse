import tweepy

def authenticate_twitter_v2(bearer_token):
    """Authenticate with Twitter API v2 and return a Client object."""
    try:
        client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)
        print("Authentication OK")
        return client
    except tweepy.TweepyException as e:
        print(f"Error during authentication: {e}")
        return None

def collect_tweets(client, query, count=100):
    """Collect tweets using the Twitter API v2."""
    try:
        response = client.search_recent_tweets(query=query, max_results=count, tweet_fields=['created_at', 'text', 'author_id', 'geo'])
        tweet_data = [
            {
                'id': tweet.id, 
                'user': tweet.author_id, 
                'text': tweet.text,
                'created_at': tweet.created_at, 
                'location': tweet.geo
            }
            for tweet in response.data
        ]
        return tweet_data
    except tweepy.TweepyException as e:
        print(f"Error: {e}")
        return None
