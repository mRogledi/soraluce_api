# -*- coding: utf-8 -*-
import requests
import time
import json
import config
import sys

'''
streamData.py
    Se encarga de hacer el streaming en un segundo plano
'''

# Para evitar el warning InsecureRequestWarning http://urllib3.readthedocs.org/en/latest/security.html#disabling-warnings
# Se usa urllib3 dentro de request, hay que afinar el import http://goo.gl/3YtXMz
# Otro: https://stackoverflow.com/questions/27981545/suppress-insecurerequestwarning-unverified-https-request-is-being-made-in-pytho
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

    # Montar y devolver todas las cabeceras necesarias en la petición
    custom_headers = {    'Content-Type': contentType,
                        'X-M2C-Sequence': sequence,                    
                          'Authorization': authHeader }
    return custom_headers
        
def listLocations ():
    resource = '/' + config.api['version'] + '/locations'
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))


def listMachines(locationId):
    resource = '/' + config.api['version'] + '/locations/' + locationId +'/machines'
    url = config.api['endpoint'] + resource    
    return makeRequest(url, _headers = getCustomHeaders(resource))
    

# Lleva a cabo una request y gestiona y muere ante errores
def makeRequest (_url, _headers = {}, _verifySSL = False, _stream = False):
    
    print ("Llamando a " + _url)
    
    # Este try probablemente capture errores a nivel de red
    try:
        resp = requests.get(_url,
                            headers = _headers,
                            verify = _verifySSL,
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

    # Comprobacón a nivel de apliación - la API ha devuelto un status? v1 - solo devuelve status si algo ha ido mal
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

# Se encarga de stremear y guardar en el fichero de salida. También lo escribe por consola para poder ver que está recibiendo datos.
def streamResource(endpoint, resource):
    print ("Llamando a " + endpoint + resource)
    print ("Realizando streaming. Cerrar esta ventana cuando se quiera cortar el streaming.")
    
    resp = requests.get(endpoint + resource,
                        #Custom headers.
                        headers = getCustomHeaders(resource),
                        #Don't verify the cert.
                        verify = False,
                        #It's an stream
                        stream = True,
                        #Proxies
                        proxies = config.proxies)
        
    for line in resp.iter_lines():
        # No imprimimos la linea de los byte
        if not line.isdigit():
            res = json.dumps(json.loads(line.decode()))
            with open("stream.dat", "a") as outfile:
                print (str(res))
                outfile.write(str(res))
                outfile.write(str("\n"))



######################################################################################################################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################
# Llamada desde fuera
######################################################################################################################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################


# Streamea los datos de una o más máquinas
def startStreaming(endpoint, resource): 
    print ("Realizando streaming contra la URL: " + endpoint + resource)
    streamResource(endpoint, resource)
    
# Streamea los datos de una máquina y devuelve también backfilling (datos anteriores al timestamp de la petición)
def startStreamingWithBackfilling(endpoint, resource): 
    print ("Realizando streaming with backfilling contra la URL: " + endpoint + resource)
    # Calculo del from para el backfilling. Se pueden pedir hasta 8 horas de backfilling
    streamResource(endpoint, resource)
