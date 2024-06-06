import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class Predictor:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)

    def predict_stock_movement(self, sentiments):
        # Add sentiment scores to your dataset
        if len(sentiments) > len(self.data):
            sentiments = sentiments[:len(self.data)]
        else:
            self.data = self.data.iloc[:len(sentiments)]
        self.data['sentiment'] = sentiments

        # Feature selection
        features = self.data[['open', 'high', 'low', 'close', 'volume', 'sentiment']]
        target = self.data['direction']  # 'direction' should be a column indicating if the stock went up or down

        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

        # Train the model
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        # Predict
        predictions = model.predict(X_test)
        return predictions
