import praw
import time
reddit = praw.Reddit(client_id='',
                            client_secret='',
                            username='',
                            password='',
                            user_agent='reputation bot by hacksorskill')

alts=['isaiasmoreno','true_market','processnow','graylyart','rtjdxcgomx6f0stucw',
      'amazingdatasets','theywantmetomakename','notsmallplayshani','heylookauser','raicle','datguythunder',
      'correct_cheesecake','tokucha','wooolf31','legitimate_purple','autoarchivebot','bigben2010']



verifs = {'isaiasmoreno':'iexe','true_market':'cfophilpostyourbook','processnow':'computenow','graylyart':
         'airlines','rtjdxcgomx6f0stucw ':'psjc1eamawcjwfbdf','theywantmetomakename':
         'calciumcitrate','theywantmetomakename':'timroxsox',
         'notsmallplayshani':'luluchick',
         'heylookauser':'lilfruini','raicle':'freepandas','datguythunder':'tman0004'
         ,'correct_cheesecake':'mimic1','tokucha':'kikiotsuka','wooolf31':'knightfall31','legitimate_purple':'cxg-pitch','autoarchivebot':'hacksorskill','bigben2010':'modsofgcx'}


subreddit=reddit.subreddit('giftcardexchange')
while True:
    for i in reddit.inbox.stream(pause_after=-1):
        if i is None:
            break
        if time.time() - i.created_utc < 60:
            if i.subject.lower() == "!verify" and str(i.author).lower() in alts:
                print(i)
                temp = reddit.redditor(verifs[str(i.author).lower()])
                
                flair = next(subreddit.flair(temp))
                t = flair['flair_text']
                t=t.split(" ") 
                t=t[0:2]
                t = " ".join(t)
                if "confirmed" in t.lower():
                    fclass = "green"
                elif "experienced" in t.lower():
                    fclass="purple"
                elif "top" in t.lower():
                    fclass="blue"
                else:
                    fclass="" 
                subreddit.flair.set(temp,t + " Rule2Verified",fclass)
                #259200
                reddit.subreddit('insertcustomname').flair.set(i.author,str(time.time() + 300))
                print("Reactivating " + str(temp))
                i.reply("Reactivated")
            else:
                pass
    for user in alts:
        try:
            
            if (next(reddit.subreddit('insertcustomname').flair(reddit.redditor(user)))["flair_text"]) is None:
                pass
            
            elif float(next(reddit.subreddit('insertcustomname').flair(reddit.redditor(user)))["flair_text"]) <= time.time():
                flairt = next(subreddit.flair(reddit.redditor(verifs[user.lower()])))["flair_text"]
                
                flairt=flairt.split(" ")
                flairt=flairt[0:2]
                flairt = " ".join(flairt)
                if "confirmed" in flairt.lower():
                    fclass = "green"
                elif "experienced" in flairt.lower():
                    fclass="purple"
                elif "top" in flairt.lower():
                    fclass="blue"
                else:
                    fclass="" 
                subreddit.flair.set(verifs[user.lower()],flairt,fclass)
                reddit.subreddit('insertcustomname').flair.set(user,"")
                print("Cleared user, time's up " + user)
                
        except Exception as e:
            print(e)
            break
