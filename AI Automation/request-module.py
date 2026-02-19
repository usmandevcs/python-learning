# REQUEST MODULE
'''
Request module is an python library thay enables
developers to easily make HTTP requests to interact 
with web services and APIs.
this module simplifies the process of sending requests
and handling responses.
'''
import requests
response = requests.get('https://google.com')
print(response.text)  