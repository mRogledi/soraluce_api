# -*- coding: utf-8 -*-
import time
import json
import subprocess
import restClient
import streamData
import os
import config

'''
SavvyAPI.py
    Contiene todas funciones que pueden ser llamadas desde MATLAB. De aquí se llama al cliente para que haga todas las gestiones oportunas
'''

####################
## FILES DOWNLOAD ##
####################

# Identificadores de los recursos
idMaquina = "MZK_BBM6VD";
fileNameForDownload = "B_VNM_HKMDHW_PAJGFT_1549756800671_1552348799671_files.zip";

# Descarga de un fichero de una máquina
#    Ej: getMachineFiles('E1L1_SL8PR5', 'fileName')
def downloadMachineFile(machineId, fileName):
    return json.dumps(restClient.downloadMachineFile(machineId, fileName))

print(restClient.machineFiles('RGP_D5TDHU'))
    
    
'''
Posibles llamadas:


#######################
FICHEROS DE UNA MÁQUINA
#######################

Respuesta: Con este tipo de petición se devolverá el FICHERO pasado en la url de la máquina indicada.
           Se mostrará una pequeña información en JSON para poder saber cuanto ocupa el fichero y leerlo correctamente y a continuación el fichero.
           {"status":200 , "fileName":"B_VNM_HKMDHW_PAJGFT_1549756800671_1552348799671_files.zip","fileSize":6278867}
print ("MACHINE FILE DOWNLOAD :: " + downloadMachineFile(idMaquina, fileNameForDownload))


'''