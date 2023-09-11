import matplotlib.pyplot as plt
import numpy as np



def gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion): #Se crea una función para graficar la predicción
    
    
    plt.figure(figsize=(15, 6)) # Se estable el tamaño de la grafica
    plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) # Se grafican los datos teoricos de Esfuerzo y Deformación 
    plt.scatter(	dataRealEsfuerzo, dataRealDeformacion, color='red') #Los datos realesm de graficaran en rojo
    plt.xlabel('Esfuerzo [kN]') #Se coloca etiqueta al eje x de Esfuerzo (KN)
    plt.ylabel('Deformación [mm]') #Se coloca etiquetta al eje y de Deformación [mm]
    plt.title('Gráfica 2: teórico versus real [ZOOM]') #Se le coloca titulo al grafico
    plt.xlim(0, x_lim) #Se establecen los limites del eje x
    plt.ylim(0, y_lim) #Se establecen los limites del eje y
    plt.grid() # SE activa la grilla para la graf´ca 
    plt.gca().invert_yaxis() # Se invierte el eje y para que la deformación aumente hacia arriba
    plt.show() # Se imprime el resultado 
 
def gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model):  #Se crea una función para graficar la predicciónde 3000 KN
  plt.figure(figsize=(15, 6)) # Se estable el tamaño de la grafica
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) # Se grafican los datos teoricos de Esfuerzo y Deformación 
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red')  #Los datos reales de graficaran en rojo
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m') # Se grafica la predicción del modelo para valores de esfuerzo de 0 a 1000 kN en color magenta 
  plt.scatter(	3000 , prediction, color='green') # Se grafica la predicción en verde
  plt.xlabel('Esfuerzo [kN]') #Se coloca etiqueta al eje x de Esfuerzo (KN)
  plt.ylabel('Deformación [mm]')   #Se coloca etiquetta al eje y de Deformación [mm]
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN') #Se le coloca titulo al grafico
  plt.xlim(0, 3000) #Se establecen los limites del eje x
  plt.ylim(0, 45) #Se establecen los limites del eje y
  plt.grid() #Se activa la grilla para la grafica
  plt.gca().invert_yaxis() # Se invierte el eje y para que la deformación aumente hacia arriba
  plt.show() # Se imprime el resultado 

def gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion):  #Se crea una función para graficar sin  predicción
  plt.figure(figsize=(15, 6)) # Se estable el tamaño de la grafica
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) # Se grafican los datos teoricos de Esfuerzo y Deformación 
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') #Los datos reales de graficaran en rojo
  plt.xlabel('Esfuerzo [kN]') #Se coloca etiqueta al eje x de Esfuerzo (KN)
  plt.ylabel('Deformación [mm]')  #Se coloca etiquetta al eje y de Deformación [mm]
  plt.title('Gráfica 1: teórico versus real') #Se le coloca titulo al grafico
  plt.grid() #Se activa la grilla para la grafica
  plt.gca().invert_yaxis() # Se invierte el eje y para que la deformación aumente hacia arriba
  plt.show() # Se imprime el resultado 
