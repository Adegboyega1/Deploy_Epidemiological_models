# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 08:08:50 2023

@author: ADEBAYO
"""
from fastapi.middleware.cors import CORSMiddleware

from data_enforcer import measles_data
from customObject import  MyCustomLayer

from customObject import Pitchfork_bifurcation
import uvicorn
from fastapi import FastAPI
#import pickle
import numpy as np
import pandas as pd
import tensorflow as tf
import math


tf.keras.utils.get_custom_objects().update({'MyCustomLayer':MyCustomLayer,'Pitchfork_bifurcation':Pitchfork_bifurcation})
app = FastAPI()
#load_pickle = open('C://Users//ADEBAYO//Desktop//Thesis//Epidemiological modeling//PitchFork_Bifurcated_2.0_measles_predictor.pkl','rb')
measles_timeseries_model = tf.keras.models.load_model('Pitchforkbifurcatedre2.0model')

testing_inpt = []

mn=287.04433962264153 
sd=353.3286976677941

#fore_cast = [60.43402099609375, 76.89613342285156, 89.54936218261719, 99.698486328125, 109.29554748535156, 120.10598754882812, 132.75567626953125, 146.4634246826172, 159.2341766357422, 171.00144958496094, 182.442138671875, 193.73880004882812, 204.9497528076172, 215.9573974609375, 226.57745361328125, 236.70115661621094, 246.33050537109375, 255.42677307128906, 263.9043884277344, 271.68414306640625, 278.69732666015625]
fore_cast=[]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/')
# model function goes here
def index():
    return 'Hello world'


@app.post('/Measles_forecaster')
# model function goes here
def bifurcated_lstm(data:measles_data):
    global fore_cast
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
    #otuput_data = testing_inpt.append(predict_data.tolist()[9:]) 
    predict_data = predict_data.tolist()
    fore_cast  = testing_inpt + predict_data[9:]
    fore_cast = [math.ceil(number) for number in fore_cast]
    return fore_cast


@app.get('/Measles_forecast')
# model function goes here
def bifurcated_lstm():
        return fore_cast

if __name__ == '__predictor_api__' :
    uvicorn.run(app, host='127.0.0.1',port=8000)


#uvicorn predictor_api:app --reload
