# This file defines the polutants dataframe and the estaciones dataframe
#


import numpy as np
import os
import sys
import pandas as pd


#f = open('../Data/Year2001/01-2001.txt', 'r')
#aver = f.readlines()
#
#print(sys.getsizeof(aver)/(1024*1024), 'Mb')
#print(len(aver))
#
#column_names = ['Provincia', 'Municipio', 'Estación', 'Magnitud',
#                'Técnica'  , 'Periodo',   'Análisis', 'Año', 'Mes',
#                'Día', 'Dato', 'Código De Validación']
#
#data = pd.DataFrame(columns = column_names)
#
#data.Provincia = [28,12,12,12]
#data.Municipio = [[28,132],12,12,12]
#
#print(data)
#
#data.to_csv('test.csv')




# Define the dataframe with information about the polutants
polutant_code = ['01', '06', '07', '08', '09',
                 '10', '12', '14', '20', '30',
                 '35', '37', '38', '39', '42', '43']

polutant_name = ['Dióxido de Azufre', 'Monóxido de Carbono', 'Monóxido de Nitrógeno',
                  'Dióxido de Nitrógeno', 'Partículas < 2.5 μm', 'Partículas < 10 μm', 
                  'Óxidos de Nitrógeno', 'Ozono', 'Tolueno', 'Benceno', 'Etilbenceno', 
                  'Metaxileno', 'Paraxileno', 'Ortoxileno', 'Hidrocarburos totales (hexano)', 'Metano'] 

polutant_abbr = [ 'SO2' , 'CO',  'NO',  'NO2', 'PM2.5', 
                  'PM10', 'NOx', 'O3',  'TOL', 'BEN', 
                  'EBE' , 'MXY', 'PXY', 'OXY', 'TCH', 'CH4'] 

polutant_unit = ['μg/m3', 'mg/m3', 'μg/m3', 'μg/m3', 
                 'μg/m3', 'μg/m3', 'μg/m3', 'μg/m3',
                 'μg/m3', 'μg/m3', 'μg/m3', 'μg/m3',
                 'μg/m3', 'μg/m3', 'mg/m3', 'mg/m3'] 

meastech_code = ['38', '48', '08', '08', '47',
                 '47', '08', '06', '59', '59',
                 '59', '59', '59', '59', '02', '02']

meastech = ['Fluorescencia ultravioleta', 'Absorción infrarroja', 'Quimioluminiscencia', 
            'Quimioluminiscencia', 'Microbalanza', 'Microbalanza', 'Quimioluminiscencia',
            'Absorción ultravioleta', 'Cromatografía de gases', 'Cromatografía de gases',
            'Cromatografía de gases', 'Cromatografía de gases', 'Cromatografía de gases',
            'Cromatografía de gases', 'Ionización de llama', 'Ionización de llama'] 

polutant_columns = ['Code', 'Name', 'Abbreviation', 'Unit', 'Measurement Technique', 'MeasTech Code']
polutants = pd.DataFrame(columns = polutant_columns)

polutants.Code = polutant_code
polutants.Name = polutant_name
polutants.Abbreviation = polutant_abbr
polutants.Unit = polutant_unit
polutants['Measurement_Technique'] = meastech
polutants['MeasTech Code'] = meastech_code

polutants.to_csv('polutants.csv')
print(polutants)

# Polutant Dataframe defined



# Define a dataframe with information of the measurement stations
estaciones_codes = [['001'], ['002'], ['003', '035'], ['004'], 
                    ['005', '039'], ['006'], ['007'], ['008'], 
                    ['009'], ['010', '038'], ['011'], ['012'], 
                    ['013', '040'], ['014'], ['015'], ['016'], 
                    ['017'], ['018'], ['019'], ['020', '036'], 
                    ['021'], ['022'], ['023']] 

estaciones_name = ['Pº. Recoletos', 'Glta. de Carlos V', 'Pza. del Carmen', 
                   'Pza. de España', 'Barrio del Pilar', 'Pza. Dr. Marañón',
                   'Pza. M. de Salamanca', 'Escuelas Aguirre', 'Pza. Luca de Tena',
                   'Cuatro Caminos', 'Av. Ramón y Cajal', 'Pza. Manuel Becerra',
                   'Vallecas', 'Pza. Fdez. Ladreda', 'Pza. Castilla', 'Arturo Soria', 
                   'Villaverde Alto', 'C/ Farolillo', 'Huerta Castañeda', 'Moratalaz',
                   'Pza. Cristo Rey', 'Pº. Pontones', 'Final C/ Alcalá']

which_decomission = [0,1,5,6,8,11,13,14,18,20,21,22]
when_decomission  =  ['04/05/2009 (14:00 h.)', '04/12/2006 (11:00 h.)',
                      '27/11/2009 (08:00 h.)', '30/12/2009 (14:00 h.)',
                      '07/12/2009 (08:00 h.)', '30/12/2009 (14:00 h.)',
                      '02/12/2009 (09:00 h.)', '17/10/2008 (11:00 h.)',
                      '30/12/2009 (13:00 h.)', '04/12/2009 (14:00 h.)',
                      '20/11/2009 (10:00 h.)', '30/12/2009 (14:00 h.)'] 


estaciones_columns = ['Code', 'Name', 'Decomission Date']
estaciones = pd.DataFrame(columns = estaciones_columns)

estaciones.Code = estaciones_codes
estaciones.Name = estaciones_name
estaciones['Decomission Date'].iloc[which_decomission] = when_decomission

estaciones.to_csv('estaciones.csv')
print(estaciones)
# Estaciones dataframe defined







