
#import praw
 


#r = praw.Reddit(user_agent="USER AGENT")
#r.login('SkylineBilly', 'roooo00oo')

targetSubreddit = 'billysTestReddit'

#import re

def check_condition(c):
    text = c.body
    tokens = text.split()
    if "1)" in tokens and "2)" in tokens:
        return True

def bot_action(c, verbose=True, respond=False):
    fixed = re.sub(r'(\n?)([0-9]+)(\))', r'\n\n\2.', c.body)

    if verbose:
        print c.body.encode("UTF-8")
        print "\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"
        print fixed.encode("UTF-8")

    if respond:
        head = "Hi! Let me try to beautify the list in  your comment:\n\n"
        tail = "\n\nI am a bot. You can provide feedback in my subreddit: /r/ListFormatFixer"
        c.reply(head + fixed + tail)

if __name__ is '__main__':
    import praw
    r = praw.Reddit(UA)

    # Provide a descriptive user-agent string. Explain what your bot does, reference
    # yourself as the author, and offer some preferred contact method. A reddit
    # username is sufficient, but nothing wrong with adding an email in here.
    UA = 'ListFormatFixer praw demo, Created by /u/shaggorama'

    # If you want the bot to be able to respond to people, you will need to login.
    # It is strongly recommended you login with oAuth
    # http://praw.readthedocs.org/en/stable/pages/oauth.html

    # NB: This login method is being deprecated soon
    r.login()

    for c in praw.helpers.comment_stream(r, targetSubreddit):
        if check_condition(c):
            # set 'respond=True' to activate bot responses. Must be logged in.
            bot_action(c, respond=False)
