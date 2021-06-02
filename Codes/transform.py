import numpy as np
import os
import sys
import pandas as pd
import time
from monthly_extract import extract_one_month


#aver = pd.read_csv('../Data/Transformed/Year2001.csv')
#
#aver.info( memory_usage = 'deep')
##aver.info( verbose = True)
#
#print(aver.Año.value_counts())
#print(aver.Mes.value_counts())
#print(aver.Día.value_counts())
#
#exit()

start_time = time.time()

out_path = '../Data/Transformed/'
os.system('mkdir ' + out_path)

# Load info from polutant and estaciones
estaciones = pd.read_csv('Info/estaciones.csv')
polutants  = pd.read_csv('Info/polutants.csv', dtype = object)
#print(polutants)

# Create dictionary with polutant code as keys and Abbr as values 
polutant_code_list = polutants.Code.values
polutant_Abbr_list = polutants.Abbreviation.values
dict_polutants = dict(zip(polutant_code_list, polutant_Abbr_list))

stations_code_list_aux = estaciones.Code.values
stations_code_list = []
for string in stations_code_list_aux:
    aver = eval(string)
    for stat in aver:
        stations_code_list.append(stat)
#print(stations_code_list)


# Initialize DataFrame. The Structure will be:
# one row per station, year, month, day with a list with 24 entries for each polutant
column_names = ['Provincia', 'Municipio', 'Estación','Año', 'Mes', 'Día' ]
column_names = column_names + list(polutant_Abbr_list)

dataraw = '../Data/Raw/'
years = ['01', '02', '03', '04',
         '05', '06', '07', '08',
         '09', '10', '11', '12',
         '13', '14', '15', '16',
         '17']
years = ['02']
months= ['01', '02', '03', '04',
         '05', '06', '07', '08',
         '09', '10', '11', '12']
 
for year in years:
    data = pd.DataFrame(columns = column_names)
    data.loc[0,'Provincia'] = 'InitializeIndex'

    for month in months:
        if year == '17' and month == '10':
            print('Oct17!!')
            break

        f = open(dataraw + 'Year20' + year + '/' + month + '-20' + year + '.txt') 
        lines = f.readlines()
        data = extract_one_month(lines, data)

        print(month)

    data.to_csv(out_path + 'Year20' + year +'.csv', index = False)


end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))

exit()

f = open('../Data/Raw/Year2001/01-2001.txt', 'r')
lines = f.readlines()
print(sys.getsizeof(lines)/(1024*1024), 'Mb')

data = extract_one_month(lines,data)

       
#    counter += 1
#    if counter == 32:
#        break



print(data)
print(data.Estación.value_counts())
data.info()

data.to_csv('test.csv', index = False)

end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
exit()








data.Provincia = [provi,1]
data.Municipio = [munic,1]
data.Estación = [estac,1]
data.Año  = [year,1]
data.Mes = [month,1]
data.Día   = [day,1]

aver = data.loc[(data.Provincia == provi) & (data.Municipio == 1)]
print(aver)
data.loc[(data.Provincia == provi) & (data.Municipio == munic)].Año = 123123
data.loc[0,'Día'] = 'nosejoder'

data.loc[3,'Provincia'] = provi
data.loc[3,'Municipio'] = munic
data.loc[3,'Estación'] = estac
data.loc[3,'Año']  = year
data.loc[3,'Mes'] = month
data.loc[3,'Día']   = day

print(data)
print(data.index)
print(data.index[0])

print(max(data.index))


print(aver.index.any())
