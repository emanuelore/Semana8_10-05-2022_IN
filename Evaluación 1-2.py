import xlrd
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt

data=pd.read_excel('Data_Ev2.xlsx')
datax=data[['YearlyIncome']]
x=np.array(datax)
y=data['NumberCarsOwned'].values
regL=linear_model.LinearRegression()
regL.fit(x,y)
y_pred=regL.predict(x)
print('Coeficiente R:',regL.coef_)
print('Error cuadrado medio %.2f '% mean_squared_error(y,y_pred))
print('Puntaje de varianza: %.2f '% r2_score(y,y_pred))
PredCarro = int(regL.predict([[50000]]))
print('Predicción del Número de Carros de acuerdo al sueldo de 50000: ',int(PredCarro))

#Si queremos la gráfica de todo el documento
data.drop(['CustomerKey'],1).hist()
plt.show()
