# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 10:38:39 2023

@author: ADEBAYO
"""

from tensorflow.keras.layers import Layer

import tensorflow as tf

def Pitchfork_bifurcation(x):
    return tf.math.pow(x,3) - 2.0*x
class MyCustomLayer(Layer):

    
    def __init__(self, units,activation, dropout, **kwargs):
        super(MyCustomLayer, self).__init__(**kwargs)
        self.units = units
        self.activation = Pitchfork_bifurcation
        self.dropout = dropout

    def build(self, input_shape):
        self.lstm = tf.keras.layers.LSTM(self.units, self.activation, self.dropout)
        super(MyCustomLayer, self).build(input_shape)

    def call(self, inputs):
        output = self.lstm(inputs)
        return output

    def get_config(self):
        config = super(MyCustomLayer, self).get_config()
        config.update({'units': self.units, 'activation': self.activation,
                       'dropout':self.dropout})
        return config

    @classmethod
    def from_config(cls, config):
        return cls(**config)
