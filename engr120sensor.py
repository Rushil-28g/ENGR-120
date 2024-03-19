
#Name: Rushil Gandevia, Sofia Daniels, Carmen Batchelor
#Date: March. 19, 2024
#Purpose: Micro-python code for the sensors

import machine
import network
import usocket as socket
import utime as time
import _thread
import json

#RED LED & THERMISTOR CODE- SOFIA DANIELS

#insert GP here
pin_redLED = machine.Pin(, machine.Pin.OUT)
status_red_led = "Off"


def get_led_status():
    return "On" if pin_redLED-
    value() == 1 else "Off"

def checkADC_controlLED():
    global status_red_led
    adc = machine.ADC()#Configure GP# as ADC PIN
    while True:
        lightsensor_value = adc.read_u16()
        print("ADC Value", lightsensor_value)

        if lightsensor_value > 4000 #threshold value
            print("Button is OFF and LEDs are OFF")
            pin_redLED.on()
        
        else:
            print("Button is ON and LEDS are ON")
        pin_redLED.off()
    
        

    status_red_led = get_led_status()#update red led status
    print("RED LED STATUS:", get_led_status)
    time.sleep(1)#wait for one second

####Create a Network Connection

access_name = 'RPI_PICO_AP'
password = '27182818'

ap = network.WLAN(network.AP_IF)
ap.config(essid=access_name, password=password)
ap.active(True)

while ap.active() == False
    pass
print("Connection is successful")
print(ap.ifconfig())


#Define HTTP Response
def webpage():
    status_red_led = get_led_status()
    led_color = "red" if status_red_led == "On" else "gray"



#HTML Portion Here

html = """<html><head>
<title>Pico Web Server</title>
<meta name = "viewpoint" content = "width = device-width, initial-scale=1">
<link rel = "icon href = "data:,">
<style>




return html"""


#Define a function to get the status of the red LED

def get_status():
    status = {
        "REDLEDStatus": status_red_led,

        }
        return json.dumps(status)

_thread.start_new_thread(checkADC_controlLED, ())

#Create a socket server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((' ', 80))
s.listen(5)

        
# This section of the code will have minimum changes. 
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    if request:
        request = str(request)
        print('Content = %s' % request)
        LED_on = request.find('/?redLED_pin=on') # this part of the code could be modified
        LED_off = request.find('/?redLED_pin=off') # this part of the code could be modified

    if LED_on == 6: 
        print('LED ON')
        redLED_pin.value(1)
    elif LED_off == 6:
        print('LED OFF')
        redLED_pin.value(0)


    if request.find("/status") == 6:
        response = get_status()
        conn.send("HTTP/1.1 200 OK\n")
        conn.send("Content-Type: application/json\n")
        conn.send("Connection: close\n\n")
        conn.sendall(response)
    else:
        response = web_page()
        conn.send("HTTP/1.1 200 OK\n")
        conn.send("Content-Type: text/html\n")
        conn.send("Connection: close\n\n")
        conn.sendall(response)
    conn.close()






