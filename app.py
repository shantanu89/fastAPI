import pandas
import numpy
import matplotlib.pyplot as plt
from model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

fit=LogisticRegression()
