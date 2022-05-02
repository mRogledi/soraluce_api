# -*- coding: utf-8 -*-
import requests
import logging
import time
import json
import config
import sys
import io

'''
restClient.py
    Se encarga de realizar las llamadas a la API
'''

# Para evitar el warning InsecureRequestWarning http://urllib3.readthedocs.org/en/latest/security.html#disabling-warnings
# Se usa urllib3 dentro de request, hay que afinar el import http://goo.gl/3YtXMz
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client

def sign_request(_secret, _target):
    from hashlib import sha1
    import hmac
    import base64
    #To support python 3
    # No sé si por la versión de hmac o de python, pero me pide string en lugar de bytearray
    hashed = hmac.new(bytearray(_secret, 'utf-8'), bytearray(_target, 'utf-8'), sha1)
    #hashed = hmac.new(_secret, _target, sha1)
    return base64.b64encode(hashed.digest()).decode()

def getCustomHeaders (_resource):    
    # Generar un número de secuencia en milisegundos para poder hacer peticiones de forma más rápida  ==> * 1000
    millis = int(round(time.time()))
    
    # Parámetros necesarios para generar la cabecera firmada
    sequence = str(millis)
    apyKey = config.api['key']
    apySecret = config.api['secret']
    method = config.api['method']
    contentType = config.api['contenType']
    
    # String a firmar
    signString = method + '\n' + contentType + '\n' + sequence + '\n' + _resource
    
    # Firmar el string y generar el valor de la cabecera de autenticación
    authHeader =  'M2C '+ apyKey + ':' + sign_request(apySecret, signString)
    print(authHeader)

    # Montar y devolver todas las cabeceras necesarias en la petición
    custom_headers = {    'Content-Type': contentType,
                        'X-M2C-Sequence': sequence,                    
                          'Authorization': authHeader }
    return custom_headers

def getCustomHeadersForPut (_resource):    
    # Generar un número de secuencia en milisegundos para poder hacer peticiones de forma más rápida  ==> * 1000
    millis = int(round(time.time()))
    
    # Parámetros necesarios para generar la cabecera firmada
    sequence = str(millis)
    apyKey = config.api['key']
    apySecret = config.api['secret']
    method = config.api['methodPut']
    contentType = config.api['contenTypeJson']
    
    # String a firmar
    signString = method + '\n' + contentType + '\n' + sequence + '\n' + _resource
    
    # Firmar el string y generar el valor de la cabecera de autenticación
    authHeader =  'M2C '+ apyKey + ':' + sign_request(apySecret, signString)

    # Montar y devolver todas las cabeceras necesarias en la petición
    custom_headers = { 'Content-Type': contentType,
                       'X-M2C-Sequence': sequence,                    
                       'Authorization': authHeader }
    return custom_headers

# ========================== Llamadas API CLOUD ============================

def customCall(resource):
    url = config.api['endpoint'] + resource 
    return makeRequest(url, _headers = getCustomHeaders(resource))

def listLocations():
    resource = '/' + config.api['version'] + '/locations'
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))


def locationInformation(locationId):
    resource = '/' + config.api['version'] + '/locations/' + locationId
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))

def listMachines():
    resource = '/' + config.api['version'] + '/machines'
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))

def machineInformation(machineId):
    resource = '/' + config.api['version'] + '/machines/' + machineId
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))

def listCaptureGroups(machineId):
    resource = '/' + config.api['version'] + '/machines/' + machineId + '/groups'
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))

def groupInformation(machineId, groupId):
    resource = '/' + config.api['version'] + '/machines/' + machineId + '/groups/' + groupId
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))

def listIndicators(machineId):
    resource = '/' + config.api['version'] + '/machines/'+ machineId + '/indicators'
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))
        
def indicatorInformation(machineId, indicatorId):
    resource = '/' + config.api['version'] + '/machines/' + machineId + '/indicators/' + indicatorId
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))

def listCategories(machineId):
    resource = '/' + config.api['version'] + '/machines/'+ machineId + '/categories'
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))
        
def categoryInformation(machineId, categoryId):
    resource = '/' + config.api['version'] + '/machines/' + machineId + '/categories/' + categoryId
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))

def listSeverities(machineId):
    resource = '/' + config.api['version'] + '/machines/'+ machineId + '/severities'
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))
        
def severityInformation(machineId, severityId):
    resource = '/' + config.api['version'] + '/machines/' + machineId + '/severities/' + severityId
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))

def listProductionLines():
    resource = '/' + config.api['version'] + '/productionLines'
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))
        
def productionLineInformation(productionLineId):
    resource = '/' + config.api['version'] + '/productionLines/' + productionLineId
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))

def segmentInformation():
    resource = '/' + config.api['version'] + '/segment'
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))

def listAlarms(machineId):
    resource = '/' + config.api['version'] + '/machines/' + machineId + '/alarms'
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))
        
def alarmInformation(machineId, alarmId):
    resource = '/' + config.api['version'] + '/machines/' + machineId + '/alarms/' + alarmId
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))

def machineFiles(machineId):
    resource = '/' + config.api['version'] + '/machines/' + machineId + '/files'
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))

def machineFileInformation(machineId, fileName):
    resource = '/' + config.api['version'] + '/machines/' + machineId + '/files/' + fileName
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))

def updateFileInformation(machineId, fileName):
    resource = '/' + config.api['version'] + '/machines/' + machineId + '/files/' + fileName
    url = config.api['endpoint'] + resource    
    body = '{"fileStatus":"demanded"}'
    return makeRequestPut(url, getCustomHeadersForPut(resource), body)

def downloadMachineFile(machineId, fileName):
    resource = '/' + config.api['version'] + '/machines/' + machineId + '/files/' + fileName + '/download'
    url = config.api['endpoint'] + resource    

    resp = requests.get(url,
                        #Custom headers.
                        headers = getCustomHeaders(resource),
                        #Don't verify the cert.
                        verify = False,
                        #It's an stream
                        stream = True,
                        #Proxies
                        proxies = config.proxies)
    
    for inputLine in resp.iter_lines():
        fileInfo = inputLine.decode("utf-8");
        print (fileInfo) # línea que contiene la información previa a la descarga del fichero
        print (1.0)

        if "fileSize" in fileInfo:

            print (1)
            data = json.loads(inputLine)
            print (data['fileSize'])
            print (2)
            size = data['fileSize']

            with open(fileName, 'wb') as f:
                    for chunk in resp.iter_content(chunk_size=size): 
                        if chunk: # filter out keep-alive new chunks
                            f.write(chunk)
                
    return fileInfo

def getData(_machine, modoHuman, _from = None, _to = None):
    resource = '/' + config.api['version'] + '/data?machines=' + _machine
    
    if ("1" == modoHuman):
        resource += '&human=1'
    
    if (not(_from == None or _to == None)):
        resource += '&from=' + str(_from) + '&to=' + str(_to)
    else:
        if (not _from == None): # Si solo se pasa _from, se devuelven datos hasta este momento
            resource += '&from=' + str(_from) + '&to=' + str(int(round(time.time() * 1000)))
    url = config.api['endpoint'] + resource    
    
    print (url)
    
    return makeRequestFromGetData(url, _headers = getCustomHeaders(resource))

def getGroupData(_group, modoHuman, _from = None, _to = None):
    resource = '/' + config.api['version'] + '/data?groups=' + _group
    
    if ("1" == modoHuman):
        resource += '&human=1'
    
    if (not(_from == None or _to == None)):
        resource += '&from=' + str(_from) + '&to=' + str(_to)
    else:
        if (not _from == None): # Si solo se pasa _from, se devuelven datos hasta este momento
            resource += '&from=' + str(_from) + '&to=' + str(int(round(time.time() * 1000)))
    url = config.api['endpoint'] + resource    
    
    print (url)
    
    return makeRequestFromGetData(url, _headers = getCustomHeaders(resource))

def getIndicatorData(_indicator, modoHuman, _from = None, _to = None):
    resource = '/' + config.api['version'] + '/data?indicators=' + _indicator
    
    if ("1" == modoHuman):
        resource += '&human=1'
    
    if (not(_from == None or _to == None)):
        resource += '&from=' + str(_from) + '&to=' + str(_to)
    else:
        if (not _from == None): # Si solo se pasa _from, se devuelven datos hasta este momento
            resource += '&from=' + str(_from) + '&to=' + str(int(round(time.time() * 1000)))
    url = config.api['endpoint'] + resource    
    
    print ('URL:' + url)
    
    return makeRequestFromGetData(url, _headers = getCustomHeaders(resource))

# Lleva a cabo una request solo si viene desde getData. Se hace así para poder controlar mejor
# la respuesta JSON. Ya que viene con bytes y hay que parsearla de una forma especial.
def makeRequestFromGetData (_url, _headers = {}, _stream = False):
    
    # Este try probablemente capture errores a nivel de red
    try:
        resp = requests.get(_url,
                            headers = _headers,
                            verify = False,
                            stream = _stream,
                            proxies = config.proxies)
    except requests.exceptions.RequestException as e:
        print ('La request no se ha llevado a cabo de forma correcta: ' + str(e))
        sys.exit(1)
    
    # Comprobación a nivel de protocolo
    # TODO la API tb fija el código de estado al devolver error, debería comprobar si hay cuerpo y coger el texto del error
    if resp.status_code != 200:
        print ('Error de red: el estado recogido no es 200: %s' % str(resp.status_code))
        print (resp.text)
        sys.exit()
        
    # Comprobación a nivel de aplicación - la respuesta JSON se puede decodificar sin problemas?
    try:

        # Convertimos el string en un fichero para poder leer línea a línea
        buf = io.StringIO(resp.text)

        # Variable donde meteremos los valores JSON
        readedJSON = ""
        
        # Leemos linea a linea y generamos el JSON correspondiente juntando las líneas correspondientes
        for lineNumber, lineContent in enumerate(buf):
            
            if "delimiter=length" not in _url: 
                readedJSON += lineContent
            else:
                # Lineas impares contienen contenido
                if lineNumber % 2 != 0 :
                    readedJSON += lineContent

        decoded = json.loads(readedJSON)
        
    except ValueError as e:
        print ("No se ha podido generar el JSON a partir de la respuesta: %s" % resp.text)
        print ("Respuesta completa:")
        print (resp)
        print (str(e))
        sys.exit()

    # Comprobación a nivel de apliación - la API ha devuelto un status? v1 - solo devuelve status si algo ha ido mal
    try:
        status = int(decoded['status'])
    except TypeError:
        # No existe status, ha ido bien
        status = 200
    except KeyError:
        # No existe status, ha ido bien
        status = 200
    
    if status != 200:
        print ('Error a nivel de aplicación: el estado recogido no es 200: %s' % str(resp))
        sys.exit()
    
    return json.loads(readedJSON)
            
# Lleva a cabo una request y gestiona y muere ante errores
def makeRequest (_url, _headers = {}, _stream = False):
    print (_url + str(_headers) + str(_stream) )
    # Este try probablemente capture errores a nivel de red
    try:
        resp = requests.get(_url,
                            headers = _headers,
                            verify = False,
                            stream = _stream,
                            proxies = config.proxies)
    except requests.exceptions.RequestException as e:
        print ('La request no se ha llevado a cabo de forma correcta: ' + str(e))
        sys.exit(1)
    
    # Comprobación a nivel de protocolo
    # TODO la API tb fija el código de estado al devolver error, debería comprobar si hay cuerpo y coger el texto del error
    if resp.status_code != 200:
        print ('Error de red: el estado recogido no es 200: %s' % str(resp.status_code))
        print (resp.text)
        sys.exit()
    
    # Comprobación a nivel de aplicación - la respuesta JSON se puede decodificar sin problemas?
    try:
        decoded = json.loads(resp.text)
    except ValueError as e:
        print ("No se ha podido decodificar la respuesta JSON. Error: \n Respuesta cruda: %s" % resp.text)
        print ("----")
        print ("Respuesta completa:")
        print (resp)
        sys.exit()

    # Comprobación a nivel de apliación - la API ha devuelto un status? v1 - solo devuelve status si algo ha ido mal
    try:
        status = int(decoded['status'])
    except TypeError:
        # No existe status, ha ido bien
        status = 200
    except KeyError:
        # No existe status, ha ido bien
        status = 200
    
    if status != 200:
        print ('Error a nivel de aplicación: el estado recogido no es 200: %s' % str(resp))
        sys.exit()
    
    return json.loads(resp.text)

# Lleva a cabo una request PUT y gestiona y muere ante errores
def makeRequestPut (_url, _headers = {}, _body = ''):
    print (_url + str(_headers) + str(_body) )
    # Este try probablemente capture errores a nivel de red
    try:
        resp = requests.put(_url,
                            data = _body,
                            headers = _headers,
                            verify = False,
                            proxies = config.proxies)
    except requests.exceptions.RequestException as e:
        print ('La request no se ha llevado a cabo de forma correcta: ' + str(e))
        sys.exit(1)
    
    # Comprobación a nivel de protocolo
    # TODO la API tb fija el código de estado al devolver error, debería comprobar si hay cuerpo y coger el texto del error
    if resp.status_code != 200:
        print ('Error de red: el estado recogido no es 200: %s' % str(resp.status_code))
        print (resp.text)
        sys.exit()
    
    # Comprobación a nivel de aplicación - la respuesta JSON se puede decodificar sin problemas?
    try:
        decoded = json.loads(resp.text)
    except ValueError as e:
        print ("No se ha podido decodificar la respuesta JSON. Error: \n Respuesta cruda: %s" % resp.text)
        print ("----")
        print ("Respuesta completa:")
        print (resp)
        sys.exit()

    # Comprobación a nivel de apliación - la API ha devuelto un status? v1 - solo devuelve status si algo ha ido mal
    try:
        status = int(decoded['status'])
    except TypeError:
        # No existe status, ha ido bien
        status = 200
    except KeyError:
        # No existe status, ha ido bien
        status = 200
    
    if status != 200:
        print ('Error a nivel de aplicación: el estado recogido no es 200: %s' % str(resp))
        sys.exit()
    
    return json.loads(resp.text)