from textblob import TextBlob
import tweepy


con_key = ''
con_secrect = ''
acc_tok = ''
acc_tok_sec = ''

auth = tweepy.OAuthHandler(con_key,con_secrect)

auth.set_access_token(acc_tok,acc_tok_sec)

api = tweepy.API(auth)

tweets = api.search('trump')

for t in tweets:
    print(t.text)
    analysis = TextBlob(t.text)
    print(analysis.sentiment)

