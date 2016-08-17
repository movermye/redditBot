
def check_condition(c):
    print "inside test condition"
    print "printing text:"
    text = c.body
    print text
    print "printing tokens:"
    tokens = text.split()
    print tokens
    return True

def bot_action(c, verbose=True, respond=False):
    print "inside bot_action"
    print "attempting to comment"
    c.reply("It worked!")


import praw
import OAuth2Util
import time 

r = praw.Reddit('basic call response bot example by SkylineBilly')
o = OAuth2Util.OAuth2Util(r, print_log=True)
o.refresh(force=True)

targetSubreddit = 'billysTestReddit'

for c in praw.helpers.comment_stream(r, targetSubreddit):
    if check_condition(c):
        # set 'respond=True' to activate bot responses. Must be logged in.
        print "deploying bot action"
        bot_action(c, respond=True)
	#time.sleep(10)
	return

print "found one, all done"
