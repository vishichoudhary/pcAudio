#tryserver
import socket
import pyaudio
import time
import threading

HOST=raw_input("Enter the ip of server")
PORT=int(raw_input("Enter the port of app"))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr=s.accept()

class sendRecord(threading.Thread):
    def __init__(self):
	        threading.Thread.__init__(self)
	        self.CHUNK=1024
	        self.FORMAT=pyaudio.paInt16
	        self.CHANNELS=1
	        self.RATE=44100
	        self.WAVE_OUTPUT_FILENAME="sever_output.wav"
	        self.frames=[]
	        self.p=pyaudio.PyAudio()
	        self.stream=self.p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
	        self.sendData=''
    def run(self):
        	sendRecordFun()
    def sendRecordFun(self):
	        while 1:
	            self.sendData=self.stream.read(CHUNK)
	            self.s.sendall(sendData)
	            time.sleep(.1)
            
class recievePlay(threading.Thread):
    def __init__(self):
	    threading.Thread.__init__(self)
	    self.CHUNK=1024
	    self.FORMAT=pyaudio.paInt16
	    self.CHANNELS=1
	    self.RATE=44100
	    self.WAVE_OUTPUT_FILENAME="sever_output.wav"
	    self.frames=[]
	    self.p1=pyaudio.PyAudio()
	    self.stream1=self.p1.open(format=FORMAT,channels=CHANNELS,rate=RATE,output=True,frames_per_buffer=CHUNK)
	    self.data='123'

    def run(self):
        recievePlayfun()

    def recievePlayfun():
        self.data = conn.recv(1024)
        self.stream1=self.p1.open(format=FORMAT,channels=CHANNELS,rate=RATE,output=True,frames_per_buffer=CHUNK)
        while self.data != '':
            self.stream1.write(data)
            self.data = conn.recv(1024)
            time.sleep(.1)

threadone=sendRecord()
threadtwo=recievePlay()
threadone.start()
threadtwo.start()
