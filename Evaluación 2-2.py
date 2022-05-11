import xlrd
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt

data=pd.read_excel('Data_Ev2.xlsx')
datos=pd.DataFrame()
YearIn=data['YearlyIncome']
TotChi=data['TotalChildren']

datos['YearlyIncome']=YearIn
datos['TotalChildren']=TotChi

xy=np.array(datos)
z=data['NumberCarsOwned'].values
regLM=linear_model.LinearRegression()
regLM.fit(xy,z)
z_pred=regLM.predict(xy)
print('Coeficiente R:'  ,regLM.coef_)
print('Error cuadrado medio %.2f ' % mean_squared_error(z,z_pred))
print('Puntaje de varianza: %.2f' % r2_score(z,z_pred))

PredCarro = int(regLM.predict([[80000,2]])) # YearlyIncome= 80000, TotalChildren=2
print('Predicción de # de carro(s): ', PredCarro)

