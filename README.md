# Housing Price Prediction

## Project Overview
The **Housing Price Prediction** project, created by **Aliza Hashmat**, aims to develop a robust machine learning model that predicts housing prices based on various features, such as location, size, number of bedrooms, and more. This project leverages advanced data preprocessing, exploratory data analysis (EDA), and machine learning techniques to create a predictive model. The model is deployed as a RESTful API using **Flask**, enabling users to make real-time predictions based on input features.

## Features
- **Data Collection:** Utilizing reliable sources like Kaggle to gather comprehensive housing data.
- **Data Cleaning & Preprocessing:** Cleaning the dataset and transforming features to enhance model performance.
- **Exploratory Data Analysis (EDA):** Analyzing the dataset to uncover patterns and relationships between features.
- **Machine Learning Model Training:** Implementing algorithms, such as Random Forest Regression, for accurate housing price predictions.
- **API Deployment:** Creating a RESTful API using Flask for seamless integration and real-time predictions.

## Technologies Used
- **Programming Language:** Python
- **Libraries:**
  - Pandas
  - NumPy
  - Scikit-learn
  - Flask
  - Matplotlib
  - Seaborn
- **Development Environment:** Any local Python environment (recommended: Anaconda or virtualenv)

## Dataset
The dataset used for this project is sourced from the Kaggle Housing Prices dataset. This dataset contains various features relevant to housing prices, providing a rich foundation for analysis and modeling.

## Setup Instructions
To set up the project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/AlizaHashmat-eng/housing-price-prediction.git
   cd housing-price-prediction
   ```

2. **Install Dependencies:** It is recommended to create a virtual environment before installing the required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Download the Dataset:** Download the dataset from Kaggle and place it in the project directory. Ensure the filename matches the one used in the code (e.g., `housing_prices.csv`).

4. **Run the Application:** Start the Flask API by running:
   ```bash
   python app.py
   ```
   The API will be accessible at `http://127.0.0.1:5000`.

## Usage Guidelines
Once the API is running, you can make predictions by sending a POST request to the `/predict` endpoint. Here’s how to do it using **curl** or a tool like **Postman**:

### Example Request
Using curl:
```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"features": [2000, 3, 2, 1]}'
```

### Example Response
```json
{
  "prediction": [250000]
}
```

### Input Format
The features represent the following:
- **Square Footage** (e.g., 2000)
- **Number of Bedrooms** (e.g., 3)
- **Number of Bathrooms** (e.g., 2)
- **Garage Size** (e.g., 1 for one-car garage)

Make sure the order of the features matches the model's training data.

## Contributing
Contributions are welcome! If you would like to contribute to this project, please fork the repository and create a pull request with your changes. Ensure to follow the coding standards and add relevant tests for new features.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- **Kaggle** for providing the dataset.
- **Flask** for the web framework that allows us to deploy our model as an API.
- **Scikit-learn** for the powerful machine learning algorithms utilized in this project.

## Author
**Aliza Hashmat**  
[GitHub Profile](https://github.com/AlizaHashmat-eng)
