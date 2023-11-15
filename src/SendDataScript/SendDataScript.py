#!/usr/bin/python3
import paho.mqtt.client as mqtt
import json
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
lista = []
data_captured = [['luces', 0.0], ['musica', 0.0], ['puerta', 0.99609], ['ruido', 0.0]]
dictionary = dict() 

while (1):  
    i+=1
    val_max = 0
    command_selected = ""
    for item in data_captured:
        #print(item)
        if(item[1] > val_max):
            val_max = item[1]
            command_selected = item[0]
    
    dictionary["command"] = command_selected

    if(command_selected == "musica"):
        dictionary["musica"] = "Sonando"
    else:
        dictionary["musica"] = "Silencio"

    if(command_selected == "luces"):
        dictionary["luces"] = "Encendidas"
    else:
        dictionary["luces"] = "Apagadas" 

    if(command_selected == "puerta"):
        dictionary["puerta"] = "Abierta"
    else:
        dictionary["puerta"] = "Cerrada" 

    if(command_selected == "ruido"):
        dictionary["ruido"] = "Ruido"
    else:
        dictionary["ruido"] = "No Ruido" 

    output = json.dumps(dictionary)
    
    if i>5:
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