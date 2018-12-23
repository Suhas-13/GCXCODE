import praw
import time
from notify_run import Notify
notify = Notify()

reddit = praw.Reddit(client_id='',
                            client_secret='',
                            username='',
                            password='',
                            user_agent='reputation bot by hacksorskill')
subreddit=reddit.subreddit('giftcardexchange')



while True:
    try:
        for submission in subreddit.stream.submissions(pause_after=-1):
            
            if submission is None:
                break
            else:
            
                now=time.time()
                if (now - submission.created_utc < 700) and submission.id not in map(str.strip, open("gcxall.txt")):
                    
                    notify.send(submission.title + " by u/" + str(submission.author), submission.url)
                    with open("gcxall.txt","a+") as f:
                            f.write(submission.id + "\n")

                    if (submission.author_flair_text == "GCX Beginner" or submission.author_flair_text is None):
                         
                            
                        print("found one " + submission.url)
                        
                        submission.mod.remove()
                        submission.reply("Please read the message under WARNING!!! MUST READ to learn how to trade safely and have your post restored.\n\n\n\nNo one can see your post until you restore it by reading and following instructions.\n\n\n\nI'm a bot!")
                         
                        
                else:
                    pass
        for comment in subreddit.stream.comments(pause_after=-1):
            try:
                if comment is None:
                    break
                else:
                    if open("currentcode.txt","r").read() in comment.body:
                        parent=comment.parent()
                        if parent.banned_by == "hacksorskillbot":
                            print('approving ' + parent.id)
                            parent.mod.approve()
                            
                            for comment in parent.comments:
                                if str(comment.author) == "hacksorskillbot":
                                    comment.edit("Your post has been restored.\n\nTrade Safely!\n\n\nI'm a bot!")
                                else:
                                    pass
                            
                    else:
                        pass
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
        pass

