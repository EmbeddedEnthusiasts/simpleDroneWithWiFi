###Runs on ESP8266 (NodeMCU running MicroPython)

import socket
from machine import Pin,PWM
import network 

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Aavishkar', 'Tinnu$276') #Replace your WiFi name and Password accordingly, here within single quotes for both
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

host = '192.168.0.143'
port = 9999

p2 = PWM(Pin(2)) #D4
p2.freq(50)
do_connect()
s = socket.socket()
s.connect((host,port))
duty_cycle=1

while True:
    data=str(s.recv(1024),"utf-8")
    #print(data)
    if data == 'w':
        duty_cycle+=30
        if duty_cycle > 1023:
            duty_cycle=1023
        elif duty_cycle < 0:
            duty_cycle = 0
        print(int(duty_cycle))
        p2.duty(int(duty_cycle))
    elif data == 's':
        duty_cycle/=3
        if duty_cycle > 1023:
            duty_cycle=1023
        elif duty_cycle < 0:
            duty_cycle = 0
        print(int(duty_cycle))
        p2.duty(int(duty_cycle))
    elif data == 'e':
        p2.deinit()
        s.close()
    else: 
        #p2.duty(0)
        continue
        
