
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
pin_redLED = machine.Pin(17, machine.Pin.OUT)
status_red_led = "Off"

IR_led = machine.Pin(0, machine.Pin.OUT)
IR_led = IR_led.value(1)



def get_led_status():
    return "On" if pin_redLED
    value() == 1 else "Off"

def checkADC_control():
    global status_red_led
    light = machine.ADC(26)#Configure GP# as ADC PIN
    thermistor = machine.ADC(27)
    IR_sense = machine.ADC(28) 
    
    while True:
        lightsensor_value = light.read_u16()
        tempsensor_value = thermistor.read_u16()
        IR_sense_value = IR_sense.read_u16()
        
        print("ADC Value", lightsensor_value)

        if lightsensor_value > 4000 and tempsensor_value > 4000 and IR_sense_value > 4000 #Placeholder threshold values will change after testing
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
#However for admission requirements the HTML code has not been abridged to interface with the Micro-python code

"""html = <html><head>
<title>Pico Web Server</title>
<meta name = "viewpoint" content = "width = device-width, initial-scale=1">
<link rel = "icon href = "data:,">
<style>

<!DOCTYPE html>
<!-- Sofia Daniels, Rushil Gandevia, Carmen Batchelor Group 8, ENGR 120, B11, Keiran Letwin -->
<!-- Smart Ln logo, transtions and code merging done by Sofia Daniels -->
<!-- Grass, manual and auto buttons and commenting done by Rushil Gandevia-->
<!-- Time diffrance calculator and code merging done by Carmen Batchelor -->
<head>
<title> 
Smart Ln 
</title> <!-- Makes webpage read as Smart ln in tab bar-->
<style>
/* the styles adjustment of the square (the box that the Smart Ln logo is in)*/
    .square { 
        width: 325px;
        height: 210px; /* adjust boxes size */
        background-color: #B6D0E2; /* adjust boxes colour */
        border: 5px solid #000;
        border-color: green; /* adjust border type and colour */
        display: flex;
        text-align: center;
        justify-content: center;
        align-items: center;
        line-height: 25px; /* adjusts the text location*/
        border-radius: 20px; /* adjusts boxes radius */
        position: absolute; left: 300px; top: 100px;/* adjusts the text location*/
        overflow: hidden;
        animation: fadeIn 1s ease-in-out; /* animation for box from fadeIn style type */
    }
/* the styles adjustment of the auto buton */
   .auto { 
        background-color: #CFD186;
        position: absolute; left: 900px; top: 125px;
        width: 225px;
        height: 135px;
        border-radius: 10px;
        border-color: #1D1E0B;
        font-family: 'Trebuchet MS', sans-serif;
        font-size: 20px;
    } 
/* adjusts text coluring and background coluring for square*/
    .green {
        color: green;
        font-size: 50px;
        font-family: "Andalé Mono", monospace;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .grey {
        color: #71797E;
        font-size: 30px;
        font-family: "Arial", sans-serif; 
    }
/* red auto button*/
    .auto.red {  
        background-color: #f44336; 
    }
/* Manual button styles*/
    .Manual {
  	background-color:#ADF5FF;
  	position: absolute; left: 900px; top: 400px;
  	width: 225px;
  	height: 135px;
  	border-radius: 10px;
  	border-color:#00363D;
  	font-family: 'Trebuchet MS', sans-serif;
  	font-size: 20px;
}
    /* creates and formats the fadeIn animation*/
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0); 
        } 
    } 
/* styles for time diffrance text*/
#timeDifference{ 
	position: absolute; left: 300px; top: 425px;
	font-family: 'Trebuchet MS', sans-serif;
	font-size: 24px;
	}
	/* styles for grass*/
	body {
            
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: flex-end; /* Aligns to the bottom of the page */
        }

        .grass { 
            width: 100%;
            height: 75px; /* Height of the grass */
            background: linear-gradient(90deg, transparent 70%, #2ecc71 70.1%); /* Green color */
            background-size: 15px 15px; /* Size of  grass  */
        }
   
</style>
</head>
<body>

<button id="autoButton" class="auto button">Auto</button>   <!-- The upper button on the right, called auto -->
  <button id="manualButton" class="Manual button">Manual Off</button>         <!-- The lower button on the right, called manual -->

<p id="timeDifference"></p> <!-- The time diffrance text -->

<div class="square">
    <div class="left-align">
        <span class="green">SMART Ln</span>
        <br>
        <span class="grey">Smart Watering System</span>
    </div>
</div> 
<div class="grass">
</div>
<script>
    // Function to change the Auto button's text, colour, size, and position based on the value received
    function updateAutoButton(value) {
	var autoButton = document.getElementById("autoButton");
        if (value === "red") {
            autoButton.textContent = "Auto Off"; // Changes text to watering
            autoButton.classList.add("red"); // changes colour to red
        } 
        else {
            autoButton.textContent = "Auto";   // Reverts text back to auto
            autoButton.classList.remove("red"); // Removes red to change the color back to default
        }
    }
    
    // Simulating receiving values from Raspberry Pi Pico. 
    // This a temp function that will be removed during the final build once the pico can interface with the sensors
    setInterval(function () {
        var valueFromPico = Math.random() < 0.5 ? "green" : "red"; // Randomly choose between 'green' and 'red'
        updateAutoButton(valueFromPico);
    }, 
    3000); // Change text and color every 5 seconds
var startTime = null;

    // Function to record time when the button is pressed
    function recordTime() {
        var currentTime = new Date(); //Captures time when button is pressed for first time
        if (!startTime) {
            startTime = currentTime;
            document.getElementById("manualButton").textContent = "Manual On"; //Changes text to Manual On
        } else {
            var endTime = currentTime; //Captures time when button is pressed for the second time
            var timeDifference = calculateTimeDifference(startTime, endTime); 
            document.getElementById("timeDifference").textContent = "Last Cycle Time: " + timeDifference;
            startTime = null;
            document.getElementById("manualButton").textContent = "Manual Off"; //sets button to off 
        }
    }

    // Function to calculate the time difference between two times
    function calculateTimeDifference(start, end) {
        var difference = end - start;
        var hours = Math.floor(difference / (1000 * 60 * 60));
        var minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((difference % (1000 * 60)) / 1000);
        return hours + " hours, " + minutes + " minutes, " + seconds + " seconds";
    }

    //event listener on button to detect its been pressed
    document.getElementById("manualButton").addEventListener("click", recordTime);
</script>
</body>
</html>


return html"""


#Define a function to get the status of the red LED

def get_status():
    status = {
        "REDLEDStatus": status_red_led,

        }
        return json.dumps(status)

#Create a socket server

_thread.start_new_thread(checkADC_control, ())

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






