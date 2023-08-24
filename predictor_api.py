# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 08:08:50 2023

@author: ADEBAYO
"""


from data_enforcer import measles_data
from customObject import  MyCustomLayer

from customObject import Pitchfork_bifurcation
import uvicorn
from fastapi import FastAPI
#import pickle
import numpy as np
import pandas as pd
import tensorflow as tf

tf.keras.utils.get_custom_objects().update({'MyCustomLayer':MyCustomLayer,'Pitchfork_bifurcation':Pitchfork_bifurcation})
app = FastAPI()
#load_pickle = open('C://Users//ADEBAYO//Desktop//Thesis//Epidemiological modeling//PitchFork_Bifurcated_2.0_measles_predictor.pkl','rb')
measles_timeseries_model = tf.keras.models.load_model('C:\\Users\\ADEBAYO\\Desktop\\Thesis\\Epidemiological modeling\\Pitchfork_bifurcated_2.0_measles model')

testing_inpt = []

mn=287.04433962264153 
sd=353.3286976677941

@app.get('/')
# model function goes here
def index():
    return 'Hello world'


@app.post('/Measles_forecaster')
# model function goes here
def bifurcated_lstm(data:measles_data):
    # Extract Predicted Vaalue for gradient Base LSTM for Longterm visuals
    data = data.dict()
    week1 = data['week_1']
    testing_inpt.append(week1)
    week2 = data['week_2']
    testing_inpt.append(week2)
    week3 = data['week_3']
    testing_inpt.append(week3)
    week4 = data['week_4']
    testing_inpt.append(week4)
    week5 = data['week_5']
    testing_inpt.append(week5)
    week6 = data['week_6']
    testing_inpt.append(week6)
    week7 = data['week_7']
    testing_inpt.append(week7)
    week8 = data['week_8']
    testing_inpt.append(week8)
    
    x_input = np.array(testing_inpt)
    x_input = (x_input-mn)/sd
    
    
    temp_input = list(x_input.ravel())
    lst_output = []
    i = 0
    while i < 21:
        if len(temp_input) > 8:
            print(temp_input[1:])
            x_input = np.array(temp_input[1:])
            x_input=  x_input.reshape((1,x_input.shape[0],1))
            yhat = measles_timeseries_model.predict(x_input, verbose=1)
            
            temp_input.append(yhat[0][0])
            temp_input=temp_input[1:]
            lst_output.append(yhat[0][0])
            i += 1
        else:
            x_input= x_input.reshape((1,x_input.shape[0],1))
            yhat = measles_timeseries_model.predict(x_input, verbose=0)
            temp_input.append(yhat[0][0])
            lst_output.append(yhat[0][0])
            i += 1
    
    
    predict_data = np.array(lst_output) * sd + mn 
   
    return predict_data.tolist()


if __name__ == '__predictor_api__' :
    uvicorn.run(app, host='127.0.0.1',port=8000)


#uvicorn predictor_api:app --reload
