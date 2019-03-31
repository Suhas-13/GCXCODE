
import praw
import time
from datetime import datetime

reddit = praw.Reddit(client_id='dt0u8lacZcydbg',
                     client_secret='GbjnUAnxbf_4u0SL4RFhkIdLqLE',
                     username='repbot1234',
                     password='fasttalker101',
                     user_agent='reputation bot by hacksorskill')
 
# look for phrase and reply appropriately


def active(user):
    try:
        flag=False
        activevar=None
        count = 0
        for i in reddit.redditor(user).comments.new(limit=150):
            
            if str(i.subreddit) == "GiftCardExchange":
                    activevar = False
                    print('posted on gcx')
                    return(activevar)
                    break
            
            elif int(time.time()) - int(i.created_utc) < 6480000:
                count+=1
                if count > 30:
                    activevar = False
                    return(activevar)
                    flag=True
                    break
        
                
        for i in reddit.redditor(user).submissions.new(limit=50):
            if str(i.subreddit) == "GiftCardExchange":
                   
                    print("posted on gcx")
                    activevar=False
                    return(activevar)
                    break
            
            elif int(time.time()) - int(i.created_utc) < 6480000:
                count+=1
                if flag == True:
                    activevar=False
                    return(activevar)
                    break
                
                elif count > 30:
                    activevar = False
                    return(activevar)
                    break
              
        if count < 30:
            activevar=True
            return(activevar)
            activevar=True
            return(activevar)

        return(activevar)
    except:
        print('error')
        pass

subreddit=reddit.subreddit('giftcardexchange')
while True:
    try:
        for comment in subreddit.stream.comments():
            try:
                if comment.author_flair_text == "GCX Beginner":
                    g=active(str(comment.author))
                    if g is True:
                        reddit.redditor('r/uselessposts').message('Post on GCX Detected, low activity + new user on sub ', "u/" + str(comment.author))
                    else:
                        pass
                    
                    
                    
                else:
                    pass
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
        pass


























