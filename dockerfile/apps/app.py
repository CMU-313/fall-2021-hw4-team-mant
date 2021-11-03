import re
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!"

def encode_data(df):
    df['address'] = np.where(df['address']=='U', 1, 0)
    df['Pstatus'] = np.where(df['Pstatus']=='T', 1, 0)
    df['activities'] = np.where(df['activities']=='yes', 1, 0)
    df['higher'] = np.where(df['higher']=='yes', 1, 0)
    df['internet'] = np.where(df['internet']=='yes', 1, 0)
    return df

@app.route('/predict')
def predict():
	#use entries from the query string here but could also use json
    # 'address', 'Pstatus', 'Medu', 'Fedu', 'studytime', 'activities', 'higher', 'internet', 'failures', 'absences'
    # "U";"T";4;3;4;"yes";"yes";"yes";0;4;
    data = request.args
    df = pd.DataFrame({
        'Fedu': pd.Series(data.get('Fedu')), 
        'Medu': pd.Series(data.get('Medu')), 
        'Pstatus': pd.Series(data.get('Pstatus')),
        'absences': pd.Series(data.get('absences')),
        'activities': pd.Series(data.get('activities')),
        'address': pd.Series(data.get('address')),
        'failures': pd.Series(data.get('failures')), 
        'higher': pd.Series(data.get('higher')),
        'internet': pd.Series(data.get('internet')),
        'studytime': pd.Series(data.get('studytime'))
    })
    
    # Transform data
    df = encode_data(df)

    # Predict
    prediction = clf.predict(df)
    return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/model.pkl')
    app.run(host="0.0.0.0", debug=True)