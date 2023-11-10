import serial
import numpy as np
import time
import wave
sample_length = 30
serial_port_name = "COM3"
print("Start audio recording...")
ser = serial.Serial(serial_port_name, 115200, timeout=None)     # Create Serial link
result_ = ""
samples = int(16000 * sample_length)
lista = []
start_time = time.time()
for x in range(samples):
    ser.read_until()
    cc1 = ser.read(2)
    #print(cc1)
    lista.append(int.from_bytes(cc1, "big"))
print("Stop audio recording.")
print("Audio length: " + str(time.time()-start_time) + " segundos")
print("Saving audio...")
audio_data = np.array([int(value) for value in lista])
with wave.open('audio/audio_output.wav', 'w') as audio_file:
    audio_file.setparams((1, 2, 32000, 0, 'NONE', 'not compressed'))
    audio_file.writeframes(audio_data.tobytes())
ser.close()
audio_file.close()
print('Audio saved as audio_output.wav')
