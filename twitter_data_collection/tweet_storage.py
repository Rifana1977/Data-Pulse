import csv

def save_tweets_to_csv(tweets, filename="disaster_tweets.csv"):
    """Save collected tweets to a CSV file."""
    if tweets:
        keys = tweets[0].keys()
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(tweets)
        print(f"Saved {len(tweets)} tweets to {filename}")
    else:
        print("No tweets to save.")
