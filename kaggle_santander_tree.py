# -*- coding: utf-8 -*-
"""
Created on Sat May 14 13:21:02 2016

@author: Rachel
"""

# import all the things ---
import pandas as pd
import numpy as np
import seaborn as sns
sns.set(style="white", color_codes=True)
import matplotlib.pyplot as plt
#%matplotlib inline


# read in csv files ---
santrainder = pd.read_csv('train.csv')
santestder = pd.read_csv('test.csv')
print "santrainder shape: " + str(santrainder.shape)
print "santestder shape:  " + str(santestder.shape)
print santrainder.TARGET.value_counts()
print santrainder.columns

santrainder_en = pd.read_csv('train_english.csv')
print santrainder_en.columns


# create describe df & csv ---
sandescriber = santrainder.describe().transpose()
sandescriber.to_csv(path_or_buf="train_describe.csv")


# remove zero-variance columns ---
all_zero_feats = []

# look for matching mins and maxes
for index, row in sandescriber.iterrows():
   if sandescriber.loc[index,'min'] == sandescriber.loc[index,'max']:
    all_zero_feats.append(index)

print sandescriber.loc[all_zero_feats,:]
santrainder.drop(all_zero_feats, axis=1, inplace=True)
print "santrainder shape: " + str(santrainder.shape)


# remove duplicate columns ---
def duplicate_columns(frame):
    groups = frame.columns.to_series().groupby(frame.dtypes).groups
    dups = []
    for t, v in groups.items():
        dcols = frame[v].to_dict(orient="list")

        vs = dcols.values()
        ks = dcols.keys()
        lvs = len(vs)

        for i in range(lvs):
            for j in range(i+1,lvs):
                if vs[i] == vs[j]: 
                    dups.append(ks[i])
                    break

    return dups

dups = duplicate_columns(santrainder)
print dups
santrainder = santrainder.drop(dups, axis=1)
print "santrainder shape: " + str(santrainder.shape)


# create feature: number of zeroes ---
santrainder['zeroes'] = np.sum(santrainder.loc[:, 'imp_ent_var16_ult1':'var38']==0, axis=1) # count the number of bools, value == 0 is True
print santrainder['zeroes'].head()

# remove errors ---
# var3 error -999999, 117 of them
# 117/77060 = 0.0015 (not even 1% of the entries)
# drop as null or replace with mode (category 2)?
santrainder = santrainder.replace(-999999, np.NaN)
santrainder = santrainder.dropna(axis=0) # use with NaNs
print "santrainder shape: " + str(santrainder.shape)

# decision tree classifier ---
feature_cols = list(santrainder.columns) 
feature_cols.remove('TARGET') # need to remove TARGET
X = santrainder[feature_cols]
y = santrainder.TARGET

from sklearn.tree import DecisionTreeClassifier
treeclf = DecisionTreeClassifier(random_state=1)
treeclf.fit(X, y)

dtreeclass_importance = pd.DataFrame({'feature':feature_cols, 'importance':treeclf.feature_importances_})