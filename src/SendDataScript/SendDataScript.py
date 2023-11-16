#!/usr/bin/python3
import serial
import paho.mqtt.client as mqtt
import json
import time
#Functions
def on_publish(client,userdata,result):             #create function for callback
    print("Data published to thingsboard \n")
    pass
#Serial connection
ser = serial.Serial(
    port='COM3',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=200\
)
print("Connected to: " + ser.portstr + "\n")
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
#Variables
i = 0
j = 0
x = 0
valorinicial = False
lista = []
dictionary = dict()

while(1):
    data_captured = ser.readline().decode().strip().split()
    data_captured[1] = float(data_captured[1])
    lista.append(data_captured)
    i+=1   
    j+=1
    val_max = 0.6
    command_selected = "ruido"
    if(j == 4):
        for item in lista:
            if(item[1] > val_max):
                val_max = item[1]
                command_selected = item[0]
        dictionary["command"] = command_selected
        print("El comando elegido es: " + command_selected)
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
        lista = []
        j = 0
        print("\nData to send:")
        print(output)
        print("\n")
        client.publish(topic, output)