# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 18:35:47 2016

@author: Rachel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

santander = pd.read_csv('train.csv', index_col='\'ID')
santander['var3'].value_counts() # wtf is var3?
santander.hist(column='var15') # this is age distribution
santander.hist(column='imp_ent_var16_ult1', range=(1,90000)) # there are a lot of $0.00's