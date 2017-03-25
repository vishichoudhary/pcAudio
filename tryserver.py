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

CHUNK=1024
FORMAT=pyaudio.paInt16
CHANNELS=1
RATE=44100

class sendRecord(threading.Thread):
    def __init__(self):
	        threading.Thread.__init__(self)
	        self.WAVE_OUTPUT_FILENAME="sever_output.wav"
	        self.frames=[]
	        self.p=pyaudio.PyAudio()
	        self.stream=self.p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
	        self.sendData=''
    def run(self):
        	self.sendRecordFun()
    def sendRecordFun(self):
	        while 1:
	            self.sendData=self.stream.read(CHUNK)
	            conn.sendall(self.sendData)
	            print "server sendRecord"
	            time.sleep(.1)
            
class recievePlay(threading.Thread):
    def __init__(self):
	    threading.Thread.__init__(self)
	    self.WAVE_OUTPUT_FILENAME="sever_output.wav"
	    self.frames=[]
	    self.p1=pyaudio.PyAudio()
	    self.stream1=self.p1.open(format=FORMAT,channels=CHANNELS,rate=RATE,output=True,frames_per_buffer=CHUNK)
	    self.data='123'

    def run(self):
        self.recievePlayfun()

    def recievePlayfun(self):
        self.data = conn.recv(1024)
        self.stream1=self.p1.open(format=FORMAT,channels=CHANNELS,rate=RATE,output=True,frames_per_buffer=CHUNK)
        while self.data != '':
            self.stream1.write(self.data)
            self.data = conn.recv(1024)
            print "server recieve play"
            time.sleep(.1)

threadone=sendRecord()
threadtwo=recievePlay()
threadone.start()
threadtwo.start()
