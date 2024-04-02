import machine
import network
import usocket as socket
import utime as time
import _thread
import json

# RED LED & THERMISTOR CODE - SOFIA DANIELS

# Insert GP here
pin_redLED = machine.Pin(17, machine.Pin.OUT)
status_red_led = "Off"


def get_led_status():
    return "On" if pin_redLED.value() == 1 else "Off"


def checkADC_control():
    global status_red_led
    light = machine.ADC(26)
    thermistor = machine.ADC(27)
    IR_sense = machine.ADC(28)

    while True:
        try:
            lightsensor_value = light.read_u16()
            tempsensor_value = thermistor.read_u16()
            IR_sense_value = IR_sense.read_u16()

            print("ADC Value", lightsensor_value)

            if lightsensor_value < 50000 and tempsensor_value < 600 and IR_sense_value < 30000:
                print("Bright, Hot, and Unblocked")
                pin_redLED.on()
            else:
                print("Dark, Cold, or Blocked")
                pin_redLED.off()

            status_red_led = get_led_status()  # update red led status
            print("RED LED STATUS:", get_led_status())
        except Exception as e:
            print("Exception in ADC thread:", e)
        time.sleep(1)  # wait for one second


#### Create a Network Connection

access_name = 'RPI_PICO_AP'
password = '27182818'

ap = network.WLAN(network.AP_IF)
ap.config(essid=access_name, password=password)
ap.active(True)

while ap.active() == False:
    pass
print("Connection is successful")
print(ap.ifconfig())


# Define HTTP Response
def webpage():
    status_red_led = get_led_status()
    led_color = "red" if status_red_led == "On" else "gray"

    # HTML Portion Here
    # However for admission requirements the HTML code has not been abridged to interface with the Micro-python code
    html = """
    <html>
    <head>
    <title>Pico Web Server</title>
    <meta name="viewpoint" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <style>
    /* Styles omitted for brevity */
    </style>
    </head>
    <body>
    <button id="autoButton" class="auto button">Auto</button>
    <button id="manualButton" class="Manual button">Manual Off</button>
    <p id="timeDifference"></p>
    <div class="square">
        <div class="left-align">
            <span class="green">SMART Ln</span>
            <br>
            <span class="grey">Smart Watering System</span>
        </div>
    </div> 
    <div class="grass"></div>
    <script>
        // JavaScript code omitted for brevity
    </script>
    </body>
    </html>
    """
    return html


# Define a function to get the status of the red LED
def get_status():
    status = {
        "REDLEDStatus": status_red_led,
    }
    return json.dumps(status)


# Create a socket server
_thread.start_new_thread(checkADC_control, ())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.10', 80))  # Change IP address to the Pi Pico's IP address
s.listen(5)

# This section of the code will have minimum changes.
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    if request:
        request = str(request)
        print('Content = %s' % request)
        LED_on = request.find('/?redLED_pin=on')
        LED_off = request.find('/?redLED_pin=off')

        if LED_on == 6:
            print('LED ON')
            pin_redLED.value(1)
        elif LED_off == 6:
            print('LED OFF')
            pin_redLED.value(0)

        if request.find("/status") == 6:
            response = get_status()
            conn.send("HTTP/1.1 200 OK\r\n")
            conn.send("Content-Type: application/json\r\n")
            conn.send("Connection: close\r\n\r\n")
            conn.sendall(response)
        else:
            response = webpage()
            conn.send("HTTP/1.1 200 OK\r\n")
            conn.send("Content-Type: text/html\r\n")
            conn.send("Connection: close\r\n\r\n")
            conn.sendall(response)
    conn.close()
