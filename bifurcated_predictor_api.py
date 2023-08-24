# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 08:08:50 2023

@author: ADEBAYO
"""
from measles_data 
import uvicorn
from fastapi import FastAPI
import pickle
app = FastAPI()
load_pickle = open('')

@app.get('/')
# model function goes here
@app.post('/')
# model function goes here
def bifurcated_lstm():
    # Extract Predicted Vaalue for gradient Base LSTM for Longterm visuals

    x_input = testing_inpt[0]
    temp_input = list(x_input.ravel())

    lst_output = []
    i = 0
    while i < 21:
        if len(temp_input) > 8:
            print(temp_input[1:])
            x_input = array(temp_input[1:])
            x_input= x_input = x_input.reshape((1,x_input.shape[0],n_features))
            yhat = measles_timeseries_model.predict(x_input, verbose=1)
            
            temp_input.append(yhat[0][0])
            temp_input=temp_input[1:]
            lst_output.append(yhat[0][0])
            i += 1
        else:
            x_input= x_input = x_input.reshape((1,x_input.shape[0],n_features))
            yhat = measles_timeseries_model.predict(x_input, verbose=0)
            temp_input.append(yhat[0][0])
            lst_output.append(yhat[0][0])
            i += 1
    
    test_data = np.array(testing_ouput[:21])
    Actual_data = test_data 
    predict_data = np.array(lst_output) 


if __name___ == '__Predictive Modeling of Measles Outbreak__' :
    uvicorn.run(app, host='',port=8000)


#uvicorn Predictive Modeling of Measles Outbreak:app --reload
