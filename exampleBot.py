#http://www.whycouch.com/2014/05/how-to-create-simple-reddit-bot-in-10.html
# author: Hathy (WhyCouch)
 
import praw
import time
 
# Initialize PRAW with a custom User-Agent
 
r = praw.Reddit('Simple comment parser from WhyCouch')
 
polite_users = set()   # to avoid duplicates
 
for i in xrange(0,10):  # Run the loop 10 times
    comments = r.get_comments('askreddit')
    for comment in comments:
        body = comment.body.lower()
        if body.find("thank") != -1 or body.find("please") != -1:
            polite_users.add(comment.author)
    time.sleep(120)   # Sleep for 2 minutes
 
print "The polite users were :"
for user in polite_users:
    print user
