# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 08:46:50 2023

@author: ADEBAYO
"""

from pydantic import BaseModel

class measles_data(BaseModel):
    week_1: float
    week_2: float
    week_3: float
    week_4: float
    week_5: float
    week_6: float
    week_7: float
    week_8: float