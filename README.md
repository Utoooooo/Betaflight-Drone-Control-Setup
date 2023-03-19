# Betaflight-Drone-Control-Setup
## Setting up the environment:

### Flight Controller Configurator and Python environment

1. Install **Betaflight Configurator** : https://github.com/betaflight/betaflight-configurator/releases/tag/10.9.0

2. Install **Python 3**: https://www.python.org/downloads/

3. Install the following libraries: 
    * Numpy 
    * pySerial

### Arduino environment setup:

You can use either Arduino IDE or VS Code with Arduino Extension:
    
1. Install Arduino IDE: https://www.arduino.cc/en/software.

2. Add ESP32 boards support to the Arduino IDE by following this tutorial: https://randomnerdtutorials.com/installing-the-esp32-board-in-arduino-ide-windows-instructions/

3. Download VL53L1X Distance Sensor library.

4. Download and install the MSP.h library in .zip file: https://github.com/fdivitto/MSP/tree/master. For installation, there's 2 ways of doing this:
   * Open Arduino IDE, **Sketch** tab, **Include Library**, click 'Add .ZIP Library'.
   * Unzip the file, add contents into the same folder as the Arduino script.


Alternatively, if you're using VS Code with Arduino Extension, please follow this instruction: 
https://circuitstate.com/tutorials/how-to-use-vs-code-for-creating-and-uploading-arduino-sketches/#:~:text=Launch%20VS%20Code%20and%20from,version)%20installations%20on%20a%20system.
