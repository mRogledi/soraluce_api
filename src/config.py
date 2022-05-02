# -*- coding: utf-8 -*-


'''
config.py
    Fichero con configuraciones generales
'''

# Configuración de la API
api = dict(
    key = 'S8s3LrUTsE',  
    secret = 'T7D4XG9t3jCLSLfUSu3n',
    method = 'GET',
    methodPut = 'PUT',
    contenType = 'text/plain',
    contenTypeJson = 'application/json',
    endpoint = 'https://api-soraluce.savvyds.com', # Nombre de segmento. 
    version = 'v2'
)

# Configuración de los proxies
proxies = {
    "http": "",
    "https": ""
}
