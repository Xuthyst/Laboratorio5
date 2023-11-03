import serial
import sys
import numpy as np
import time
import wave

def record_audio(time_stamp,serial_port_name,sample_length):
    print("Start audio recording...")
    ser = serial.Serial(serial_port_name, 115200, timeout=None)     # Create Serial link
    result_ = ""
    samples = int(16000 * sample_length)
    lista = []
    start_time = time.time()
    for x in range(samples):
      ser.read_until()
      cc1 = ser.read(2)
      lista.append(int.from_bytes(cc1, "big"))
    print("Stop audio recording.")
    print("Audio length:",time.time()-start_time)
    #NUEVO
    print("Saving audio...")
    # Crea un archivo de audio WAV
    # Convierte los datos en un arreglo de números
    audio_data = np.array([int(value) for value in lista])
    with wave.open('audio_output.wav', 'w') as audio_file:
        audio_file.setparams((1, 2, 32000, 0, 'NONE', 'not compressed'))
        audio_file.writeframes(audio_data.tobytes())
    ser.close()
    audio_file.close()

if __name__ == '__main__':
    #Importing sys parameters
    print("TEST MODE audio !")
    par_time_stamp = "test"
    par_serial_port_name = "COM3"
    par_sample_length = 5
    record_audio(par_time_stamp,par_serial_port_name,par_sample_length)#!/usr/bin/python3