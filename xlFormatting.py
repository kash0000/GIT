import pandas as pd

# Load the Excel file
df = pd.read_excel('data.xlsx', engine='openpyxl')

# Iterate through the rows and create the formatted strings
formatted_strings = []
for index, row in df.iterrows():
    amount = row['Amount']
    pl = row['PL']
    pe_balance = row['pe_balance']
    formatted_string = f'#Amount#: {amount} #PL#: {pl} #pe_balance#:{pe_balance}'
    formatted_strings.append(formatted_string)

# Join the formatted strings with line breaks
result = '\n'.join(formatted_strings)

# Print or save the result as needed
print(result)
