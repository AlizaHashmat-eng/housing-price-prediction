import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load your dataset
data = pd.read_csv('housing_prices.csv')

# Preprocess your data as needed (feature selection, cleaning, etc.)
# Assuming 'target' is the column you want to predict
X = data.drop('target', axis=1)
y = data['target']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train your model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'housing_price_model.pkl')
