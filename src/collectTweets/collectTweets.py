import tweepy
import pandas as pd

def main():
    # トークン周り
    consumer_key = 'write your consumer_key'
    consumer_secret = 'write your consumer_secret'
    access_token = 'write your access_token'
    access_token_secret = 'write your access_token_secret'

    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, access_token, access_token_secret
    )

    # ツイートの取得
    api = tweepy.API(auth)
    search_word = 'ワールドカップ'
    tweets = api.search_tweets(q = search_word, count=100, lang='ja')

    tweet_list = []
    for tweet in tweets:
        tweet_list.append(tweet.text.replace('\n', ''))

    df = pd.DataFrame(tweet_list)
    df.to_csv('./data/tweets.csv', encoding='utf-8', header=None, index=False)


if __name__ == "__main__":
    main()

