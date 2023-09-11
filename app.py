from data.data import * # Se importan las funciones de archivos de data
from BD.baseDatos import * # Se importan las funciones de archivos de base de datos
from sklearn.linear_model import LinearRegression # se instala pip install scikit-learn y se importa la libreria para regresión lineal
from grafica.grafica import * # Se importan las funciones ddel archivo graficas
import pandas as pd #Se instala pandas con pip install pandas y se importa

#Datos del excel
dataTeoricoEsfuerzo, dataTeoricoDeformacion = dataTeorico() # Se obtienen los datos teóricos del archivo data.py llamando la funcion dataTeorico()

#Datos de la base de datos y realizamos el modelo
data_list = lecturaDatos() # Se leen los datos de la base de datos
data_real = pd.DataFrame(data_list) #Se crea un data frame con el data_list creado
data_real_fit = data_real #Se crea una copia del data frame data_real
X = data_real_fit['Esfuerzo[kN]'].values.reshape(-1, 1) #Se asignan los datos de Esfuerzo[kN] en el eje x para le modelo de regresión líneal 
y = data_real_fit['Deformacion[mm]'].values.reshape(-1, 1) #Se asignan los datos de Deformacion[mm] en el eje y para le modelo de regresión líneal 
x_lim = data_real['Esfuerzo[kN]'].iloc[-1] #Se establecen los limites del eje x, se usa  iloc(-1) para indicar el último valor de la serie de datos
y_lim = data_real['Deformacion[mm]'].iloc[-1] #Se establecen los limites del eje y, se usa  iloc(-1) para indicar el último valor de la serie de datos
model = LinearRegression() # Se crea  e modello para realizar la regresión líneal
model.fit(X, y) #Se aplica la regresión liean a las variabels x e y antes creadas
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1) # Con la regresión lineal ibtenida se hace la presicción para una deformación de 3000 KN
print('la predicción a 1000 kN es de: ', prediction ,'mm') #Se imprime el resultado de la defomración hallada


dataRealEsfuerzo = data_real['Esfuerzo[kN]'] #Se exportan los datos de Esfuerzo de la base de datos real 
dataRealDeformacion = data_real['Deformacion[mm]'] #Se exportan los datos de Deformación de la base de datos real 

#realizamos la lectura de las gráficas
gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion) # Se realiza la grafíca isin predicción 
gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion) # Se realiza la grafica con los limtes de x e y establecidos 
gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model) #Se realiza la grafica con la predicción de 3000KN hallada

