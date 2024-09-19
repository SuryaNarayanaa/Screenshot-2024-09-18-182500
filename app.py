from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Read the CSV file
    df = pd.read_csv('transactions.csv')
    
    # Convert the DataFrame to a list of dictionaries
    transactions = df.to_dict(orient='records')
    
    return render_template('index.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)
