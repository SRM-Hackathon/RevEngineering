from textblob import TextBlob 

def GetMood(s):
	analysis = TextBlob(s)
	return float(analysis.sentiment[0])

