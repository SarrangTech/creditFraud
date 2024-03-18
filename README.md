# FindDefault
## Prediction of Credit Card Fraud
### Overview:
Credit card fraud is a significant concern for financial institutions and consumers alike. The FindDefault project aims to develop a machine learning model to predict fraudulent credit card transactions. By identifying fraudulent activities, the model can help prevent financial losses for both credit card companies and cardholders.

### Dataset:
The dataset used in this project contains transactions made by credit cards in September 2013 by European cardholders. It includes a total of 284,807 transactions, out of which 492 are labeled as fraudulent. The dataset is highly imbalanced, with fraudulent transactions accounting for only 0.172% of all transactions.

### Project Goals:
1. Explore and analyze the dataset to identify patterns and relationships.
2. Preprocess the data by handling missing values, outliers, and imbalanced classes.
3. Train machine learning models to predict fraudulent transactions.
4. Evaluate the performance of the models using appropriate metrics.
5. Deploy the trained model for real-time fraud detection.

### Technologies Used:
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- Imblearn
- Streamlit
- Altair

### Installation:
1. Clone the repository:
```
git clone https://github.com/SarrangTech/FindDefault.git
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```


### Usage:
1. Navigate to the project directory:
```
cd FindDefault
```

2. Run the Streamlit app:
```
streamlit run init.py
```

3. Upload a CSV file containing credit card transaction data to the Streamlit prototype app and view the predictions. → `finddefault\input_test_UI.csv`

### Project Structure:	
The repository contains the following files:
- `__init__.py`: The main Streamlit application file.
- `voting_clf.joblib`: Main model used to perform prediction in application. It is an ensemble of all the models trained.
- `notebooks`: Directory containing Jupyter Notebook files or Python scripts used for training the machine learning models. This can include files with hyperparameter tuning, cross-validation, and model evaluation.
- `models`: Directory containing all saved model files, such as joblib files, pickle files, or any other serialized model objects. This directory would include the `voting_clf.joblib` file mentioned earlier.
- `requirements.txt`: File listing all the required Python packages and their versions.
- `README.md`: This file, providing an overview of the project and instructions for running the application.

### Future Work:
1. Collect a more extensive dataset spanning a longer period to capture a broader range of fraudulent activities.
2. Explore advanced techniques for handling imbalanced data, such as ensemble methods and anomaly detection algorithms.
3. Implement real-time data streaming and feature engineering techniques to enhance fraud detection capabilities.
4. Continuously monitor and update the deployed model to adapt to evolving fraud patterns.

### Contributors:
SarrangTech bathalapalli9920@gmail.com

