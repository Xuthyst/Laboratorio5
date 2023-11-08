#!/usr/bin/python3
import serial
import paho.mqtt.client as mqtt
import json
#Functions
def on_publish(client,userdata,result):             #create function for callback
    print("data published to thingsboard \n")
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
print("Connected to: " + ser.portstr)
#Datos para la conexión con el cliente:
# broker = "iot.eie.ucr.ac.cr"
# port = 1883
# topic = "v1/devices/me/telemetry"
# username = "STM"
# password = "ozwnzj5hfdmn1nyjlxev"    
# #Establecemos los parámetros de conexión
# client = mqtt.Client(username)
# client.on_publish = on_publish
# client.username_pw_set(password)
# client.connect(broker, port, keepalive=60)
i = 0
j = 0
lista = []
dictionary = dict()
while i<12:#Taking 3 test 
    data_captured = ser.readline().decode().strip().split()
    data_captured[1] = float(data_captured[1])
    lista.append(data_captured)
    i+=1   
    j+=1
    val_max = 0
    command_selected = ""
    if(j == 4):
        for item in lista:
            if(item[1] > val_max):
                val_max = item[1]
                command_selected = item[0]
        dictionary["command"] = command_selected
        output = json.dumps(dictionary)
        #print(output)
        #client.publish(topic, output)
        print(lista)
        print("El comando es: " + command_selected)
        j = 0
        lista = []
ser.close()