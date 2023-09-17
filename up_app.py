from flask import Flask, render_template
import pandas as pd
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Read data from the pipe-separated text file
    data = pd.read_csv('data/data.txt', delimiter='|')

    # Calculate SLA_Breached based on mail_send_date
    current_date = datetime.now().strftime('%Y%m%d')
    data['SLA_Breached'] = data['mail_send_date'].apply(lambda date: 'Yes' if date == current_date else 'No')

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
