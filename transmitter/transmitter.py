import keyboard
import time
import socket

s=socket.socket()
def Connect():
    global s
    host="192.168.0.143"
    port=9999
    s.bind((host,port))
    s.listen(5)
    c,a=s.accept()
    print(a[0])
    mes='x'
    while True:
        if (keyboard.is_pressed('a') or keyboard.is_pressed('w') or keyboard.is_pressed('s') or keyboard.is_pressed('d') or keyboard.is_pressed('a+w') or keyboard.is_pressed('w+d') or keyboard.is_pressed('w+a') or keyboard.is_pressed('d+w') or keyboard.is_pressed('s+a') or keyboard.is_pressed('a+s') or keyboard.is_pressed('s+d') or keyboard.is_pressed('d+s') or keyboard.is_pressed('e')):
            key=str(keyboard.get_hotkey_name())
            time.sleep(0.1)
            print(key)
            c.send(str.encode(key))
        elif keyboard.is_pressed('e'):
            key = str(keyboard.get_hotkey_name())
            time.sleep(0.1)
            c.send(str.encode(key))
            c.close()
            break
        else:
            c.send(str.encode(mes))
            continue

Connect()

