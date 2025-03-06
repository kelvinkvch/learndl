import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import datasets as d
from sklearn.model_selection import  train_test_split
from sklearn.metrics import accuracy_score,mean_squared_error
from sklearn import preprocessing

x,y=d.load_iris(return_X_y=True)
print(x.shape)
print(y.shape)


xtrain,xtest,ytrain,ytest=train_test_split(x,y,random_state=42)
## just test modify
