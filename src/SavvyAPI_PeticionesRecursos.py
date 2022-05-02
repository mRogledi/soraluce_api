# -*- coding: utf-8 -*-
import time
import json
import subprocess
import restClient
import streamData
import os
import config

#########################
## PETICIONES RECURSOS ##
#########################

# Identificadores de los recursos
idLocalizacion = "SG1_E6L23";
idMaquina = "MZK_BBM6VD";
idGrupo = "G_MZK_BBM6VD_HTM5DC";
idIndicador = "I_MZK_BBM6VD_4K1L8F";
idCategoria = "C_MZK_BBM6VD_PTWVAK";
idSeveridad = "S_MZK_BBM6VD_4NQBUY";
idLineaProduccion = "SG1_PL30";
idAlarma = "A_MZK_BBM6VD_YK33AD";
fileName = "B_VNM_HKMDHW_PAJGFT_1549756800671_1552348799671_files.zip";
fileNameForDemand = "bridgeLog_10.0.0.11_1551856443.zip";

# Listar las localizaciones
#     Ej: getLocations()
def getLocations():
    return json.dumps(restClient.listLocations());

# Información de una localización
#     Ej: getLocationInformation('SG1_E3L3')
def getLocationInformation(locationId):
    return json.dumps(restClient.locationInformation(locationId));

# Listar las máquinas a partir de un location id
#     Ej: getMachines('SG1_E3L3')
def getMachines():
    return json.dumps(restClient.listMachines())

# Información de una máquina
#     Ej: getMachineInformation('E1L1_SL8PR5')
def getMachineInformation(machineId):
    return json.dumps(restClient.machineInformation(machineId));

# Listar los grupos de captura de una máquina
#    Ej: getCaptureGroups('E1L1_SL8PR5')
def getCaptureGroups(machineId):
    return json.dumps(restClient.listCaptureGroups(machineId))

# Información de un grupo de captura de una máquina
#    Ej: getCaptureGroups('E1L1_SL8PR5', 'G_E1L1_SL8PR5_Q4R8ZB')
def getCaptureGroupInformation(machineId, groupId):
    return json.dumps(restClient.groupInformation(machineId, groupId))

# Lista los indicadores de una máquina
#    Ej: getIndicators('E1L1_SL8PR5')
def getIndicators(machineId):
    return json.dumps(restClient.listIndicators(machineId))

# Información de un indicador de una máquina
#    Ej: getIndicatorInformation('E1L1_SL8PR5')
def getIndicatorInformation(machineId, indicatorId):
    return json.dumps(restClient.indicatorInformation(machineId, indicatorId))

# Lista las categorias de alarma de una máquina
#    Ej: getCategories('E1L1_SL8PR5')
def getCategories(machineId):
    return json.dumps(restClient.listCategories(machineId))

# Información de una categoría de alarma de una máquina
#    Ej: getCategoryInformation('E1L1_SL8PR5')
def getCategoryInformation(machineId, categoryId):
    return json.dumps(restClient.categoryInformation(machineId, categoryId))

# Lista las severidaded de alarma de una máquina
#    Ej: getSeverities('E1L1_SL8PR5')
def getSeverities(machineId):
    return json.dumps(restClient.listSeverities(machineId))

# Información de una severidad de alarma de una máquina
#    Ej: getSeverityInformation('E1L1_SL8PR5')
def getSeverityInformation(machineId, severityId):
    return json.dumps(restClient.severityInformation(machineId, severityId))

# Lista las líneas de producción
#    Ej: getProductionLines('E1L1_SL8PR5')
def getProductionLines():
    return json.dumps(restClient.listProductionLines())

# Información de una línea de producción
#    Ej: getProductionLineInformation('E1L1_SL8PR5')
def getProductionLineInformation(productionLineId):
    return json.dumps(restClient.productionLineInformation(productionLineId))

# Información de un segmento
#    Ej: getSegmentInformation()
def getSegmentInformation():
    return json.dumps(restClient.segmentInformation())

# Lista las alarmas de una maquina
#    Ej: getAlarms('E1L1_SL8PR5')
def getAlarms(machineId):
    return json.dumps(restClient.listAlarms(machineId))

# Información de una alarma de una maquina
#    Ej: getIndicators('E1L1_SL8PR5')
def getAlarmInformation(machineId, productionLineId):
    return json.dumps(restClient.alarmInformation(machineId, productionLineId))
    
# Listado de ficheros de una máquina
#    Ej: getMachineFiles('E1L1_SL8PR5')
def getMachineFiles(machineId):
    return json.dumps(restClient.machineFiles(machineId))

# Información de una alarma de una maquina
#    Ej: getMachineFiles('E1L1_SL8PR5')
def getMachineFileInformation(machineId, fileName):
    return json.dumps(restClient.machineFileInformation(machineId, fileName))

# Información de una alarma de una maquina
#    Ej: getMachineFiles('E1L1_SL8PR5')
def updateFileInformation(machineId, fileName):
    return json.dumps(restClient.updateFileInformation(machineId, fileName))
    
'''
Posibles llamadas:

########
SEGMENTO
########

Respuesta: {"segmentLanguages":[{"languageLocale":"es_ES","languageDefault":true,"languageName":"Español"},
                                {"languageDefault":false,"languageName":"Euskara"},
                                {"languageLocale":"en_GB","languageDefault":false,"languageName":"English"},
                                {"languageLocale":"de_DE","languageDefault":false,"languageName":"Deutsch"},
                                {"languageLocale":"fr_FR","languageDefault":false,"languageName":"Français"}]}
print ("SEGMENT INFORMATION :: " + getSegmentInformation())
    
#########
LOCATIONS
#########
    
Respuesta:[{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},
           {"locationId":"SG1_E6L23","locationEnterpriseName":"Savvy Data Systems","locationName":"Tests Api 1"}]
print ("LOCATIONS :: " + getLocations())

Respuesta: {"locationId":"SG2_E1L1","locationEnterpriseName":"Empresa de demo","locationName":"Taller","geolocation":"43.301227464575554,-2.0148110389709473","timezone":"Europe/Madrid"}
print ("LOCATION INFORMATION :: " + getLocationInformation(idLocalizacion))

####################
LÍNEAS DE PRODUCCIÓN
####################

Respuesta: [{"lineId":"SG1_PL6","lineName":"Linea Maya","lineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"}},
		     {"lineId":"SG1_PL10","lineName":"Línea Ion","lineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"}},
		 	 {"lineId":"SG1_PL16","lineName":"Maya02"},
		    {"lineId":"SG1_PL19","lineName":"Linea de Jose","lineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"}},
		    {"lineId":"SG1_PL25","lineName":"Linea prueba"},
		    {"lineId":"SG1_PL30","lineName":"Tests Api 1","lineLocation":{"locationId":"SG1_E6L23","locationEnterpriseName":"Savvy Data Systems","locationName":"Tests Api 1"}}]
print ("PRODUCTION LINES :: " + getProductionLines())


Respuesta: {"lineId": "SG1_PL30", "lineName": "Tests Api 1", "lineLocation": {"locationId": "SG1_E6L23", "locationEnterpriseName": "Savvy Data Systems", "locationName": "Tests Api 1"}, "lineTranslates": []}
print ("PRODUCTION LINE INFORMATION :: " + getProductionLineInformation(idLineaProduccion))

########
MACHINES
########

Respuesta: [{"machineId":"QNQ_GRJ79R","machineName":"Máquina 0","machineAlarmsArchivedDate":"2019-01-25T12:59:59.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL10","lineName":"Línea Ion"}],"machineLastReceivedDate":"2011-12-31T23:00:00.000Z","machineDataAvailableFrom":"2019-01-25T12:59:59.000Z"},
   			  {"machineId":"CMS_9BX587","machineName":"Máquina 1","machineLastDate":"2019-03-27T15:58:44.000Z","machineMinuteLastDate":"2019-03-23T14:19:00.000Z","machineHourLastDate":"2019-03-23T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-11T14:39:48.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL6","lineName":"Linea Maya"},{"lineId":"SG1_PL16","lineName":"Maya02"},{"lineId":"SG1_PL25","lineName":"Linea prueba"}],"machineLastReceivedDate":"2019-03-27T15:59:56.000Z","machineDataAvailableFrom":"2019-01-28T07:32:12.000Z"},
			  {"machineId":"RWK_Q3HEYJ","machineName":"Máquina 2","machineLastDate":"2019-03-27T14:57:04.000Z","machineMinuteLastDate":"2019-03-22T14:24:00.000Z","machineHourLastDate":"2019-03-22T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-16T16:00:09.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL16","lineName":"Maya02"}],"machineLastReceivedDate":"2019-03-25T13:36:07.000Z","machineDataAvailableFrom":"2019-01-28T07:32:48.000Z"},
			  {"machineId":"VNM_HKMDHW","machineName":"Máquina 3","machineLastDate":"2019-03-27T15:59:26.000Z","machineMinuteLastDate":"2019-03-15T16:14:00.000Z","machineHourLastDate":"2019-03-15T16:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:45:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL16","lineName":"Maya02"}],"machineLastReceivedDate":"2019-03-27T15:59:56.000Z","machineDataAvailableFrom":"2019-01-28T07:33:14.000Z"},
		 	  {"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:57:42.000Z","machineMinuteLastDate":"2019-03-22T14:19:00.000Z","machineHourLastDate":"2019-03-22T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:51:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:59:49.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}]
print ("MACHINES :: " + getMachines())

Respuesta: {"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:57:42.000Z","machineMinuteLastDate":"2019-03-22T14:19:00.000Z","machineHourLastDate":"2019-03-22T14:00:00.000Z",
			  "machineAlarmsArchivedDate":"2019-02-25T15:51:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},
			  "machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:59:49.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z",
	 	     "machineCreationDate":"2019-03-18T12:03:33.000Z","machineStoragePeriod":"unbounded","machineTranslates":[],"machineGroups":[{"groupId":"G_MZK_BBM6VD_HTM5DC","groupName":"Grupo 1",
			  "groupActive":true,"groupLastDate":"2019-03-22T14:18:07.932Z","groupMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:57:42.000Z",
			  "machineMinuteLastDate":"2019-03-22T14:19:00.000Z","machineHourLastDate":"2019-03-22T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:51:42.000Z",
			  "machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],
		      "machineLastReceivedDate":"2019-03-27T15:59:49.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}},{"groupId":"G_MZK_BBM6VD_JTT348","groupName":"Grupo 5",
			   "groupActive":true,"groupLastDate":"2019-03-18T13:49:30.661Z","groupMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:57:42.000Z","machineMinuteLastDate":"2019-03-22T14:19:00.000Z",
              ......}
print ("MACHINE INFORMATION :: " + getMachineInformation(idMaquina))

######
GROUPS
######

Respuesta: [{"groupId":"G_MZK_BBM6VD_HTM5DC","groupName":"Grupo 1","groupActive":true,"groupLastDate":"2019-03-22T14:18:07.932Z","groupMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:57:42.000Z","machineMinuteLastDate":"2019-03-22T14:19:00.000Z","machineHourLastDate":"2019-03-22T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:51:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:59:49.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}},
		     {"groupId":"G_MZK_BBM6VD_JTT348","groupName":"Grupo 5","groupActive":true,"groupLastDate":"2019-03-18T13:49:30.661Z","groupMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:57:42.000Z","machineMinuteLastDate":"2019-03-22T14:19:00.000Z","machineHourLastDate":"2019-03-22T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:51:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:59:49.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}},
		     {"groupId":"G_MZK_BBM6VD_KLXLFZ","groupName":"Grupo 3 (Desactivado)","groupActive":false,"groupMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:57:42.000Z","machineMinuteLastDate":"2019-03-22T14:19:00.000Z","machineHourLastDate":"2019-03-22T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:51:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:59:49.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}}]
print ("GROUPS :: " + getCaptureGroups(idMaquina))

Respuesta: {"groupId": "G_E1L1_SL8PR5_Q4R8ZB", "groupName": "Test", "groupActive": true, "groupLastDate": "2018-09-12T15:28:42.0Z", "groupDescription": "", "groupType": "4", "groupFrequency": "1000", "groupDataSize": "483268"}
print ("GROUP INFORMATION :: " + getCaptureGroupInformation('G_E1L1_SL8PR5_Q4R8ZB', 'G_E1L1_SL8PR5_Q4R8ZB'))


##########
INDICATORS
##########

Respuesta: [{"indicatorId":"I_MZK_BBM6VD_4K1L8F","indicatorName":"Indicador 1","indicatorGroup":{"groupId":"G_MZK_BBM6VD_HTM5DC","groupName":"Grupo 1","groupActive":true,"groupLastDate":"2019-03-22T14:18:07.932Z","groupMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:57:42.000Z","machineMinuteLastDate":"2019-03-22T14:19:00.000Z","machineHourLastDate":"2019-03-22T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:51:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:59:59.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}},"indicatorActive":true,"indicatorIsKey":false,"indicatorMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:57:42.000Z","machineMinuteLastDate":"2019-03-22T14:19:00.000Z","machineHourLastDate":"2019-03-22T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:51:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:59:59.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}},
		     {"indicatorId":"I_MZK_BBM6VD_BSQ7EH","indicatorName":"Indicador 3 (Desactivado)","indicatorGroup":{"groupId":"G_MZK_BBM6VD_HTM5DC","groupName":"Grupo 1","groupActive":true,"groupLastDate":"2019-03-22T14:18:07.932Z","groupMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:57:42.000Z","machineMinuteLastDate":"2019-03-22T14:19:00.000Z","machineHourLastDate":"2019-03-22T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:51:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:59:59.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}},"indicatorActive":false,"indicatorIsKey":false,"indicatorMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:57:42.000Z","machineMinuteLastDate":"2019-03-22T14:19:00.000Z","machineHourLastDate":"2019-03-22T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:51:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:59:59.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}},
            {"indicatorId":"I_MZK_BBM6VD_KEMGHT","indicatorName":"Indicador 5 (clave)","indicatorGroup":{"groupId":"G_MZK_BBM6VD_JTT348","groupName":"Grupo 5","groupActive":true,"groupLastDate":"2019-03-18T13:49:30.661Z","groupMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:57:42.000Z","machineMinuteLastDate":"2019-03-22T14:19:00.000Z","machineHourLastDate":"2019-03-22T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:51:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:59:59.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}},"indicatorActive":true,"indicatorIsKey":true,"indicatorMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:57:42.000Z","machineMinuteLastDate":"2019-03-22T14:19:00.000Z","machineHourLastDate":"2019-03-22T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:51:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:59:59.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}},
		     {"indicatorId":"I_MZK_BBM6VD_D1UPQ9","indicatorName":"Indicador 8 (en grupo desactivado)","indicatorGroup":{"groupId":"G_MZK_BBM6VD_KLXLFZ","groupName":"Grupo 3 (Desactivado)","groupActive":false,"groupMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:57:42.000Z","machineMinuteLastDate":"2019-03-22T14:19:00.000Z","machineHourLastDate":"2019-03-22T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:51:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:59:59.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}},"indicatorActive":true,"indicatorIsKey":false,"indicatorMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:57:42.000Z","machineMinuteLastDate":"2019-03-22T14:19:00.000Z","machineHourLastDate":"2019-03-22T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:51:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:59:59.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}}]
print ("INDICATORS :: " + getIndicators(idMaquina))


Respuesta: {"indicatorId":"I_MZK_BBM6VD_4K1L8F","indicatorName":"Indicador 1","indicatorGroup":{"groupId":"G_MZK_BBM6VD_HTM5DC","groupName":"Grupo 1",
			  "groupActive":true,"groupLastDate":"2019-03-24T14:18:04.271Z","groupMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1",
			  "machineLastDate":"2019-03-27T16:07:53.000Z","machineMinuteLastDate":"2019-03-24T14:19:00.000Z","machineHourLastDate":"2019-03-24T14:00:00.000Z",
			  "machineAlarmsArchivedDate":"2019-02-25T16:00:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems",
			  "locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T16:08:09.000Z",
			  "machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}},"indicatorActive":true,"indicatorIsKey":false,
			  "indicatorMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T16:07:53.000Z","machineMinuteLastDate":"2019-03-24T14:19:00.000Z",
		  	  "machineHourLastDate":"2019-03-24T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T16:00:42.000Z","machineLocation":{"locationId":"SG1_E6L4",
		     "locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],
		     "machineLastReceivedDate":"2019-03-27T16:08:09.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"},"indicatorOrigin":"1","indicatorTargetValue":"",
		     "indicatorComparer":"","indicatorTranslates":[]}
print ("INDICATOR INFORMATION :: " + getIndicatorInformation(idMaquina, idIndicador))

#######
ALARMAS
#######

Respuesta: [{"alarmId":"A_MZK_BBM6VD_YK33AD","alarmCode":"1","alarmDescription":"Alarma 1","alarmSeverity":{"severityId":"S_MZK_BBM6VD_4NQBUY","severityName":"Mucha","severityMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:48:42.000Z","machineMinuteLastDate":"2019-03-21T14:19:00.000Z","machineHourLastDate":"2019-03-21T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:45:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:49:19.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}},"alarmCategory":{"categoryId":"C_MZK_BBM6VD_PTWVAK","categoryName":"Alerta por %","categoryMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:48:42.000Z","machineMinuteLastDate":"2019-03-21T14:19:00.000Z","machineHourLastDate":"2019-03-21T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:45:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:49:19.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}},"alarmMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:48:42.000Z","machineMinuteLastDate":"2019-03-21T14:19:00.000Z","machineHourLastDate":"2019-03-21T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:45:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:49:19.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}},
			  {"alarmId":"A_MZK_BBM6VD_8CMJ5Y","alarmCode":"2","alarmDescription":"Alarma 2 (sin severidad ni categoria)","alarmMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:48:42.000Z","machineMinuteLastDate":"2019-03-21T14:19:00.000Z","machineHourLastDate":"2019-03-21T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:45:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:49:19.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}}]
print ("ALARMS :: " + getAlarms(idMaquina))


Respuesta: {"alarmId":"A_MZK_BBM6VD_YK33AD","alarmCode":"1","alarmDescription":"Alarma 1","alarmSeverity":{"severityId":"S_MZK_BBM6VD_4NQBUY","severityName":"Mucha","severityMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:48:42.000Z","machineMinuteLastDate":"2019-03-21T14:19:00.000Z","machineHourLastDate":"2019-03-21T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:45:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:49:19.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}},"alarmCategory":{"categoryId":"C_MZK_BBM6VD_PTWVAK","categoryName":"Alerta por %","categoryMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:48:42.000Z","machineMinuteLastDate":"2019-03-21T14:19:00.000Z","machineHourLastDate":"2019-03-21T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:45:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:49:19.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"},"categoryDescription":"","categoryTranslates":[]},"alarmMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-27T15:48:42.000Z","machineMinuteLastDate":"2019-03-21T14:19:00.000Z","machineHourLastDate":"2019-03-21T14:00:00.000Z","machineAlarmsArchivedDate":"2019-02-25T15:45:42.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-27T15:49:19.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"},"alarmType":"normal","alarmTranslates":[]}
print ("ALARM INFORMATION :: " + getAlarmInformation(idMaquina, idAlarma))

####################
CATEGORIAS DE ALARMA
####################

Respuesta: [{"categoryId":"C_MZK_BBM6VD_PTWVAK","categoryName":"Alerta por %","categoryMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-28T07:46:26.000Z","machineMinuteLastDate":"2019-03-28T07:43:00.000Z","machineHourLastDate":"2019-03-28T07:00:00.000Z","machineAlarmsArchivedDate":"2019-02-26T07:43:26.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-28T07:48:32.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}}]
print ("CATEGORIES :: " + getCategories(idMaquina))


Respuesta: {"categoryId":"C_MZK_BBM6VD_PTWVAK","categoryName":"Alerta por %","categoryMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-28T07:49:26.000Z","machineMinuteLastDate":"2019-03-28T07:49:00.000Z","machineHourLastDate":"2019-03-28T07:00:00.000Z","machineAlarmsArchivedDate":"2019-02-26T07:49:26.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-28T07:51:52.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"},"categoryDescription":"","categoryTranslates":[]}
print ("CATEGORY INFORMATION :: " + getCategoryInformation(idMaquina, idCategoria))

#####################
SEVERIDADES DE ALARMA
#####################

Respuesta: [{"severityId":"S_MZK_BBM6VD_4NQBUY","severityName":"Mucha","severityMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-28T07:40:26.000Z","machineMinuteLastDate":"2019-03-28T07:34:00.000Z","machineHourLastDate":"2019-03-28T07:00:00.000Z","machineAlarmsArchivedDate":"2019-02-26T07:34:25.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-28T07:43:12.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}}]
print ("SEVERITIES :: " + getSeverities(idMaquina))


Respuesta: {"severityId":"S_MZK_BBM6VD_4NQBUY","severityName":"Mucha","severityMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-28T07:46:26.000Z","machineMinuteLastDate":"2019-03-28T07:43:00.000Z","machineHourLastDate":"2019-03-28T07:00:00.000Z","machineAlarmsArchivedDate":"2019-02-26T07:43:26.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-28T07:48:32.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"},"severityDescription":"","severityTranslates":[]}
print ("SEVERYTY INFORMATION :: " + getSeverityInformation(idMaquina, idSeveridad))

#######################
FICHEROS DE UNA MÁQUINA
#######################

Respuesta: [{"fileName":"B_VNM_HKMDHW_PAJGFT_1549756800671_1552348799671_files.zip","fileType":"send","fileStatus":"available","fileSize":"8246","fileCaptureDate":1553760415000,"fileReceptionDate":1553760416000,"fileMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-28T09:39:44.000Z","machineMinuteLastDate":"2019-03-28T09:39:00.000Z","machineHourLastDate":"2019-03-28T09:00:00.000Z","machineAlarmsArchivedDate":"2019-02-26T09:39:44.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-28T09:42:32.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}},
            {"fileName":"B_MPH_A92TVZ_grupo_1525125600000_1527803940000_files02.zip","fileType":"onDemand","fileStatus":"onDemand","fileSize":"1232","fileCaptureDate":1553762542000,"fileMachine":{"machineId":"MZK_BBM6VD","machineName":"Tests Api 1","machineLastDate":"2019-03-28T09:39:44.000Z","machineMinuteLastDate":"2019-03-28T09:39:00.000Z","machineHourLastDate":"2019-03-28T09:00:00.000Z","machineAlarmsArchivedDate":"2019-02-26T09:39:44.000Z","machineLocation":{"locationId":"SG1_E6L4","locationEnterpriseName":"Savvy Data Systems","locationName":"Oficina"},"machineProductionLines":[{"lineId":"SG1_PL30","lineName":"Tests Api 1"}],"machineLastReceivedDate":"2019-03-28T09:42:32.000Z","machineDataAvailableFrom":"2019-03-18T12:03:33.000Z"}}]
print ("MACHINE FILES :: " + getMachineFiles(idMaquina))

Respuesta: {"fileName": "B_VNM_HKMDHW_PAJGFT_1549756800671_1552348799671_files.zip", "fileType": "send", "fileStatus": "available", "fileSize": "8246", "fileCaptureDate": 1553760415000, "fileReceptionDate": 1553760416000, "fileMachine": {"machineId": "MZK_BBM6VD", "machineName": "Tests Api 1", "machineLastDate": "2019-04-01T07:42:29.000Z", "machineMinuteLastDate": "2019-04-01T07:39:00.000Z", "machineHourLastDate": "2019-04-01T07:00:00.000Z", "machineAlarmsArchivedDate": "2019-03-02T07:39:29.000Z", "machineLocation": {"locationId": "SG1_E6L4", "locationEnterpriseName": "Savvy Data Systems", "locationName": "Oficina"}, "machineProductionLines": [{"lineId": "SG1_PL30", "lineName": "Tests Api 1"}], "machineLastReceivedDate": "2019-04-01T07:43:53.000Z", "machineDataAvailableFrom": "2019-03-18T12:03:33.000Z"}}
print ("MACHINE FILE INFORMATION :: " + getMachineFileInformation(idMaquina, fileName))

Respuesta: Con este tipo de petición se actualizará el fichero indicado para que el servidor comiece la descarga del fichero desde el captador al servidor..
print ("MACHINE FILE GET FROM SMARTBOX :: " + updateFileInformation(idMaquina, fileNameForDemand))

'''

print ("MACHINE INFORMATION :: " + getMachineInformation(idMaquina))
