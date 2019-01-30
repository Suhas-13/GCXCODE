import praw
import time
import os
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     username='repbot1234',
                     password='',
                     user_agent='reputation bot by hacksorskill')

import sys
alts=['isaiasmoreno','true_market','processnow','graylyart','rtjdxcgomx6f0stucw',
      'amazingdatasets','theywantmetomakename','notsmallplayshani','heylookauser','raicle','datguythunder',
      'correct_cheesecake','tokucha','wooolf31','legitimate_purple','autoarchivebot','bigben2010','tamkholy1','tamkholy','aacd001','motion70ver','oceanxyver','potion_19ver','qmager','hangryyyy']



verifs = {'isaiasmoreno':'iexe','true_market':'cfophilpostyourbook','processnow':'computenow','graylyart':
         'airlines','rtjdxcgomx6f0stucw ':'psjc1eamawcjwfbdf','amazingdatasets':
         'calciumcitrate','theywantmetomakename':'timroxsox',
         'notsmallplayshani':'luluchick',
         'heylookauser':'lilfruini','raicle':'freepandas','datguythunder':'tman0004'
         ,'correct_cheesecake':'mimic1','tokucha':'kikiotsuka','wooolf31':'knightfall31','legitimate_purple':'cxg-pitch','hacksorskills':'hacksorskill','bigben2010':'modsofgcx','tamkholy1':
          "tamkholy",'motion70ver':'motion70','oceanxyver':'oceanxy','potion_19ver':'potion_19','qmager':'antonniooo','hangryyyy':'ihugdomo','aacd001':'aacd00'}
subreddit=reddit.subreddit('giftcardexchange')
while True:
    try:
        for i in reddit.inbox.stream(pause_after=-1):
            
            if i is None:
                break
            if time.time() - i.created_utc < 300:
                print(i)
                if str(i) in map(str.strip,open("logrule2.txt")):
                    print("PASSING")
                    pass
                elif i.subject.lower() == "!verify" and str(i.author).lower() in alts:
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
                    reddit.subreddit('insertcustomname').flair.set(i.author,str(time.time() + 259200))
                    print("Reactivating " + str(temp) + t)
                    i.reply("Reactivated")
                    with open("logrule2.txt","a+") as f:
                        f.write(i.id + "\n")  
                else:
                    pass
    except Exception as e:
        print(e)
    
        pass
    for user in alts:
        try:
            
            if (next(reddit.subreddit('insertcustomname').flair(reddit.redditor(user)))["flair_text"]) is None or (next(reddit.subreddit('insertcustomname').flair(reddit.redditor(user)))["flair_text"]) == " " or(next(reddit.subreddit('insertcustomname').flair(reddit.redditor(user)))["flair_text"]) == "":
                #print("passing " + user)
                pass
            
            elif float(next(reddit.subreddit('insertcustomname').flair(reddit.redditor(user)))["flair_text"]) + 259200 <= time.time():
                flairt = next(subreddit.flair(reddit.redditor(verifs[user.lower()])))["flair_text"]
                print(flairt)
                
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
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            break

