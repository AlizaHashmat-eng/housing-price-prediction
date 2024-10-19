# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib  # For saving the model

# Step 1: Load the Dataset
# Replace 'housing_prices.csv' with the actual name of your dataset file
data = pd.read_csv('housing_prices.csv')

# Step 2: Preprocess the Data
# Assume the dataset has columns: 'area', 'bedrooms', 'bathrooms', 'location', 'garage', 'price'
# You may need to convert categorical variables into numerical format
data['garage'] = data['garage'].map({'yes': 1, 'no': 0})  # Convert Garage Yes/No to 1/0
data = pd.get_dummies(data, columns=['location'], drop_first=True)  # Convert categorical 'location' into dummy variables

# Step 3: Define Features and Target Variable
X = data.drop('price', axis=1)  # Features
y = data['price']  # Target variable

# Step 4: Split the Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 6: Make Predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate the Model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Step 8: Save the Model
joblib.dump(model, 'housing_price_model.pkl')
print("Model saved as 'housing_price_model.pkl'")
