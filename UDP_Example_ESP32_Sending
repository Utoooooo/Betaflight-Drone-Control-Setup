#include <HardwareSerial.h>
#include <MSP.h>
#include <Wire.h>
#include <VL53L1X.h>
#include <WiFi.h>
#include <WiFiUdp.h>

//Wifi UDP Settings
const char* ssid = "<Your ssid>";
const char* password = "<Your password>";
const uint16_t udpPort = 8888;  // Port number to use for UDP

WiFiUDP udp;

void setup() {

  //Connect to WiFi hotspot
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    // Serial.println("Connecting to WiFi...");
  }
  udp.begin(udpPort);
}

void loop() {
  uint8_t buf[5] = {1,2,3,4,5};  // Create a buffer to hold the received data
  int packetSize = udp.parsePacket();
  if (packetSize) {
    Serial.println('received');
    udp.beginPacket(udp.remoteIP(), udp.remotePort());
    udp.write(1);
    udp.endPacket();
  }
}
