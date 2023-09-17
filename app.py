from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    # Read data from the pipe-separated text file
    data = []
    with open('data/data.txt', 'r') as file:
        reader = csv.DictReader(file, delimiter='|')
        for row in reader:
            data.append(row)

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
