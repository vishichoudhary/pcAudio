# Echo server program
import socket
import pyaudio
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 20
WAVE_OUTPUT_FILENAME = "server_output.wav"
WIDTH = 2
frames = []

HOST=raw_input("Enter the proxy")
PORT=int(raw_input("Enter the port"))

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(WIDTH),channels=CHANNELS,rate=RATE,output=True,frames_per_buffer=CHUNK)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr

data = conn.recv(1024)
while data != '':
    stream.write(data)
    data = conn.recv(1024)

stream.stop_stream()
stream.close()
p.terminate()
conn.close()
