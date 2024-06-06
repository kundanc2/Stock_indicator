from textblob import TextBlob

class SentimentAnalyzer:
    def get_sentiment(self, text):
        blob = TextBlob(text)
        return blob.sentiment.polarity
