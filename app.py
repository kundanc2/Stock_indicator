import streamlit as st
from data_fetcher import DataFetcher
from text_processor import TextProcessor
from sentiment_analyzer import SentimentAnalyzer
from predictor import Predictor

def main():
    st.title('Stock News Sentiment Analysis and Prediction')

    # Initialize classes
    data_fetcher = DataFetcher(api_key='YOUR_NEWS_API_KEY')
    text_processor = TextProcessor()
    sentiment_analyzer = SentimentAnalyzer()
    predictor = Predictor(data_path='historical_stock_data.csv')

    # User input
    stock_ticker = st.text_input('Enter Stock Ticker:')

    if st.button('Predict'):
        # Fetch news
        news_data = data_fetcher.get_news(stock_ticker)
        
        # Preprocess news articles
        preprocessed_news = [text_processor.preprocess_text(article['content']) for article in news_data['articles']]
        
        # Perform sentiment analysis
        sentiments = [sentiment_analyzer.get_sentiment(article) for article in preprocessed_news]
        
        # Predict stock movement
        predictions = predictor.predict_stock_movement(sentiments)
        
        # Display results
        st.write(f'Predictions: {predictions}')

if __name__ == '__main__':
    main()
