from wifi_lib import conecta # conecta na intenet
from umqtt.simple import MQTTClient # Protocolo MQTT
import machine
import time
import dht

dht11=dht.DHT11(machine.Pin(4)) # Sensor DHT11
#r=machine.Pin(27,machine.Pin.OUT) #Rele

SERVER = "mqtt.thingspeak.com"  # inicio do processo do protocolo MQTT
mqtt_port = 1883

user_id ='mwa0000019607971'
mqtt_api_key = 'VGSV5J5V7ITLUWOY'
mqtt_client_id = '00e90a5af7ee4e859514dc8173392759'
WRITE_API_KEY = 'LCYVUBRPQANQIVDA'
READ_API_KEY = 'SQ3UBRQX62OW1V8U'
CHANNEL_ID = "1149367" 

import urequests
print("Conectando...")
station = conecta("NET_2G0B3BB3", "4F0B3BB3") #chama a função de acesso a intenet dentro da LIB wifi_lib
if not station.isconnected():
    print("Não conectado!...")
else:
    print("Conectado!...")
    ip = station.ifconfig()
    print("IP : ", ip)
 
def readDht(): 
    dht11.measure()        
    return dht11.temperature(), dht11.humidity()

def main():
    print("Rodando....")
    while True:
        temp, hum = readDht()
        time.sleep(20)
      # if dht11.temperature()>=25: # condição para acionar o RELE acima de 25º.
      #    r.value(1)
      #    rele = 1            
      # else:
      #     r.value(0)
      #     rele = 0           
           
        #client = MQTTClient("umqtt_client", SERVER, mqtt_api_key,mqtt_client_id, mqtt_port)
       # client = MQTTClient(mqtt_client_id, SERVER, mqtt_port, user_id, mqtt_api_key)        
        SERVER = "mqtt.thingspeak.com"  # inicio do processo do protocolo MQTT
        client = MQTTClient("umqtt_client", SERVER)
        CHANNEL_ID = "1149367" 
        WRITE_API_KEY = "LCYVUBRPQANQIVDA"
        topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY
        payload = "field1="+str(temp)+"&field2="+str(hum)#+"&field3="+str(rele)
        client.connect() 
        client.publish(topic, payload)
        client.disconnect()
        print("Temp={}   Umid={}".format(dht11.temperature(), dht11.humidity()))
        
main()