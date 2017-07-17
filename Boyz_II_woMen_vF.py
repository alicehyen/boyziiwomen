# defining the method for how we will translate Josh texts to Liz texts
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text
 
# the pseudo text Josh sends which will ultimately be translated into comprehendable Liz text
JOSH_TEXT = "hey. what are you doing tonight? i'm gonna grab drinks later with some friends if you wanna join."

# our Josh to Liz translation dictionary with our key:characters to put a max on the excitement
if JOSH_TEXT.count('!!') <= 1:
	JOSH_TEXT
else:
	COUNT = JOSH_TEXT.count('!!')-1
	JOSH_TEXT = JOSH_TEXT.replace('!!','',COUNT)

# our Josh to Liz translation dictionary with our key:values.
REPS_WORDS = {'hey':'why hello you beautiful independent woman',
'what are you doing tonight':'just thinking about you and wondering what you are up to',
'if you wanna join':'if you are up for hanging out because i think you are amazinggg [winky face][red heart emoji]',
'okay':'amazingggg', 'good':'incredibleeee', 'like':'red heart emoji', 'thanks':'thank you soooo much', 'babe':'mah lady','my boyfriend':'my meant-to-be soulmate','my girlfriend':'my meant-to-be soulmate',
'haha':'lolll','yeah':'yesss','baby':'my wonderful significant other', '.':'!', '!':'!!!!!', '?':'??'}

LIZ_TEXT = replace_all(JOSH_TEXT, REPS_WORDS)

print LIZ_TEXT