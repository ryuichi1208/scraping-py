def get_all_tweets(screen_name):
    alltweets = []
    new_tweets = api.user_timeline(screen_name=screen_name,count=200)
    alltweets.extend(new_tweets)
    if len(alltweets) > 200: # greater than 200 tweets 
        oldest=alltweets[-1].id-1
        while len(new_tweets)>0:
            alltweets = []
            oldest=0 
            print("getting tweets before %s" %(oldest))
            new_tweets = api.user_timeline(screen_name=screen_name,count=200,max_id=oldest)#
            alltweets.extend(new_tweets)
            oldest=alltweets[-1].id-1
            print("...%s tweets downloaded so far" % (len(alltweets)))
        outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    elif len(alltweets) > 1: # less than or eq to 200 tweets
        oldest=alltweets[-1].id-1
        outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    else: # for 0-1 tweets
        oldest=0
        if len(alltweets) > 0: # for 1 tweet user
            outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
        else: # for no tweet users
            outtweets=[]
