# -*- coding: utf-8 -*-
import time
import json
import subprocess

from numpy import dtype
import restClient
import streamData
import os
import config

'''
SavvyAPI.py
    Contiene todas funciones que pueden ser llamadas desde MATLAB. De aquí se llama al cliente para que haga todas las gestiones oportunas
'''

#####################
## METAINFORMACION ##
#####################

# Identificadores de los recursos
idLocalizacion = "SG1_E6L23";
idMaquina = "MZK_BBM6VD";
idGrupo = "G_MZK_BBM6VD_HTM5DC";
idIndicador = "I_MZK_BBM6VD_4K1L8F";
modoHumanOn = "1";
modoHumanOff = "0";

dateFrom = '1553076000000';
dateTo = '1553083200000';

# Capturar los datos de la máquina indicada como parámetro dentro de un rango
#    Ej: getMachineData('MZK_BBM6VD', '0', '1513343363000', '1513343373000')
def getMachineData(machineId, human, timestampFrom = None, timestampTo = None):
    return json.dumps(restClient.getData(machineId, human, timestampFrom, timestampTo)).replace('$', '')

# Capturar los datos del grupo indicada como parámetro dentro de un rango
#    Ej: getGroupData('MZK_BBM6VD', '0', '1513343363000', '1513343373000')
def getGroupData(groupId, human, timestampFrom = None, timestampTo = None):
    return json.dumps(restClient.getGroupData(groupId, human, timestampFrom, timestampTo)).replace('$', '')

# Capturar los datos del indicador indicada como parámetro dentro de un rango
#    Ej: getGroupData('G_MZK_BBM6VD_HTM5DC', '0', '1513343363000', '1513343373000')
def getIndicatorData(indicatorId, human, timestampFrom = None, timestampTo = None):
    return json.dumps(restClient.getIndicatorData(indicatorId, human, timestampFrom, timestampTo)).replace('$', '')

# getIndicatorData('I_RGP_D5TDHU_LUH6XQ', '0', '1643097600000', '1643130000000')

indicator_data = (restClient.listIndicators('RGP_D5TDHU'))
print(type(indicator_data))
print(indicator_data[0])
# print(restClient.groupInformation('RGP_D5TDHU','G_RGP_D5TDHU_TYZBPS'))

# print(restClient.indicatorInformation('RGP_D5TDHU','I_RGP_D5TDHU_3JN99Z'))

# print(restClient.getData('RGP_D5TDHU','0','1643184000000','1643220000000'))

# getIndicatorData('I_RGP_D5TDHU_SJ2F7A','0','1643216400000','1643220000000')

# resource = '/v2/data?machines=RGP_D5TDHU&human=0'
# restClient.customCall(resource)





'''
Posibles llamadas:

#############################
DATA 1 MACHINE SIN MODO HUMAN
#############################

Respuesta: {"data" : [
			{"machine" : "MZK_BBM6VD" , 
			"data" : [
			{"group": "G_MZK_BBM6VD_KLXLFZ","data":[], "metadata": {}}, 
			{"group": "G_MZK_BBM6VD_HTM5DC","data":[
			{ "timestamp" : "2019-03-28T16:06:15.067Z" , "I_MZK_BBM6VD_4K1L8F" : -0.29073623283496397}
			 ,{ "timestamp" : "2019-03-28T16:06:05.068Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9910076890250326}
			 ,{ "timestamp" : "2019-03-28T16:05:55.068Z" , "I_MZK_BBM6VD_4K1L8F" : -0.5340731967283592}
			 ,{ "timestamp" : "2019-03-28T16:05:45.068Z" , "I_MZK_BBM6VD_4K1L8F" : -0.54650194641878}
			 ,{ "timestamp" : "2019-03-28T16:05:35.068Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9889233090664216}
			 ,{ "timestamp" : "2019-03-28T16:05:25.068Z" , "I_MZK_BBM6VD_4K1L8F" : -0.2765726668926666}
			 ....
			 ....
			 ....
			 ,{ "timestamp" : "2019-03-28T15:07:04.758Z" , "I_MZK_BBM6VD_4K1L8F" : -0.23083517666915765}
			 ,{ "timestamp" : "2019-03-28T15:06:54.758Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9808402169940765}
			 ,{ "timestamp" : "2019-03-28T15:06:44.758Z" , "I_MZK_BBM6VD_4K1L8F" : -0.5853173619979521}
			 ,{ "timestamp" : "2019-03-28T15:06:34.758Z" , "I_MZK_BBM6VD_4K1L8F" : -0.4935103647124094}
			 ,{ "timestamp" : "2019-03-28T15:06:24.758Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9962250438880216}
			], "metadata": {"resultsFrom":"2019-03-28T15:06:24.758Z","resultsTo":"2019-03-28T16:06:15.067Z"}}, 
			{"group": "G_MZK_BBM6VD_JTT348","data":[], "metadata": {}}
			]}] , "metadata": {"warnings":[  ] , "executionTime" : 751 , "bloqued" : false , "bloquedStatus" : "High"}}
    
print ("MACHINE DATA :: " + getMachineData(idMaquina, modoHumanOff))

#############################
DATA 1 MACHINE CON MODO HUMAN
#############################

Respuesta: { "data" : [
		   {"machine" : "Tests Api 1" , "data" : [
		   {"group": "Grupo 3 (Desactivado)","data":[] , "metadata": {}}, 
		   {"group": "Grupo 1","data":[
		   	{ "timestamp" : "2019-03-28T16:24:35.155Z" , "Indicador 1" : -0.3902568016886103}
 			,{ "timestamp" : "2019-03-28T16:24:25.155Z" , "Indicador 1" : 0.9996054118638734}
 			,{ "timestamp" : "2019-03-28T16:24:15.155Z" , "Indicador 1" : -0.44170376643491815}
 			,{ "timestamp" : "2019-03-28T16:24:05.155Z" , "Indicador 1" : -0.6319725245314184}
 			,{ "timestamp" : "2019-03-28T16:23:55.155Z" , "Indicador 1" : 0.9676905001718403}
 			,{ "timestamp" : "2019-03-28T16:23:45.155Z" , "Indicador 1" : -0.1734301562750482}
			...
			...
			...
 			,{ "timestamp" : "2019-03-28T15:25:24.849Z" , "Indicador 1" : -0.33315728016346013}
 			,{ "timestamp" : "2019-03-28T15:25:14.849Z" , "Indicador 1" : 0.9959927653839821}
 			,{ "timestamp" : "2019-03-28T15:25:04.849Z" , "Indicador 1" : -0.49580119691330854}
 			,{ "timestamp" : "2019-03-28T15:24:54.849Z" , "Indicador 1" : -0.5833405660804617}
 			,{ "timestamp" : "2019-03-28T15:24:44.849Z" , "Indicador 1" : 0.9813118593213154}
 		   ], "metadata": {"resultsFrom":"2019-03-28T15:24:44.849Z","resultsTo":"2019-03-28T16:24:35.155Z"}}, 
 		   {"group": "Grupo 5","data":[], "metadata": {}}
			]}], "metadata": {"warnings":[  ] , "executionTime" : 674 , "bloqued" : false , "bloquedStatus" : "High"}}

print ("MACHINE DATA :: " + getMachineData(idMaquina, modoHumanOn))

###############################
DATA 1 MACHINE WITH FROM AND TO
###############################

Respuesta: { "data" : [
		   {"machine" : "MZK_BBM6VD" , "data" : [
		   {"group": "G_MZK_BBM6VD_HTM5DC","data":[
			{ "timestamp" : "2019-03-20T11:59:54.988Z" , "I_MZK_BBM6VD_4K1L8F" : -0.01941793934642864}
			 ,{ "timestamp" : "2019-03-20T11:59:44.988Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9172066965015869}
			 ,{ "timestamp" : "2019-03-20T11:59:34.988Z" , "I_MZK_BBM6VD_4K1L8F" : -0.743967391071552}
			 ,{ "timestamp" : "2019-03-20T11:59:24.988Z" , "I_MZK_BBM6VD_4K1L8F" : -0.2980073439242727}
			 ,{ "timestamp" : "2019-03-20T11:59:14.988Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9919717491958542}
			 ,{ "timestamp" : "2019-03-20T11:59:04.988Z" , "I_MZK_BBM6VD_4K1L8F" : -0.5276254978483683}
			...
			...
			...
			 ,{ "timestamp" : "2019-03-20T11:48:03.437Z" , "I_MZK_BBM6VD_4K1L8F" : -0.7951842865957521}
			 ,{ "timestamp" : "2019-03-20T11:47:53.437Z" , "I_MZK_BBM6VD_4K1L8F" : -0.22065039338401332}
			 ,{ "timestamp" : "2019-03-20T11:47:43.437Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9787089033759818}
			 ,{ "timestamp" : "2019-03-20T11:47:33.437Z" , "I_MZK_BBM6VD_4K1L8F" : -0.593922834696862}
			 ,{ "timestamp" : "2019-03-20T11:47:23.446Z" , "I_MZK_BBM6VD_4K1L8F" : -0.4891078018338196}
			], "metadata": {"resultsFrom":"2019-03-20T11:47:23.446Z","resultsTo":"2019-03-20T11:59:54.988Z"}}, 
		   ]}], "metadata": {"warnings":[  ] , "executionTime" : 592 , "bloqued" : false , "bloquedStatus" : "High"}}
    
print ("MACHINE DATA :: " + getMachineData(idMaquina, modoHumanOff, dateFrom, dateTo))

###########################
DATA 1 GROUP SIN MODO HUMAN
###########################

Respuesta: {"data" : [
			{"machine" : "MZK_BBM6VD" , 
			"data" : [
			{"group": "G_MZK_BBM6VD_KLXLFZ","data":[], "metadata": {}}, 
			{"group": "G_MZK_BBM6VD_HTM5DC","data":[
			{ "timestamp" : "2019-03-28T16:06:15.067Z" , "I_MZK_BBM6VD_4K1L8F" : -0.29073623283496397}
			 ,{ "timestamp" : "2019-03-28T16:06:05.068Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9910076890250326}
			 ,{ "timestamp" : "2019-03-28T16:05:55.068Z" , "I_MZK_BBM6VD_4K1L8F" : -0.5340731967283592}
			 ,{ "timestamp" : "2019-03-28T16:05:45.068Z" , "I_MZK_BBM6VD_4K1L8F" : -0.54650194641878}
			 ,{ "timestamp" : "2019-03-28T16:05:35.068Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9889233090664216}
			 ,{ "timestamp" : "2019-03-28T16:05:25.068Z" , "I_MZK_BBM6VD_4K1L8F" : -0.2765726668926666}
			 ....
			 ....
			 ....
			 ,{ "timestamp" : "2019-03-28T15:07:04.758Z" , "I_MZK_BBM6VD_4K1L8F" : -0.23083517666915765}
			 ,{ "timestamp" : "2019-03-28T15:06:54.758Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9808402169940765}
			 ,{ "timestamp" : "2019-03-28T15:06:44.758Z" , "I_MZK_BBM6VD_4K1L8F" : -0.5853173619979521}
			 ,{ "timestamp" : "2019-03-28T15:06:34.758Z" , "I_MZK_BBM6VD_4K1L8F" : -0.4935103647124094}
			 ,{ "timestamp" : "2019-03-28T15:06:24.758Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9962250438880216}
			], "metadata": {"resultsFrom":"2019-03-28T15:06:24.758Z","resultsTo":"2019-03-28T16:06:15.067Z"}}, 
			{"group": "G_MZK_BBM6VD_JTT348","data":[], "metadata": {}}
			]}] , "metadata": {"warnings":[  ] , "executionTime" : 751 , "bloqued" : false , "bloquedStatus" : "High"}}
    
print ("GROUP DATA :: " + getGroupData(idGrupo, modoHumanOff))

#############################
DATA 1 GROUP WITH FROM AND TO
#############################

Respuesta: { "data" : [
		   {"machine" : "MZK_BBM6VD" , "data" : [
		   {"group": "G_MZK_BBM6VD_HTM5DC","data":[
			{ "timestamp" : "2019-03-28T16:06:15.067Z" , "I_MZK_BBM6VD_4K1L8F" : -0.29073623283496397}
			 ,{ "timestamp" : "2019-03-28T16:06:05.068Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9910076890250326}
			 ,{ "timestamp" : "2019-03-28T16:05:55.068Z" , "I_MZK_BBM6VD_4K1L8F" : -0.5340731967283592}
			 ,{ "timestamp" : "2019-03-28T16:05:45.068Z" , "I_MZK_BBM6VD_4K1L8F" : -0.54650194641878}
			 ,{ "timestamp" : "2019-03-28T16:05:35.068Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9889233090664216}
			 ,{ "timestamp" : "2019-03-28T16:05:25.068Z" , "I_MZK_BBM6VD_4K1L8F" : -0.2765726668926666}
			 ....
			 ....
			 ....
			 ,{ "timestamp" : "2019-03-28T15:07:04.758Z" , "I_MZK_BBM6VD_4K1L8F" : -0.23083517666915765}
			 ,{ "timestamp" : "2019-03-28T15:06:54.758Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9808402169940765}
			 ,{ "timestamp" : "2019-03-28T15:06:44.758Z" , "I_MZK_BBM6VD_4K1L8F" : -0.5853173619979521}
			 ,{ "timestamp" : "2019-03-28T15:06:34.758Z" , "I_MZK_BBM6VD_4K1L8F" : -0.4935103647124094}
			 ,{ "timestamp" : "2019-03-28T15:06:24.758Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9962250438880216}
			], "metadata": {"resultsFrom":"2019-03-28T15:06:24.758Z","resultsTo":"2019-03-28T16:06:15.067Z"}}
		   ]}], "metadata": {"warnings":[  ] , "executionTime" : 592 , "bloqued" : false , "bloquedStatus" : "High"}}

print ("GROUP DATA :: " + getGroupData(idGrupo, modoHumanOff, dateFrom, dateTo))

###############################
DATA 1 INDICATOR SIN MODO HUMAN
###############################

Respuesta: { "data" : [
		   {"machine" : "MZK_BBM6VD" , "data" : [
		   {"group": "G_MZK_BBM6VD_HTM5DC","data":[
			{ "timestamp" : "2019-03-28T16:06:15.067Z" , "I_MZK_BBM6VD_4K1L8F" : -0.29073623283496397}
			 ,{ "timestamp" : "2019-03-28T16:06:05.068Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9910076890250326}
			 ,{ "timestamp" : "2019-03-28T16:05:55.068Z" , "I_MZK_BBM6VD_4K1L8F" : -0.5340731967283592}
			 ,{ "timestamp" : "2019-03-28T16:05:45.068Z" , "I_MZK_BBM6VD_4K1L8F" : -0.54650194641878}
			 ,{ "timestamp" : "2019-03-28T16:05:35.068Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9889233090664216}
			 ,{ "timestamp" : "2019-03-28T16:05:25.068Z" , "I_MZK_BBM6VD_4K1L8F" : -0.2765726668926666}
			 ....
			 ....
			 ....
			 ,{ "timestamp" : "2019-03-28T15:07:04.758Z" , "I_MZK_BBM6VD_4K1L8F" : -0.23083517666915765}
			 ,{ "timestamp" : "2019-03-28T15:06:54.758Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9808402169940765}
			 ,{ "timestamp" : "2019-03-28T15:06:44.758Z" , "I_MZK_BBM6VD_4K1L8F" : -0.5853173619979521}
			 ,{ "timestamp" : "2019-03-28T15:06:34.758Z" , "I_MZK_BBM6VD_4K1L8F" : -0.4935103647124094}
			 ,{ "timestamp" : "2019-03-28T15:06:24.758Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9962250438880216}
			], "metadata": {"resultsFrom":"2019-03-28T15:06:24.758Z","resultsTo":"2019-03-28T16:06:15.067Z"}}
		   ]}], "metadata": {"warnings":[  ] , "executionTime" : 592 , "bloqued" : false , "bloquedStatus" : "High"}}
    
print ("INDICATOR DATA :: " + getIndicatorData(idIndicador, modoHumanOff))

#################################
DATA 1 INDICATOR WITH FROM AND TO
#################################

Respuesta: { "data" : [
		   {"machine" : "MZK_BBM6VD" , "data" : [
		   {"group": "G_MZK_BBM6VD_HTM5DC","data":[
			{ "timestamp" : "2019-03-20T11:59:54.988Z" , "I_MZK_BBM6VD_4K1L8F" : -0.01941793934642864}
			 ,{ "timestamp" : "2019-03-20T11:59:44.988Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9172066965015869}
			 ,{ "timestamp" : "2019-03-20T11:59:34.988Z" , "I_MZK_BBM6VD_4K1L8F" : -0.743967391071552}
			 ,{ "timestamp" : "2019-03-20T11:59:24.988Z" , "I_MZK_BBM6VD_4K1L8F" : -0.2980073439242727}
			 ,{ "timestamp" : "2019-03-20T11:59:14.988Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9919717491958542}
			 ,{ "timestamp" : "2019-03-20T11:59:04.988Z" , "I_MZK_BBM6VD_4K1L8F" : -0.5276254978483683}
			...
			...
			...
			 ,{ "timestamp" : "2019-03-20T11:48:03.437Z" , "I_MZK_BBM6VD_4K1L8F" : -0.7951842865957521}
			 ,{ "timestamp" : "2019-03-20T11:47:53.437Z" , "I_MZK_BBM6VD_4K1L8F" : -0.22065039338401332}
			 ,{ "timestamp" : "2019-03-20T11:47:43.437Z" , "I_MZK_BBM6VD_4K1L8F" : 0.9787089033759818}
			 ,{ "timestamp" : "2019-03-20T11:47:33.437Z" , "I_MZK_BBM6VD_4K1L8F" : -0.593922834696862}
			 ,{ "timestamp" : "2019-03-20T11:47:23.446Z" , "I_MZK_BBM6VD_4K1L8F" : -0.4891078018338196}
			], "metadata": {"resultsFrom":"2019-03-20T11:47:23.446Z","resultsTo":"2019-03-20T11:59:54.988Z"}}, 
		   ]}], "metadata": {"warnings":[  ] , "executionTime" : 592 , "bloqued" : false , "bloquedStatus" : "High"}}

print ("INDICATOR DATA :: " + getIndicatorData(idIndicador, modoHumanOff, dateFrom, dateTo))

'''

print ("MACHINE DATA :: " + getMachineData(idMaquina, modoHumanOff))
