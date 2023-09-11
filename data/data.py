import pandas as pd

# Importar datos del csv
data_teorico = pd.read_csv(r"C:\Users\USUARIO\Downloads\actividad_4-main\data\Data ingeniero.csv") # Importamos datos desde el archivo CSV y se crea un DataFrame

#Código general
""" En caso que se exigiera realizar la limpieza de la data se haría aca"""

def dataTeorico(): # Se define la función llamada 'dataTeorico()' que extrae datos específicos del DataFrame 'data_teorico'
    dataTeoricoEsfuerzo = data_teorico['Esfuerzo[kN]'] # Se extrae la columna 'Esfuerzo[kN]'
    dataTeoricoDeformacion = data_teorico['Deformacion[mm]']# Se extrae la columna Deformacion[mm]
    return dataTeoricoEsfuerzo, dataTeoricoDeformacion # Se devuelven los datos extraídos como una tupla o lista


