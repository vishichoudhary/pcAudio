# client side code
import socket
import pyaudio

#record
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
#RECORD_SECONDS = 40

#HOST = '192.168.43.232'    # The remote host
#PORT = 50007              # The same port as used by the server
HOST=raw_input("Enter the proxy of Server")
PORT=raw_input("Enter the port of application")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

print("*recording")

while True:
 data  = stream.read(CHUNK)
 s.sendall(data)

print("*done recording")

stream.stop_stream()
stream.close()
p.terminate()
s.close()

print("*closed")
