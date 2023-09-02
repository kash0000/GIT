import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Sample dataset
data = pd.read_csv('fruits_data.csv')

# Define a function to generate commentary
def generate_commentary(row):
    fruit = row['Fruit']
    market_before = row[['Market1_Before', 'Market2_Before']]
    market_after = row[['Market1_After', 'Market2_After']]
    
    # Perform linear regression to analyze price change
    reg = LinearRegression().fit(market_before.values.reshape(-1, 1), market_after.values.reshape(-1, 1))
    slope = reg.coef_[0][0]
    
    # Sentiment analysis of price change
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(f"Price of {fruit} increased by {slope:.2f}.")
    
    # Generate commentary based on price change sentiment
    if sentiment_score['compound'] >= 0.05:
        commentary = f"The price of {fruit} has slightly increased from an average of {np.mean(market_before):.2f} to {np.mean(market_after):.2f}."
    elif sentiment_score['compound'] <= -0.05:
        commentary = f"The price of {fruit} has slightly decreased from an average of {np.mean(market_before):.2f} to {np.mean(market_after):.2f}."
    else:
        commentary = f"The price of {fruit} has remained relatively stable, changing from {np.mean(market_before):.2f} to {np.mean(market_after):.2f}."
    
    return commentary

# Apply the commentary generation function to each row
data['Commentary'] = data.apply(generate_commentary, axis=1)

# Display the dataset with commentary
print(data[['Fruit', 'Market1_Before', 'Market1_After', 'Market2_Before', 'Market2_After', 'Commentary']])

output_file_path = 'output_file.txt'

# Open the output file for writing
with open(output_file_path, 'w') as file:
    # Iterate through the 'Commentary' column and write each commentary to the file
    for commentary in data['Commentary']:
        file.write(commentary + '\n')

# Print a message to confirm that the data has been saved
print("Commentary data has been saved to '{}'.".format(output_file_path))
