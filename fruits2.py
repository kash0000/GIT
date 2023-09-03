import pandas as pd

# Sample dataset
data = pd.read_csv('fruits_data.csv')

# Define a function to generate commentary
def generate_commentary(row):
    fruit = row['Fruit']
    market_before = row[['Market1_Before', 'Market2_Before']]
    market_after = row[['Market1_After', 'Market2_After']]
    
    # Calculate average prices before and after
    avg_before = market_before.mean()
    avg_after = market_after.mean()
    
    # Generate commentary based on price change
    if avg_after > avg_before:
        commentary = f"The price of {fruit} has increased from an average of {avg_before:.2f} to {avg_after:.2f}."
    elif avg_after < avg_before:
        commentary = f"The price of {fruit} has decreased from an average of {avg_before:.2f} to {avg_after:.2f}."
    else:
        commentary = f"The price of {fruit} has remained stable, staying at an average of {avg_before:.2f}."
    
    return commentary

# Apply the commentary generation function to each row
data['Commentary'] = data.apply(generate_commentary, axis=1)

# Display the dataset with commentary
print(data[['Fruit', 'Market1_Before', 'Market1_After', 'Market2_Before', 'Market2_After', 'Commentary']])
