import thread
import time

def print_cout(threadname,delay):
    cout=0
    while cout<10:
        print cout
        time.sleep(delay)
        cout=cout+1
try:
    thread.start_new_thread(print_cout,("First thread",20))
    thread.start_new_thread(print_cout,("Second thread",1))
except:
    print "thread not created"


