#!/usr/bin/python3
import paho.mqtt.client as mqtt
import json
import time
#Functions
def on_publish(client,userdata,result):             #create function for callback
    print("data published to thingsboard \n")
    pass

#Datos para la conexión con el cliente:
broker = "iot.eie.ucr.ac.cr"
port = 1883
topic = "v1/devices/me/telemetry"
username = "NANO_10_SD"
password = "r83olk7lufc6wh3yj7wo"    
#Establecemos los parámetros de conexión
client = mqtt.Client(username)
client.on_publish = on_publish
client.username_pw_set(password)
client.connect(broker, port, keepalive=60)

i = 0
x = 0
valorinicial = False
lista = []
data_captured = [['luces', 0.0], ['musica', 0.0], ['puerta', 0.99609], ['ruido', 0.0]]
dictionary = dict() 

while (1):  
    time.sleep(2)
    i+=1
    val_max = 0
    command_selected = ""
    for item in data_captured:
        #print(item)
        if(item[1] > val_max):
            val_max = item[1]
            command_selected = item[0]
    
    dictionary["command"] = command_selected

    #Valores Iniciales
    if(valorinicial == False):
        dictionary["musica"] = "Silencio"
        dictionary["luces"] = "Apagadas"
        dictionary["puerta"] = "Cerrada"
        valorinicial = True

    if(command_selected == "musica"):
        if (dictionary["musica"] == "Sonando"):
            dictionary["musica"] = "Silencio"
        else:
            dictionary["musica"] = "Sonando"

    if(command_selected == "luces"):
        if (dictionary["luces"] == "Encendidas"):
            dictionary["luces"] = "Apagadas"
        else:
            dictionary["luces"] = "Encendidas" 

    if(command_selected == "puerta"):
        if(dictionary["puerta"] == "Abierta"):
            dictionary["puerta"] = "Cerrada"
        else:
            dictionary["puerta"] = "Abierta" 

    output = json.dumps(dictionary)
    
    print(dictionary)
    print(output)

    if i>2000:
        for ind in range(len(data_captured)):
            if x == ind:    
                data_captured[ind][1] = 0.99609
            else:
                data_captured[ind][1] = 0.0 
        i=0
        x+=1
        if x == 4:
            x = 0
    
    client.publish(topic, output)

    #print("Los datos recibidos son:")
    #print(data_captured)
    #print("Identificando comando recibido...")
    #print("El comando es: " + command_selected + "\n")