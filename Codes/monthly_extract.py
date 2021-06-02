import pandas as pd
import numpy as np


# Load info from polutant and estaciones
estaciones = pd.read_csv('Info/estaciones.csv')
polutants  = pd.read_csv('Info/polutants.csv', dtype = object)

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


def extract_one_month(lines,data):

    df_index_counter = max(data.index)
    # Loop through lines in data file
    for line in lines:
        # extract info
        provi = line[0:2]
        munic = line[2:5]
        estac = line[5:8]
        polut = line[8:10]
        techn = line[10:12]
        perio = line[12:14]
        year  = line[14:16]
        month = line[16:18]
        day   = line[18:20]

        # Skip the lines with a polutant or a station that is not 
        # in the pdf with the info
        if polut not in polutant_code_list:
    #        print(polut)
            continue
        if estac not in stations_code_list:
    #        print(estac)
            continue


        # Extract hourly data
        # Data without the validation code V is not extracted
        li = []
        i = 20
        indV = -42
        indN = -42
        indM = -42
        indC = -42
        while i < len(line):
    #        print(line[i:len(line)])
            if indN == 1e6:
                pass
            else:
                indN = line[i:len(line)].find('N')
                if indN == -1:
                    indN = 1e6

            if indM == 1e6:
                pass
            else:
                indM = line[i:len(line)].find('M')
                if indM == -1:
                    indM = 1e6

            if indC == 1e6:
                pass
            else:
                indC = line[i:len(line)].find('C')
                if indC == -1:
                    indC = 1e6

            if indV == 1e6:
                pass
            else:
                indV = line[i:len(line)].find('V')

    #        print('indN = ' + str(indN))
    #        print('indV = ' + str(indV))
            if indV == -1:
                indV = 1e6
            # if data is not validated add '' to list
            if   indN < indV or indM < indV or indC < indV:
                li.append('')
                i += min(indN, indM, indC) + 1
            # if data is validated add the number to the list
            elif indN > indV or indM > indV or indC > indV:
                li.append(float(line[i:i+indV]))
                i += indV + 1
            else:
                i = len(line)

        check = data.loc[(data.Provincia == provi) &
                         (data.Municipio == munic) &
                         (data.Estación  == estac) &
                         (data.Año       == year)  &
                         (data.Mes       == month) &
                         (data.Día       == day)].index

        # Check if the row of the day exists
        if len(check) == 0:
            # if it does not exist, create it
            data.loc[df_index_counter,'Provincia'] = provi
            data.loc[df_index_counter,'Municipio'] = munic
            data.loc[df_index_counter,'Estación' ] = estac
            data.loc[df_index_counter,'Año'      ] = year
            data.loc[df_index_counter,'Mes'      ] = month
            data.loc[df_index_counter,'Día'      ] = day
            data.loc[df_index_counter, dict_polutants[polut]] = li
            df_index_counter += 1
        else:
            # if it exists just add the polutant info
            data.loc[check[0], dict_polutants[polut]] = li
            if len(check) > 1:
                print('MORE THAN ONE ROW FOR A STATION AND DAY!!! THIS SHOULDNT BE!!')

    return data



