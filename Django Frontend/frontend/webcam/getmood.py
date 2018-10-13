from textblob import TextBlob 

def GetMood(s):
	analysis = TextBlob(s)
	if float(analysis.sentiment[0]) > 0 :
		return 1
	else:
		return 0

