import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the data
data = pd.read_csv('customer_churn_data.csv')

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data[['customer_id', 'age', 'gender', 'tenure', 'monthly_spend']], data['churned'], test_size=0.25, random_state=42)

# Train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict_proba(X_test)

# Recommend mitigation strategies for customers who are likely to churn
def recommend_mitigation_strategies(customer_id, churn_probability):
    if churn_probability > 0.5:
        mitigation_strategies = ['offer a discount', 'send a personalized email campaign', 'call the customer to discuss their needs']
    else:
        mitigation_strategies = []

    return mitigation_strategies

# Get the churn probability for each customer in the test set
churn_probabilities = y_pred[:, 1]

# Recommend mitigation strategies for each customer in the test set
customer_id_to_mitigation_strategies = {}
for i in range(len(X_test)):
    customer_id = X_test.iloc[i, 0]
    churn_probability = churn_probabilities[i]
    mitigation_strategies = recommend_mitigation_strategies(customer_id, churn_probability)

    customer_id_to_mitigation_strategies[customer_id] = mitigation_strategies

# Print the recommended mitigation strategies for each customer in the test set
for customer_id, mitigation_strategies in customer_id_to_mitigation_strategies.items():
    print('Customer ID:', customer_id)
    print('Mitigation strategies:', mitigation_strategies)
