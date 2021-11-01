import re
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!"

@app.route('/predict')
def predict():
	#use entries from the query string here but could also use json
    # 'address', 'Pstatus', 'Medu', 'Fedu', 'studytime', 'activities', 'higher', 'internet', 'failures', 'absences'
    # "U";"T";4;3;4;"yes";"yes";"yes";0;4;
    data = request.args
    df = pd.DataFrame({
        'address': pd.Series(data.get('address')),
        'Pstatus': pd.Series(data.get('Pstatus')),
        'Medu': pd.Series(data.get('Medu')), 
        'Fedu': pd.Series(data.get('Fedu')), 
        'studytime': pd.Series(data.get('studytime')), 
        'activities': pd.Series(data.get('activities')),
        'higher': pd.Series(data.get('higher')),
        'internet': pd.Series(data.get('internet')),
        'failures': pd.Series(data.get('failures')), 
        'absences': pd.Series(data.get('absences'))
    })
    
    # Transform data
    df['address'] = np.where(df['address']=='U', 1, 0)
    df['Pstatus'] = np.where(df['Pstatus']=='A', 1, 0)
    df['activities'] = np.where(df['activities']=='yes', 1, 0)
    df['higher'] = np.where(df['higher']=='yes', 1, 0)
    df['internet'] = np.where(df['internet']=='yes', 1, 0)

    # Predict
    prediction = clf.predict(df)
    return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/model.pkl')
    app.run(host="0.0.0.0", debug=True)