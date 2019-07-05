from textblob import TextBlob
import tweepy


con_key = 'wrLnUwMx5Y14xnRTjaIUx9PY9'
con_secrect = 'gA4dIGiDtBSy8GVehmG3ryGttH3GLzDLSnif5Lw0PxbmCq6h2S'
acc_tok = '1145775012055519233-83pruLeKDnbs9v2wdaDAaRHDsDrxBQ'
acc_tok_sec = '9q5MUy9abwGvbvT0Q9c69tNU3p28XBtmt5LkVKgHEKOjD'

auth = tweepy.OAuthHandler(con_key,con_secrect)

auth.set_access_token(acc_tok,acc_tok_sec)

api = tweepy.API(auth)

tweets = api.search('trump')

for t in tweets:
    print(t.text)
    analysis = TextBlob(t.text)
    print(analysis.sentiment)

