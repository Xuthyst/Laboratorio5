#!/usr/bin/python3
import serial
import csv

fileName = "flex.csv"  # Cambio el nombre del archivo de salida
encabezado = ["Dato1", "Dato2", "Dato3", "Dato4", "Dato5", "Dato6"]
ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=200
)
print("Conectado a: " + ser.portstr)
print("Creando archivo CSV")
valores = []
file = open(fileName, mode='w', newline='')
filewrite = csv.writer(file)
filewrite.writerow(encabezado)
lineas_en_blanco = 0

while lineas_en_blanco < 20:
    linea_serie = ser.readline().decode().strip()
    if not linea_serie:
        # Se encontró una línea en blanco, incrementar el contador.
        lineas_en_blanco += 1
    else:
        # No es una línea en blanco, guardarla en el CSV y reiniciar el contador de líneas en blanco.
        valores.extend(linea_serie.split(','))
        if len(valores) == 6:
            print("Escribiendo una nueva línea en el CSV")
            filewrite.writerow(valores)
            valores = []

ser.close()
file.close()