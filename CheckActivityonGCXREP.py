
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
        for i in reddit.redditor(user).comments.new(limit=35):
            
            if str(i.subreddit) == "FreeKarma4U" or str(i.subreddit) == "FreeKarma4You":
                    activevar = True
                    print('posted on freekarma')
                    return(activevar)
                    break
            
            elif int(time.time()) - int(i.created_utc) < 6480000:
                count+=1
                if count > 30:
                    activevar = False
                    return(activevar)
                    flag=True
                    break
        
                
        for i in reddit.redditor(user).submissions.new(limit=35):
            
            if int(time.time()) - int(i.created_utc) < 6480000:
                count+=1
                if flag == True:
                    activevar=False
                    return(activevar)
                    break
                if str(i.subreddit) == "FreeKarma4U" or str(i.subreddit) == "FreeKarma4You":
                    count=0
                    print("posted on freekarma")
                    activevar=True
                    return(activevar)
                    break
                elif count > 30:
                    activevar = False
                    return(activevar)
                    break
              
        if count < 26:
            activevar=True
            return(activevar)

        for i in reddit.redditor(user).submissions.new(limit=35):
            
            if int(time.time()) - int(i.created_utc) < 6480000:
                count+=1
                if flag == True:
                    activevar=False
                    return(activevar)
                    break
                if str(i.subreddit) == "FreeKarma4U" or str(i.subreddit) == "FreeKarma4You":
                    count=0
                    print("posted on freekarma")
                    activevar=True
                    return(activevar)
                    break
                elif count > 30:
                    activevar = False
                    return(activevar)
                    break
              
        if count < 26:
            activevar=True
            return(activevar)
        return(activevar)
    except:
        print('error')
        pass

subreddit=reddit.subreddit('gcxrep')
while True:
    try:
        for comment in subreddit.stream.comments():
            try:
              if str(comment.author) in map(str.strip,open("exceptionlist.txt")):
                  pass
              elif active(str(comment.author)) == True:
                  reddit.redditor("r/uselessposts").message(str(comment.author) + " has been marked as inactive or has posted on FreeKarma4U", "Link to profile: " + "https://reddit.com/u/" + str(comment.author))
                  print(comment.body)
                  
              else:
                  pass
            except Exception as e:
                print(e)
                pass                                                                                                                                                                                           
    except Exception as e:
        print(e)
        pass










