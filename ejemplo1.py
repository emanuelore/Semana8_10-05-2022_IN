import xlrd
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error,r2_score
data=pd.read_excel('BI_Alumnos08.xlsx')
lista=pd.DataFrame()
alt=data['Altura']
ed=data['Edad']
lista['Altura']=alt
lista['Edad']=ed
xy=np.array(lista)
z=data['Peso'].values
regLM=linear_model.LinearRegression()
regLM.fit(xy,z)
z_pred=regLM.predict(xy)
print('Coeficiente R:' ,regLM.coef_)
print('Error cuadrado medio %.2f ' % mean_squared_error(z,z_pred))
print('Puntaje de varianza: %.2f' % r2_score(z,z_pred))
predPeso=regLM.predict([[180,22]])
print('Prediccion de Peso: ',int(predPeso))