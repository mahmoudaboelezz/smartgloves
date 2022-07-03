# get data from http://192.168.1.224/read every second
ip = 'http://192.168.1.224/read'
import requests
from time import sleep
# get request from url and return the data
def get_data(url):
    response = requests.get(url)
    data = response.json()
    return data

while True:
    # get data from url
    data = get_data(ip)
    # print the data
    print(data)
    # sleep for 1 second
    sleep(.1)    