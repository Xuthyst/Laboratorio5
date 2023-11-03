#!/usr/bin/python3
import serial
import csv
import numpy as np
import wave
ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=200
)
valores = []
print("Conectado a: " + ser.portstr)
print("Leyendo y mostrando lectura de puerto serial: ")
while(1):
    linea_serie = ser.readline().decode().strip()
    print("El valor actual es: " + linea_serie)
    if(linea_serie == "EOF"):
        print("La transmisión de datos finalizo")
        break
    valores.append(linea_serie)
print("Estos son los valores:")
#print(valores)
# Convierte los datos en un arreglo de números
audio_data = np.array([int(value) for value in valores])
print(audio_data)
# Crea un archivo de audio WAV
with wave.open('audio_output.wav', 'w') as audio_file:
    audio_file.setparams((1, 2, 16000, 0, 'NONE', 'not compressed'))
    audio_file.writeframes(audio_data.tobytes())
ser.close()