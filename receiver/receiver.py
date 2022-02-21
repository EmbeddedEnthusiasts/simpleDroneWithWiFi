###Runs on ESP8266 (NodeMCU running MicroPython)

import socket
from machine import Pin,PWM
import network
import sys

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        #sta_if.connect('Aavishkar', 'Tinnu$276')#Replace your WiFi name and Password accordingly, here within single quotes for both
        sta_if.connect('POCO F1', '18765432')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

#host = '192.168.0.143'
host = '192.168.43.187'
port = 9999

p2 = PWM(Pin(2)) #D4 up and down
p2.freq(50)

p4 = PWM(Pin(4)) #D2 pitch
p4.freq(50)

p5 = PWM(Pin(5)) #D4 roll
p5.freq(50)

p12 = PWM(Pin(12)) #D4 yaw
p12.freq(50)

do_connect()
s = socket.socket()
s.connect((host,port))
dc2=0
dc3=1
dc4=1
dc5=1
while True:
    data=str(s.recv(1024),"utf-8")
    #print(data)
    if 'up' in data:
        dc2+=10
        if dc2 > 1023:
            dc2=1023
        elif dc2 < 0:
            dc2 = 0
        print(int(dc2))
        p2.duty(int(dc2))
    if 'down' in data:
        dc2-=10
        if dc2 > 1023:
            dc2=1023
        elif dc2 < 0:
            dc2 = 0
        print(int(dc2))
        p2.duty(int(dc2))
        
    #if 'a' in data:
        
        
    if 'e' in data:
        p2.deinit()
        s.close()
        sys.exit()
    else: 
        #p2.duty(0)
        continue
        
    
    
